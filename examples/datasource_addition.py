# swagger Examples - Adding datasources in bulk
#
# This script uses an input CSV (example: data_sources.csv)
# To add multiple vRealize Network Insight Data Sources. Modify data_sources.csv to contain your own data sources
# (vCenters, NSX, switches, firewalls)
# and run this script with the param --data_sources_csv to your CSV.

# Note: -
# DataSourceType in data_sources.csv is taken from swagger_client.models.data_source_type.py
# For reference here are the data source types that can be used in CSV
# CiscoSwitchDataSource, DellSwitchDataSource, AristaSwitchDataSource, BrocadeSwitchDataSource, JuniperSwitchDataSource,
# GDDataSource, VCenterDataSource, NSXVManagerDataSource, UCSManagerDataSource, HPVCManagerDataSource, 
# HPOneViewDataSource, PanFirewallDataSource, CheckpointFirewallDataSource, NSXTManagerDataSource, KubernetesDataSource,
# InfobloxManagerDataSource

# Cisco Switch type can be taken from from swagger_client.models.cisco_switch_type.py -
# CATALYST_3000, CATALYST_4500, CATALYST_6500, NEXUS_5K, NEXUS_7K, NEXUS_9K

import swagger_client
import init_api_client
import csv
from swagger_client.rest import ApiException
import swagger_client.models.data_source_type as data_source_type
import json


def get_api_function_name(datasource_type):
    datasource = {data_source_type.DataSourceType.CISCOSWITCHDATASOURCE: {"snmp_config": "update_cisco_switch_snmp_config",
                                                                          "add": "add_cisco_switch"},
                  data_source_type.DataSourceType.DELLSWITCHDATASOURCE: {"snmp_config": "update_dell_switch_snmp_config",
                                                                          "add": "add_dell_switch"},
                  data_source_type.DataSourceType.ARISTASWITCHDATASOURCE: {"snmp_config": "list_vcenters",
                                                                          "add": "update_arista_switch_snmp_config"},
                  data_source_type.DataSourceType.BROCADESWITCHDATASOURCE: {"snmp_config": "update_brocade_switch_snmp_config",
                                                                          "add": "add_brocade_switch"},
                  data_source_type.DataSourceType.JUNIPERSWITCHDATASOURCE: {"snmp_config": "update_juniper_switch_snmp_config",
                                                                          "add": "add_juniper_switch"},
                  data_source_type.DataSourceType.VCENTERDATASOURCE: {"add": "add_vcenter_datasource"},
                  data_source_type.DataSourceType.NSXVMANAGERDATASOURCE: {"add": "add_nsxv_manager_datasource"},
                  data_source_type.DataSourceType.UCSMANAGERDATASOURCE: {"snmp_config": "update_ucs_snmp_config",
                                                                          "add": "add_ucs_manager"},
                  data_source_type.DataSourceType.HPVCMANAGERDATASOURCE: {"add": "add_hpvc_manager"},
                  data_source_type.DataSourceType.HPONEVIEWDATASOURCE: {"add": "add_hpov_manager"},
                  data_source_type.DataSourceType.PANFIREWALLDATASOURCE: {"add": "add_panorama_firewall"},
                  data_source_type.DataSourceType.CHECKPOINTFIREWALLDATASOURCE: {"add": "add_panorama_firewall"},
                  data_source_type.DataSourceType.NSXTMANAGERDATASOURCE: {"add": "add_nsxt_manager_datasource"},
                  data_source_type.DataSourceType.KUBERNETESDATASOURCE: {"add": "add_kubernetes_datasource"},
                  data_source_type.DataSourceType.POLICYMANAGERDATASOURCE: {"add": "add_policy_manager_datasource"}}

    return datasource[datasource_type]

