# swagger Examples - update datasources in bulk
#
# This script uses an input CSV (example: update_data_sources.csv)
# To update multiple vRealize Network Insight Data Sources. Modify data_sources.csv to contain your own data sources
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
import swagger_client.models.data_source_type as data_source_type

import init_api_client
import utilities

logger = logging.getLogger("vrni_sdk")


def get_api_function_name(datasource_type):
    datasource = {
        data_source_type.DataSourceType.CISCOSWITCHDATASOURCE: {"update_snmp_config": "update_cisco_switch_snmp_config",
                                                                "get_snmp_config": "get_cisco_switch_snmp_config",
                                                                "update": "update_cisco_switch",
                                                                "get": "get_cisco_switch",
                                                                "list": "list_cisco_switches"},
        data_source_type.DataSourceType.DELLSWITCHDATASOURCE: {"update_snmp_config": "update_dell_switch_snmp_config",
                                                               "get_snmp_config": "get_dell_switch_snmp_config",
                                                               "update": "update_dell_switch",
                                                               "get": "get_dell_switch",
                                                               "list": "list_dell_switches"},
        data_source_type.DataSourceType.ARISTASWITCHDATASOURCE: {"update_snmp_config": "update_arista_switch_snmp_config",
                                                                 "get_snmp_config": "get_arista_switch_snmp_config",
                                                                 "update": "update_arista_switch",
                                                                 "get": "get_arista_switch",
                                                                 "list": "list_arista_switches"},
        data_source_type.DataSourceType.BROCADESWITCHDATASOURCE: {"update_snmp_config": "update_brocade_switch_snmp_config",
                                                                  "get_snmp_config": "get_brocade_switch_snmp_config",
                                                                  "update": "update_brocade_switch",
                                                                  "get": "get_brocade_switch",
                                                                  "list": "list_brocade_switches"},
        data_source_type.DataSourceType.JUNIPERSWITCHDATASOURCE: {"update_snmp_config": "update_juniper_switch_snmp_config",
                                                                  "get_snmp_config": "get_juniper_switch_snmp_config",
                                                                  "update": "update_juniper_switch",
                                                                  "get": "get_juniper_switch",
                                                                  "list": "list_juniper_switches"},
        data_source_type.DataSourceType.VCENTERDATASOURCE: {"update": "update_vcenter",
                                                            "get": "get_vcenter",
                                                            "list": "list_vcenters"},
        data_source_type.DataSourceType.NSXVMANAGERDATASOURCE: {"update": "update_nsxv_manager",
                                                                "get": "get_nsxv_manager",
                                                                "list": "list_nsxv_managers"},
        data_source_type.DataSourceType.UCSMANAGERDATASOURCE: {"update_snmp_config": "update_ucs_snmp_config",
                                                               "get_snmp_config": "get_ucs_snmp_config",
                                                               "update": "update_ucs_manager",
                                                               "get": "get_ucs_manager",
                                                               "list": "list_ucs_managers"},
        data_source_type.DataSourceType.HPVCMANAGERDATASOURCE: {"update": "update_hpvc_manager",
                                                                "get": "get_hpvc_manager",
                                                                "list": "list_hpvc_managers"},
        data_source_type.DataSourceType.HPONEVIEWDATASOURCE: {"update": "update_hpov_manager",
                                                              "get": "get_hpov_manager",
                                                              "list": "list_hpov_managers"},
        data_source_type.DataSourceType.PANFIREWALLDATASOURCE: {"update": "update_panorama_firewall",
                                                                "get": "get_panorama_firewall",
                                                                "list": "list_panorama_firewalls"},
        data_source_type.DataSourceType.CHECKPOINTFIREWALLDATASOURCE: {"update": "update_checkpoint_firewall",
                                                                       "get": "get_checkpoint_firewall",
                                                                       "list": "list_checkpoint_firewalls"},
        data_source_type.DataSourceType.NSXTMANAGERDATASOURCE: {"update": "update_nsxt_manager_datasource",
                                                                "list": "list_nsxt_managers"},
        data_source_type.DataSourceType.KUBERNETESDATASOURCE: {"update": "update_kubernetes_datasource",
                                                               "get": "get_kubernetes_cluster",
                                                               "list": "list_infoblox_managers"},
        data_source_type.DataSourceType.POLICYMANAGERDATASOURCE: {"update": "update_policy_manager",
                                                                  "get": "get_policy_manager",
                                                                  "list": "list_policy_managers"}}

    return datasource[datasource_type]


def get_update_request_body(response, data_source):
    response.credentials.username = data_source['Username']
    response.credentials.password = data_source['Password']
    return response


def update_snmp_config(entity_id, data_source_api, data_source_api_name, data_source):
    try:
        update_snmp_api_fn = getattr(data_source_api, data_source_api_name['update_snmp_config'])
        get_snmp_api_fn = getattr(data_source_api, data_source_api_name['get_snmp_config'])
        response = get_snmp_api_fn(id=entity_id)

        if data_source['snmp_version'] == 'v2c':
            response.config_snmp_2c.community_string = data_source['snmp_community_string']
        elif data_source['snmp_version'] == 'v3':
            response
        update_snmp_api_fn(id=entity_id, body=response)
    except ApiException as e:
        print("Failed updating of data source type: {} : Error : {} ".format(data_source_type, json.loads(e.body)))
        print "here"

    if data_source['snmp_version'] == 'v2c':
        snmp_config = dict(config_snmp_2c=dict(community_string='{}'.format(data_source['snmp_community_string'])))

    elif data_source['snmp_version'] == 'v3':
        snmp_config = dict(config_snmp_3=dict(
            username="{}".format(datasource['snmp_username']),
            authentication_password="{}".format(datasource['snmp_password']),
            context_name="",
            authentication_type="{}".format(datasource['snmp_auth_type']),
            privacy_type="{}".format(datasource['snmp_privacy_type'])
        ))

    api_request_body.update(snmp_config)

    logger.info("Request body : <{}>".format(api_request_body))
    return api_request_body

def get_data_source_entity_id(data_source_api, get_datasource_fn, data_source_list, data_source):
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

            logger.info("Adding: <{}> <{}>".format(data_source_type, data_source['IP']))
            # Get the Data source add api fn
            data_source_api_name = get_api_function_name(data_source_type)
            get_datasource_fn = getattr(data_source_api, data_source_api_name["get"])
            update_datasource_fn = getattr(data_source_api, data_source_api_name["update"])
            try:
                list_datasource_api_fn = getattr(data_source_api, data_source_api_name["list"])
                data_source_list = list_datasource_api_fn()
                logger.info("Successfully got list of: {} : Response : {}".format(data_source_type, data_source_list))
                entity_id = get_data_source_entity_id(data_source_api, get_datasource_fn, data_source_list, data_source)
                response = get_datasource_fn(id=entity_id)
                update_request_body = get_update_request_body(response, data_source)
                update_datasource_fn(id=entity_id, body=update_request_body)
                logger.info("Successfully updated: {} : Response : {}".format(data_source_type, data_source_list))
                if data_source['snmp_version']:
                    update_snmp_config(entity_id, data_source_api, data_source_api_name, data_source)
            except ApiException as e:
                print("Failed updating of data source type: {} : Error : {} ".format(data_source_type, json.loads(e.body)))


def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument("--data_sources_csv", action="store",
                        default='update_data_sources.csv', help="csv file with your own data sources")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main(api_client, args)
