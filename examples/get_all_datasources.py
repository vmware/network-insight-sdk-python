# Example: Getting added datasources in bulk
#
# START Description
# This script write the added datasource in an input CSV (example: list_data_sources.csv)
# To list added vRealize Network Insight Data Sources, run this script with the param --data_sources_csv with new csv file name.
# END Description
#
# Note: -
# DataSourceType in DATASOURCES_LIST is taken from swagger_client.models.data_source_type.py
# For reference here are the data source types that can be used in CSV
# CiscoSwitchDataSource, DellSwitchDataSource, AristaSwitchDataSource, BrocadeSwitchDataSource, JuniperSwitchDataSource,
# GDDataSource, VCenterDataSource, NSXVManagerDataSource, UCSManagerDataSource, HPVCManagerDataSource, PolicyManagerDataSource,
# HPOneViewDataSource, PanFirewallDataSource, CheckpointFirewallDataSource, NSXTManagerDataSource, KubernetesDataSource,
# InfobloxManagerDataSource
#
# Cisco Switch type can be taken from from swagger_client.models.cisco_switch_type.py -
# CATALYST_3000, CATALYST_4500, CATALYST_6500, NEXUS_5K, NEXUS_7K, NEXUS_9K
#
# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later

import swagger_client
import init_api_client
import logging
import time

import csv
from swagger_client.rest import ApiException
import swagger_client.models.data_source_type as data_source_type
import json
logger = logging.getLogger("vrni_sdk")


DATASOURCES_LIST = ["VCenterDataSource", "CiscoSwitchDataSource", "NSXVManagerDataSource", "NSXTManagerDataSource",
                    "PolicyManagerDataSource", "PanFirewallDataSource"]

SNMP_CONFIG_LIST = ["CiscoSwitchDataSource", "DellSwitchDataSource", "AristaSwitchDataSource", "BrocadeSwitchDataSource",
                    "JuniperSwitchDataSource", "UCSManagerDataSource"]


def get_api_function_name(datasource_type):
    datasource = {data_source_type.DataSourceType.CISCOSWITCHDATASOURCE: {"list": "list_cisco_switches",
                                                                          "get": "get_cisco_switch",
                                                                          "snmp_config": "get_cisco_switch_snmp_config"},
                  data_source_type.DataSourceType.DELLSWITCHDATASOURCE: {"list": "list_dell_switches",
                                                                         "get": "get_dell_switch",
                                                                         "snmp_config": "get_dell_switch_snmp_config"},
                  data_source_type.DataSourceType.ARISTASWITCHDATASOURCE: {"list": "list_arista_switches",
                                                                           "get": "get_arista_switch",
                                                                           "snmp_config": "get_arista_switch_snmp_config"},
                  data_source_type.DataSourceType.BROCADESWITCHDATASOURCE: {"list": "list_brocade_switches",
                                                                            "get": "get_brocade_switch"},
                  "snmp_config": "get_brocade_switch_snmp_config",
                  data_source_type.DataSourceType.JUNIPERSWITCHDATASOURCE: {"list": "list_juniper_switches",
                                                                            "get": "get_juniper_switch",
                                                                            "snmp_config": "get_juniper_switch_snmp_config"},
                  data_source_type.DataSourceType.VCENTERDATASOURCE: {"list": "list_vcenters",
                                                                      "get": "get_vcenter"},
                  data_source_type.DataSourceType.NSXVMANAGERDATASOURCE: {"list": "list_nsxv_managers",
                                                                          "get": "get_nsxv_manager"},
                  data_source_type.DataSourceType.UCSMANAGERDATASOURCE: {"list": "list_ucs_managers",
                                                                         "get": "get_ucs_manager",
                                                                         "snmp_config": "get_ucs_snmp_config"},
                  data_source_type.DataSourceType.HPVCMANAGERDATASOURCE: {"list": "list_hpvc_managers",
                                                                          "get": "get_hpvc_manager"},
                  data_source_type.DataSourceType.HPONEVIEWDATASOURCE: {"list": "list_hpov_managers",
                                                                        "get": "get_hpov_manager"},
                  data_source_type.DataSourceType.PANFIREWALLDATASOURCE: {"list": "list_panorama_firewalls",
                                                                          "get": "get_panorama_firewall"},
                  data_source_type.DataSourceType.CHECKPOINTFIREWALLDATASOURCE: {"list": "list_checkpoint_firewalls",
                                                                                 "get": "get_checkpoint_firewall"},
                  data_source_type.DataSourceType.NSXTMANAGERDATASOURCE: {"list": "list_nsxt_managers",
                                                                          "get": "get_nsxt_manager"},
                  data_source_type.DataSourceType.INFOBLOXMANAGERDATASOURCE: {"list": "list_infoblox_managers",
                                                                              "get": "get_infoblox_manager"},
                  data_source_type.DataSourceType.POLICYMANAGERDATASOURCE: {"list": "list_policy_managers",
                                                                            "get": "get_policy_manager"},
                  data_source_type.DataSourceType.KUBERNETESDATASOURCE: {"list": "list_kubernetes_clusters",
                                                                         "get": "get_kubernetes_cluster"}}

    return datasource[datasource_type]


