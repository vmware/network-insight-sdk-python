# Python SDK Examples
# Script will get total bytes transferred for a specific IP or group of IPs
# or the scope can be any l2 network, security group, etc.

import init_api_client
import swagger_client
import utilities


def main(api_client):
    search_api = swagger_client.SearchApi(api_client=api_client)

    # TODO: Add/Change filter to get valid results. Examples are shown below
    # filter_string = "destination_ip.ip_address = '192.168.21.20'"
    # filter_string = "port = 123"
    # filter_string = "source_cluster.name = 'HaaS-Cluster-6'"
    filter_string = "destination_l2_network.name = 'vlan-1014'"

    aggregation = swagger_client.Aggregation(field="flow.totalBytes.delta.summation.bytes",
                                             aggregation_type="SUM")

    # Time range is last 15 days
    time_range = swagger_client.TimeRange(start_time=utilities.get_start_time(15), end_time=utilities.get_end_time())

    aggregation_request = swagger_client.AggregationRequest(entity_type=swagger_client.EntityType.FLOW,
                                                            aggregations=[aggregation], time_range=time_range,
                                                            filter=filter_string)

    api_response = search_api.aggregate_search_results(body=aggregation_request)
    # Value of sum bytes
    print(api_response.aggregations[0].value)


if __name__ == '__main__':
    args = init_api_client.parse_arguments()
    api_client = init_api_client.get_api_client(args)
    main(api_client)
