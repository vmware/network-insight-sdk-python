# Python SDK Examples

# Script will fetch Flows matching certain search criteria
# Along with the flow information it will fetch the correlated
# VMs and send it to vRealize Log Insight via its API
#
# Usage:  python flows_to_vrli.py --platform_ip your-vrni-platform --username admin@local --password 'VMware1!' --vrli_server your-vrli-server
#
# Martijn Smit <msmit@vmware.com / @smitmartijn>

import time
import logging
import re
import socket
import requests
from datetime import datetime
import init_api_client
import swagger_client
from sdk_utilities import get_referenced_entity_name
import utilities

# this is the search call that will be used to limit the returned flows.
# the active one below returns all flows that involve a VM and returns only flows that have been active in the last 24 hours
# if you want to run this script more than every 24 hours, adjust the time. "in last 4 hours" is also valid
CONFIG_FILTER_STRING = "((flow_tag = TAG_SRC_IP_VM) or (flow_tag = TAG_DST_IP_VM)) in last 24 hours"

# you can also change the filter to anything the search API supports. Below are a few examples for inspiration:
#
# filter on a destination IP address
# CONFIG_FILTER_STRING = "destination_ip.ip_address = '192.168.21.20'"
# filter on a specific network port
# CONFIG_FILTER_STRING = "port = 123"
# retrieve only flows related to this vSphere cluster
# CONFIG_FILTER_STRING = "source_cluster.name = 'HaaS-Cluster-6'"
# filter by a specific network
# CONFIG_FILTER_STRING = "destination_l2_network.name = 'vlan-1014'"
# return only flows with security tag 'OPI' and exclude internet traffic
# CONFIG_FILTER_STRING = "(source_security_tags.name = 'OPI' or destination_security_tags.name='OPI') and (flow_tag != TAG_INTERNET_TRAFFIC)"
# return only internet traffic and from a specific vSphere cluster
# CONFIG_FILTER_STRING = "((flow_tag = TAG_INTERNET_TRAFFIC) and (source_datacenter.name = 'HaaS-1'))"

def send_vrli_message(message, timestamp_milliseconds, fields, args):
    cfapi_port = 9543 if args.vrli_port is None else args.vrli_port
    vrli_url = "https://{}:{}/api/v1/events/ingest/0".format(args.vrli_server, cfapi_port)

    body = {}
    body['text'] = message
    body['timestamp'] = timestamp_milliseconds
    if fields:
        body['fields'] = [{'name': str(k), 'content': str(v)} for k, v in fields.items()]

    try:
        r = requests.post(vrli_url, json={"events": [body]}, verify=False)
    except requests.exceptions.HTTPError as err:
        raise ServerError(err)

# cache Virtual Machine names to prevent duplicate lookups
# cache_vms[entity_id] = vm_name
cache_vms = {}

def lookup_vm_name(vm_entity):
    # resolve VM Name from the entity_id
    vm_name = None
    # check cache first
    if vm_entity.entity_id in cache_vms:
        vm_name = cache_vms[vm_entity.entity_id]
        print("Found src {} in cache!".format(vm_name))
    else:
        vm_name = None if vm_entity is None else get_referenced_entity_name(referenced_entity=vm_entity)
        if vm_name is None:
            pass
        else:
            # save to cache
            cache_vms[vm_entity.entity_id] = vm_name

    return vm_name

def main(args):
    # Create search API client object
    search_api = swagger_client.SearchApi()
    logger = logging.getLogger("vrni_sdk")
    filter_string = CONFIG_FILTER_STRING

    # Create request parameters required for search APIs
    public_api_search_request_params = dict(entity_type=swagger_client.EntityType.FLOW, filter=filter_string, size=100)
    logger.info("Get all flows with filter = [{}]".format(filter_string))
    search_payload = swagger_client.SearchRequest(**public_api_search_request_params)

    # to prevent default lookups, keep a record
    destination_ip_port_protocol = []

    while True:
        # Call the search API
        api_response = search_api.search_entities(body=search_payload)
        logger.info("Response attributes: Total Count: {} Start Time: {} End Time: {}".format(api_response.total_count, datetime.fromtimestamp(api_response.start_time), datetime.fromtimestamp(api_response.end_time)))
        #print(api_response)

        for result in api_response.results:
            entities_api = swagger_client.EntitiesApi()
            flow_timestamp = result.time
            flow_details = entities_api.get_flow(id=result.entity_id, time=flow_timestamp)
            flow_name = flow_details.name.encode('utf-8').strip()
            logger.info("Flow: {}".format(flow_name))

            # Ignore flows we've already seen
            dest_ip_port_protocol = '{}-{}--{}-{}'.format(flow_details.destination_ip.ip_address, flow_details.protocol, flow_details.port.start, flow_details.port.end)
            if dest_ip_port_protocol in destination_ip_port_protocol:
                continue
            destination_ip_port_protocol.append(dest_ip_port_protocol)

            # get source VM Name, if any
            src_vm_name = None
            if flow_details.source_vm != None:
                src_vm_name = lookup_vm_name(flow_details.source_vm)

            # get destination VM Name, if any
            dst_vm_name = None
            if flow_details.destination_vm != None:
                dst_vm_name = lookup_vm_name(flow_details.destination_vm)

            # for debugging purposes
            #print("Flow info: ")
            #print("Source: ", flow_details.source_ip.ip_address, " (",src_vm_name,") Destination: ", flow_details.destination_ip.ip_address, " (",dst_vm_name,")")
            #print("Port: ", flow_details.port.iana_port_display, " Protocol: ", flow_details.protocol)

            # create syslog message
            datetime_str = datetime.fromtimestamp(flow_timestamp)
            syslog_msg = 'vRNI-Flow: {} {} {} {}'.format(datetime_str, flow_details.firewall_action, flow_details.protocol, flow_name)

            print(syslog_msg)

            # form the fields parameter, which will show up as 'Fields' in vRLI
            log_fields = {}
            log_fields["__vrni_flow_firewall_action"] = flow_details.firewall_action
            log_fields["__vrni_flow_firewall_rule_id"] = flow_details.firewall_rule_id
            log_fields["__vrni_flow_traffic_type"] = flow_details.traffic_type
            log_fields["__vrni_flow_tag"] = flow_details.flow_tag
            log_fields["__vrni_flow_source_ip"] = flow_details.source_ip.ip_address
            log_fields["__vrni_flow_destination_ip"] = flow_details.destination_ip.ip_address
            log_fields["__vrni_flow_port"] = flow_details.port.display
            log_fields["__vrni_flow_port_name"] = flow_details.port.iana_name
            log_fields["__vrni_flow_protocol"] = flow_details.protocol
            log_fields["__vrni_flow_timestamp"] = flow_timestamp

            # vRLI takes milliseconds as the ts
            flow_timestamp_ms = flow_timestamp * 1000
            try:
                send_vrli_message(syslog_msg, flow_timestamp_ms, log_fields, args)
            except:
                print("Failure sending to vRLI")

        # break from the loop if this was the last results page
        if not api_response.cursor:
            break
        # otherwise save the cursor of the next page and move on
        search_payload.cursor = api_response.cursor


def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument('--vrli_server', action='store', help='IP address or hostname of vRealize Log Insight', required=True)
    parser.add_argument('--vrli_port', action='store', help='CFAPI Port of vRealize Log Insight (default 9543)', required=False)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main(args)