def get_data(api_client, datasource_api, datasource):
    data = {}
    if hasattr(datasource, "vcenter_id"):
        vcenter_ip = datasource_api.get_vcenter(id=datasource.vcenter_id).ip
        data["ParentvCenter"] = "{}".format(vcenter_ip)
    data["DataSourceType"] = "{}".format(datasource.entity_type)
    data["ProxyIP"] = "{}".format(
        get_proxy_ip(api_client, datasource.proxy_id))
    if datasource.ip:
        data["IP"] = "{}".format(datasource.ip)
    if datasource.fqdn:
        data["fqdn"] = "{}".format(datasource.fqdn)
    if hasattr(datasource, "credentials"):
        data["Username"] = "{}".format(datasource.credentials.username)
    data["NickName"] = "{}".format(datasource.nickname)
    if hasattr(datasource, "switch_type"):
        data["SwitchType"] = "{}".format(datasource.switch_type)
    if hasattr(datasource, "ipfix_enabled"):
        data["IPFixEnabled"] = "{}".format(datasource.ipfix_enabled)
    if hasattr(datasource, "central_cli_enabled"):
        data["CentralCliEnabled"] = "{}".format(datasource.central_cli_enabled)
    return data


def get_proxy_ip(api_client, entity_id):
    infrastructure_api = swagger_client.InfrastructureApi(
        api_client=api_client)
    node = infrastructure_api.get_node(id=entity_id)
    return node.ip_address


def main(api_client, args):

    # Create data source API client object
    datasource_api = swagger_client.DataSourcesApi(api_client=api_client)
    with open("{}".format(args.data_sources_csv), 'w') as csvFile:
        fields = ["DataSourceType", "IP", "fqdn", "Username", "Password", "CSPRefreshToken", "NickName", "CentralCliEnabled",
                  "IPFixEnabled", "SwitchType", "ParentvCenter", "IsVMC", "snmp_version", "snmp_community_string", "ProxyIP"]
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        data = []
        for data_source_type in DATASOURCES_LIST:
            data_source_api_name = get_api_function_name(data_source_type)
            # Get lis function for datasource
            list_datasource_api_fn = getattr(
                datasource_api, data_source_api_name["list"])
            get_datasource_fn = getattr(
                datasource_api, data_source_api_name["get"])
            # make sure we don't hit the vRNI throttle and start getting 429 errors
            time.sleep(0.025)
            try:
                data_source_list = list_datasource_api_fn()
                logger.info("Successfully got list of: {} : Response : {}".format(
                    data_source_type, data_source_list))
                for data_source in data_source_list.results:
                    datasource = get_datasource_fn(id=data_source.entity_id)
                    logger.info("Successfully got {} : Response : {}".format(
                        data_source_type, datasource))
                    data_dict = get_data(
                        api_client, datasource_api, datasource)
                    if data_source_type in SNMP_CONFIG_LIST:
                        get_snmp_api_fn = getattr(
                            datasource_api, data_source_api_name['snmp_config'])
                        response = get_snmp_api_fn(id=datasource.entity_id)
                        # make sure we don't hit the vRNI throttle and start getting 429 errors
                        time.sleep(0.025)
                        if response.snmp_version == 'v2c':
                            data_dict['snmp_version'] = response.snmp_version
                            logger.info("Successfully got: {} {} snmp : Response : {}".format(data_source_type, datasource.ip,
                                                                                              response))
                    data.append(data_dict)
            except ApiException as e:
                print("Failed getting list of data source type: {} : Error : {} ".format(
                    data_source_type, json.loads(e.body)))
        writer.writerows(data)


def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument("--data_sources_csv", action="store",
                        default='data_sources.csv', help="csv file with your own data sources")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    api_client = init_api_client.get_api_client(args)
    main(api_client, args)
