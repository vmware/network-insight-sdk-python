# Python SDK Examples

# Script will fetch Flows matching certain search criteria
# Along with the flow information it will fetch appropriate VM, Security group information and dump it to
# CSV file
#
# Copyright 2019 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later

import time
import csv
import logging

import init_api_client
import swagger_client
from sdk_utilities import get_referenced_entity_name
import utilities


def main():

    # Create search API client object
    search_api = swagger_client.SearchApi()
    logger = logging.getLogger("vrni_sdk")

    # TODO: Add/Change filter to get valid results
    filter_string = "((flow_tag = TAG_INTERNET_TRAFFIC) and (source_datacenter.name = 'HaaS-1'))"
    # Create request parameters required for search APIs
    public_api_search_request_params = dict(entity_type=swagger_client.EntityType.FLOW,
                                            filter=filter_string,
                                            size=100)
    logger.info("Get all VMs with filter = [{}]".format(filter_string))

    # Create payload from search parameters required for calling the search API
    search_payload = swagger_client.SearchRequest(**public_api_search_request_params)

    f_csv = open('flows_to_internet.csv', 'w')
    fields = ['src_ip', 'dst_ip', 'src_vm', 'src_security_groups', 'port']
    writer = csv.DictWriter(f_csv, fieldnames=fields, delimiter=":")
    writer.writeheader()

    while True:
        # Call the search API
        api_response = search_api.search_entities(body=search_payload)
        logger.info("Response attributes: Total Count: {} "
              "Time: {}".format(api_response.total_count,
                                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(api_response.end_time))))
        for result in api_response.results:
            entities_api = swagger_client.EntitiesApi()

            internet_flow = entities_api.get_flow(id=result.entity_id)
            logger.info("Flow: {}".format(internet_flow.name))
            time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors

            # Get Source VM Name
            src_vm_name = get_referenced_entity_name(referenced_entity=internet_flow.source_vm)
            time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors

            # Get Source security groups
            sec_group_names = []
            for src_sec_group in internet_flow.source_security_groups:
                name = get_referenced_entity_name(referenced_entity=src_sec_group)
                if name: sec_group_names.append(name)

            # Write it to csv file
            flow_fields = dict(src_ip=internet_flow.source_ip.ip_address,
                               dst_ip=internet_flow.destination_ip.ip_address,
                               port=internet_flow.port.iana_port_display,
                               src_vm=src_vm_name,
                               src_security_groups=",".join(sec_group_names))
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
