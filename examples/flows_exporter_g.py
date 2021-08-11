# Example: Export Flows into CSV
#
# START Description
# Script will fetch Flows matching certain search criteria
# It will take this fetch flows result and bulk fetch to get all flows information
# Along with the flow information it will fetch appropriate VM, Security group information and dump it to
# CSV file
# END Description
#
# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later

import time
import csv
import logging
import re
import socket

import init_api_client
import swagger_client
from sdk_utilities import get_referenced_entity_name
import utilities


def main():

    # Create search API client object
    search_api = swagger_client.SearchApi()
    logger = logging.getLogger("vrni_sdk")
    filter_string = "(source_security_tags.name = 'OPI' or destination_security_tags.name='OPI') " \
                    "and (flow_tag != TAG_INTERNET_TRAFFIC) and" \
                    "(source_security_tags.name != AD ) and (destination_security_tags.name != AD)"
    filter_string = "((flow_tag = TAG_INTERNET_TRAFFIC) and (source_datacenter.name = 'HaaS-1'))"

    # Create request parameters required for search APIs
    public_api_search_request_params = dict(entity_type=swagger_client.EntityType.FLOW,
                                            filter=filter_string,
                                            size=100)
    logger.info("Get all VMs with filter = [{}]".format(filter_string))

    search_payload = swagger_client.SearchRequest(
        **public_api_search_request_params)

    f_csv = open('flows_to_internet.csv', 'w')
    fields = ['source_sec_tag', 'destination_sec_tag', 'src_security_groups', 'dst_security_groups', 'src_vm', 'src_ip',
              'destination_vm', 'dst_ip', 'protocol', 'port']
    writer = csv.DictWriter(f_csv, fieldnames=fields, delimiter=":")
    writer.writeheader()

    destination_ip_port_protocol = []

    while True:
        # Call the search API
        api_response = search_api.search_entities(body=search_payload)
        logger.info("Response attributes: Total Count: {} "
                    "Time: {}".format(api_response.total_count,
                                      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(api_response.end_time))))

        for result in api_response.results:
            entities_api = swagger_client.EntitiesApi()

            flow_details = entities_api.get_flow(id=result.entity_id)
            logger.info("Flow: {}".format(flow_details.name))

            # Ignore same source IPs
            dest_ip_port_protocol = '{}-{}--{}-{}'.format(flow_details.destination_ip.ip_address, flow_details.protocol,
                                                          flow_details.port.start, flow_details.port.end)
            if dest_ip_port_protocol in destination_ip_port_protocol:
                continue
            destination_ip_port_protocol.append(dest_ip_port_protocol)

            # Get Source VM Name
            src_vm_name = None if flow_details.source_vm is None else get_referenced_entity_name(
                referenced_entity=flow_details.source_vm)
            if src_vm_name is None:
                pass
                # Get vm name

            # Get Destination VM Name
            dst_vm_name = None if flow_details.destination_vm is None else get_referenced_entity_name(
                referenced_entity=flow_details.destination_vm)
            if dst_vm_name is None:
                pass
                # Get VM Name

            # Get Source security groups
            src_group_names = []
            for src_sec_group in flow_details.source_security_groups:
                name = get_referenced_entity_name(
                    referenced_entity=src_sec_group)
                if name:
                    src_group_names.append(name)

            dst_group_names = []
            for dst_sec_group in flow_details.destination_security_groups:
                name = get_referenced_entity_name(
                    referenced_entity=dst_sec_group)
                if name:
                    dst_group_names.append(name)

            # Get Source security tag
            src_security_tag_names = []
            for src_sec_tag in flow_details.source_security_tags:
                name = get_referenced_entity_name(
                    referenced_entity=src_sec_tag)
                if name:
                    src_security_tag_names.append(name)

            dst_security_tag_names = []
            for dst_sec_tag in flow_details.destination_security_groups:
                name = get_referenced_entity_name(
                    referenced_entity=dst_sec_tag)
                if name:
                    dst_security_tag_names.append(name)

            # Write it to csv file
            flow_fields = dict(src_ip=flow_details.source_ip.ip_address,
                               dst_ip=flow_details.destination_ip.ip_address,
                               port=flow_details.port.iana_port_display,
                               protocol=flow_details.protocol,
                               src_vm=src_vm_name,
                               destination_vm=dst_vm_name,
                               source_sec_tag=",".join(src_security_tag_names),
                               destination_sec_tag=",".join(
                                   dst_security_tag_names),
                               src_security_groups=",".join(src_group_names),
                               dst_security_groups=",".join(dst_group_names))
            writer.writerow(flow_fields)

        if not api_response.cursor:
            break
        search_payload.cursor = api_response.cursor
    f_csv.close()


def parse_arguments():
    parser = init_api_client.parse_arguments()
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main()