def get_add_request_body(datasource, proxy_id=None, vcenter_id=None):
    api_request_body = {
        "ip": "{}".format(datasource['IP']),
        "fqdn": "",
        "proxy_id": "{}".format(proxy_id),
        "enabled": True,
        "nickname": datasource["NickName"],
        "notes": "added by public api",
    }
    if datasource['Username']:
        api_request_body["credentials"] = {"username": "{}".format(datasource['Username']),
                               "password": "{}".format(datasource['Password'])}
    if datasource['CSPRefreshToken']:
        api_request_body["csp_refresh_token"] = datasource['CSPRefreshToken']
    if datasource['CentralCliEnabled']:
        api_request_body["central_cli_enabled"] = datasource['CentralCliEnabled']
    if datasource['IPFixEnabled']:
        api_request_body["ipfix_enabled"] = datasource['IPFixEnabled']
    if vcenter_id:
        api_request_body['vcenter_id'] = vcenter_id
    if datasource['SwitchType']:
        api_request_body["switch_type"] = datasource['SwitchType']
    if datasource['IsVMC']:
        api_request_body["is_vmc"] = datasource['IsVMC']
    print("Request body : <{}>".format(api_request_body))
    return api_request_body

def get_snmp_request_body(datasource, proxy_id=None, vcenter_id=None):
    api_request_body = {
            "snmp_enabled": True,
            "snmp_version": "{}".format(datasource['snmp_version']),
            "config_snmp_3": {
            "username": "{}".format(datasource['snmp_username']),
            "authentication_password": "{}".format(datasource['snmp_password']),
            "context_name": "",
            "authentication_type": "{}".format(datasource['snmp_auth_type']),
            "privacy_type": "{}".format(datasource['snmp_privacy_type'])
          }
        }
    print("Request body : <{}>".format(api_request_body))
    return api_request_body

def get_node_entity_id(api_client, proxy_ip=None):
    infrastructure_api = swagger_client.InfrastructureApi(api_client=api_client)
    node_list = infrastructure_api.list_nodes()
    for entity in node_list.results:
        node = infrastructure_api.get_node(id=entity.id)
        if proxy_ip == node.ip_address:
            return node.id
    return None


def get_vcenter_manager_entity_id(data_source_api, vcenter_ip=None):
    if not vcenter_ip: return None
    data_source_list = data_source_api.list_vcenters()
    for entity in data_source_list.results:
        ds = data_source_api.get_vcenter(id=entity.entity_id)
        if ds.ip == vcenter_ip:
            return entity.entity_id
    return None

def main(api_client, args):

    # Create data source API client object
    data_source_api = swagger_client.DataSourcesApi(api_client=api_client)
    with open("{}".format(args.data_sources_csv), 'rb') as csvFile:
        data_sources = csv.DictReader(csvFile)
        for data_source in data_sources:
            data_source_type = data_source['DataSourceType']
            # Get the Proxy ID from Proxy IP
            proxy_id = get_node_entity_id(api_client, data_source['ProxyIP'])
            if not proxy_id:
                print("Incorrect Proxy IP {}".format(data_source['ProxyIP']))
                continue
            # Get vCenter ID for vCenter manager required for adding NSX
            vcenter_id = get_vcenter_manager_entity_id(data_source_api, data_source['ParentvCenter'])
            print("Adding: <{}> <{}>".format(data_source_type, data_source['IP']))
            # Get the Data source add api fn
            data_source_api_name = get_api_function_name(data_source_type)
            add_data_source_api_fn = getattr(data_source_api, data_source_api_name['add'])
            try:
                response = add_data_source_api_fn(body=get_add_request_body(data_source, proxy_id, vcenter_id))
                print("Successfully added: {} {} : Response : {}".format(data_source_type, data_source['IP'], response))
                if data_source['snmp_version']:
                    add_snmp_api_fn = getattr(data_source_api, data_source_api_name['snmp_config'])
                    response = add_snmp_api_fn(id=response.entity_id, body=get_snmp_request_body(data_source, proxy_id, vcenter_id))
                    print("Successfully added: {} {} snmp : Response : {}".format(data_source_type, data_source['IP'], response))
            except ApiException as e:
                print("Failed adding data source: {} : Error : {} ".format(data_source['IP'], json.loads(e.body)))

if __name__ == '__main__':
    args = init_api_client.parse_arguments()
    api_client = init_api_client.get_api_client(args)
    main(api_client, args)
