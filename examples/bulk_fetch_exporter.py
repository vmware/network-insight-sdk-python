# Python SDK Examples

# Script will fetch Flows matching certain search criteria
# It will take this fetch flows result and bulk fetch to get all flows information
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
from swagger_client.rest import ApiException
import utilities

logger = logging.getLogger("vrni_sdk")
id_to_name_map = dict()


def get_referenced_entity_name(entity_id=None, entity_type=None, entities_api=None):
    logger.info("Fetching id = {} of type = {}".format(entity_id, entity_type))
    if entity_id in id_to_name_map:
        return id_to_name_map[entity_id]

    if entity_type == swagger_client.AllEntityType.VIRTUALMACHINE:
        entity_fn = entities_api.get_vm
    elif entity_type == swagger_client.AllEntityType.NSXSECURITYGROUP:
        entity_fn = entities_api.get_security_group
    else:
        raise ValueError("API not assigned to type {}".format(entity_type))

    entity_name = None
    try:
        entity_name = entity_fn(id=entity_id).name
    except ApiException as e:
        # This means referenced entity might be deleted
        logger.exception(e)
    id_to_name_map[entity_id] = entity_name
    return entity_name


def main():

    # Create search API client object
    search_api = swagger_client.SearchApi()

    # TODO: Add/Change filter to get valid results
    filter_string = "((source_datacenter.name = 'washington-dc-delta-1'))"

    # Create request parameters required for search APIs
    public_api_search_request_params = dict(entity_type=swagger_client.EntityType.FLOW,
                                            size=3)
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
        logger.info("Result list : {} ".format(api_response.results))

        # payload for bulk fetch
        payload ={"entity_ids" : api_response.results}
        entities_api = swagger_client.EntitiesApi(api_client=api_client)
        # bulk fetching the entities
        api_response = entities_api.entities_fetch_post(body=payload)
        time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors

        for result in api_response.results:
            # Get Source VM Name
            src_vm_name = get_referenced_entity_name(entity_id=result.entity.source_vm.entity_id,
                                                     entity_type=result.entity.source_vm.entity_type,
                                                     entities_api=entities_api)
            time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors
            # Get Source security groups
            sec_group_names = []
            for src_sec_group in result.entity.source_security_groups:
                name = get_referenced_entity_name(entity_id=src_sec_group.entity_id,
                                                  entity_type=src_sec_group.entity_type,
                                                  entities_api=entities_api)
                if name: sec_group_names.append(name)
                time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors
            # Write it to csv file
            flow_fields = dict(src_ip=result.entity.source_ip.ip_address,
                               dst_ip=result.entity.destination_ip.ip_address,
                               port=result.entity.port.iana_port_display,
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
