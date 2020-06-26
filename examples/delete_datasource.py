# swagger Examples - update datasources in bulk
#
# This script uses an input CSV (example: update_data_sources.csv)
# To update multiple vRealize Network Insight Data Sources. Modify update_data_sources.csv to contain your own data sources
# (vCenters, NSX, switches, firewalls)
# and run this script with the param --data_sources_csv to your CSV.

# Note: -
# DataSourceType in update_data_sources.csv is taken from swagger_client.models.data_source_type.py
# For reference here are the data source types that can be used in CSV
# CiscoSwitchDataSource, DellSwitchDataSource, AristaSwitchDataSource, BrocadeSwitchDataSource, JuniperSwitchDataSource,
# GDDataSource, VCenterDataSource, NSXVManagerDataSource, UCSManagerDataSource, HPVCManagerDataSource,
# HPOneViewDataSource, PanFirewallDataSource, CheckpointFirewallDataSource, NSXTManagerDataSource, KubernetesDataSource,
# InfobloxManagerDataSource

# Cisco Switch type can be taken from from swagger_client.models.cisco_switch_type.py -
# CATALYST_3000, CATALYST_4500, CATALYST_6500, NEXUS_5K, NEXUS_7K, NEXUS_9K
#
# Copyright 2019 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later

import csv
import json
import logging

import swagger_client

from swagger_client.rest import ApiException
import helper.get_datasource_details as get_datasource_details

import init_api_client
import utilities

logger = logging.getLogger("vrni_sdk")
ERROR = 1
SUCCESS = 0

def get_data_source_entity_id(get_datasource_fn, data_source_list, data_source):
    for entity in data_source_list.results:
        ds = get_datasource_fn(id=entity.entity_id)
        if ds.ip == data_source['IP'] or ds.fqdn == data_source['fqdn']:
            return entity.entity_id
    return None

def main(api_client, args):

    # Create data source API client object
    data_source_api = swagger_client.DataSourcesApi(api_client=api_client)
    with open("{}".format(args.data_sources_csv), 'rb') as csvFile:
        data_sources = csv.DictReader(csvFile)
        for data_source in data_sources:
            data_source_type = data_source['DataSourceType']

            logger.info("Deleting: <{}> <{}>".format(data_source_type, data_source['IP']))
            # Get the Data source add api fn
            data_source_api_name = get_datasource_details.get_api_function_name(data_source_type)
            get_datasource_fn = getattr(data_source_api, data_source_api_name["get"])
            delete_datasource_fn = getattr(data_source_api, data_source_api_name["delete"])
            try:
                list_datasource_api_fn = getattr(data_source_api, data_source_api_name["list"])
                data_source_list = list_datasource_api_fn()
                logger.info("Successfully got list of: {} : Response : {}".format(data_source_type, data_source_list))
                entity_id = get_data_source_entity_id(get_datasource_fn, data_source_list, data_source)
                if not entity_id:
                    print("Failed getting data source type : {}: {}".format(data_source_type, data_source['IP']))
                    return
                delete_datasource_fn(id=entity_id)
                logger.info("Successfully deleted: {} : {}".format(data_source_type, entity_id))
            except ApiException as e:
                print("Failed deleting data source type: {} : Error : {} ".format(data_source_type, json.loads(e.body)))
                return_code = ERROR

    auth_api = swagger_client.AuthenticationApi(api_client=api_client)
    auth_api.delete()
    return return_code

def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument("--data_sources_csv", action="store",
                        default='delete_data_sources.csv', help="csv file with your own data sources")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main(api_client, args)
