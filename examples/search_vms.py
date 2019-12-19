# Python SDK Examples
#
# Script will fetch VMs through a call to search API. Search API returns uuids for all VMs.
# Script will then fetch every single VM's complete information.
#
# Copyright 2019 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later

import time

import init_api_client
import swagger_client
import logging
import utilities
logger = logging.getLogger("vrni_sdk")


def main():

    # Create search API client object
    search_api = swagger_client.SearchApi()

    # TODO: Add/Change filter to get valid results
    filter_string = "vcenter_manager.name = '10.197.17.43'"
    # Create request parameters required for search APIs
    public_api_search_request_params = dict(entity_type=swagger_client.EntityType.VIRTUALMACHINE,
                                            filter=filter_string,
                                            size=100)
    logger.info("Get all VMs with filter = [{}]".format(filter_string))

    # Create payload from search parameters required for calling the search API
    search_payload = swagger_client.SearchRequest(**public_api_search_request_params)

    while True:
        # Call the search API
        api_response = search_api.search_entities(body=search_payload)
        logger.info("Response attributes: Total Count: {} Cursor : {} "
              "Time: {}".format(api_response.total_count, api_response.cursor,
                                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(api_response.end_time))))
        for result in api_response.results:
            entities_api = swagger_client.EntitiesApi(api_client=api_client)
            logger.info("VM Name: {}".format(entities_api.get_vm(id=result.entity_id).name))
            time.sleep(0.025) # make sure we don't hit the vRNI throttle and start getting 429 errors
        if not api_response.cursor:
            break
        search_payload.cursor = api_response.cursor

def parse_arguments():
    parser = init_api_client.parse_arguments()
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main()
