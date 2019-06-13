# Python SDK Examples
# Script will get total bytes transferred for a specific IP or group of IPs
# or the scope can be any l2 network, security group, etc.
#
# Copyright 2019 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later

import init_api_client
import swagger_client
import utilities
import logging

logger = logging.getLogger("vrni_sdk")


def main():
    search_api = swagger_client.SearchApi(api_client=api_client)

    # TODO: Add/Change filter to get valid results. Examples are shown below
    # filter_string = "destination_ip.ip_address = '192.168.21.20'"
    # filter_string = "port = 123"
    # filter_string = "source_cluster.name = 'HaaS-Cluster-6'"
    filter_string = "destination_l2_network.name = 'vlan-1014'"

    aggregation = swagger_client.Aggregation(field="flow.totalBytes.delta.summation.bytes",
                                             aggregation_type="SUM")

    logger.info("Getting total bytes for {} in last 15 days".format(filter_string))
    # Time range is last 15 days
    time_range = swagger_client.TimeRange(start_time=utilities.get_start_time(15), end_time=utilities.get_end_time())

    aggregation_request = swagger_client.AggregationRequest(entity_type=swagger_client.EntityType.FLOW,
                                                            aggregations=[aggregation], time_range=time_range,
                                                            filter=filter_string)

    api_response = search_api.aggregate_search_results(body=aggregation_request)
    # Value of sum bytes
    logger.info(api_response.aggregations[0].value)

def parse_arguments():
    parser = init_api_client.parse_arguments()
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main()
