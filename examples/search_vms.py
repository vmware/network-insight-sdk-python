# Python SDK Examples

# Script will fetch VMs through a call to search API. Search API returns uuids for all VMs.
# Script will then fetch every single VM's complete information.

import time

import init_api_client
import swagger_client


def main():
    # Get API Client
    api_client = init_api_client.get_api_client()

    # Create search API client object
    search_api = swagger_client.SearchApi(api_client=api_client)

    # TODO: Add/Change filter to get valid results
    filter_string = "vcenter_manager.name = '10.197.17.51'"
    # Create request parameters required for search APIs
    public_api_search_request_params = dict(entity_type=swagger_client.EntityType.VIRTUALMACHINE,
                                            filter=filter_string,
                                            size=100)
    print("Get all VMs with filter = [{}]".format(filter_string))

    # Create payload from search parameters required for calling the search API
    search_payload = swagger_client.SearchRequest(**public_api_search_request_params)

    while True:
        # Call the search API
        api_response = search_api.search_entities(body=search_payload)
        print("Response attributes: Total Count: {} "
              "Time: {}".format(api_response.total_count,
                                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(api_response.end_time))))
        for result in api_response.results:
            entities_api = swagger_client.EntitiesApi(api_client=api_client)
            print("VM Name: {}".format(entities_api.get_vm(id=result.entity_id).name))
            # print result
        if not api_response.cursor:
            break
        search_payload.cursor = api_response.cursor


if __name__ == '__main__':
    main()
