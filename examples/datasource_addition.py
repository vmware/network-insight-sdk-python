# swagger Examples - Adding datasources in bulk
#
# This script uses an input CSV (example: data_sources.csv)
# To add multiple vRealize Network Insight Data Sources. Modify data_sources.csv to contain your own data sources (vCenters, NSX, switches, firewalls)
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
    datasource = {data_source_type.DataSourceType.CISCOSWITCHDATASOURCE: "add_cisco_switch",
                  data_source_type.DataSourceType.DELLSWITCHDATASOURCE: "add_dell_switch",
                  data_source_type.DataSourceType.ARISTASWITCHDATASOURCE: "add_arista_switch",
                  data_source_type.DataSourceType.BROCADESWITCHDATASOURCE: "add_brocade_switch",
                  data_source_type.DataSourceType.JUNIPERSWITCHDATASOURCE: "add_juniper_switch",
                  data_source_type.DataSourceType.VCENTERDATASOURCE: "add_vcenter_datasource",
                  data_source_type.DataSourceType.NSXVMANAGERDATASOURCE: "add_nsxv_manager_datasource",
                  data_source_type.DataSourceType.UCSMANAGERDATASOURCE: "add_ucs_manager",
                  data_source_type.DataSourceType.HPVCMANAGERDATASOURCE: "add_hpvc_manager",
                  data_source_type.DataSourceType.HPONEVIEWDATASOURCE: "add_hpov_manager",
                  data_source_type.DataSourceType.PANFIREWALLDATASOURCE: "add_panorama_firewall",
                  data_source_type.DataSourceType.CHECKPOINTFIREWALLDATASOURCE: "add_checkpoint_firewall",
                  data_source_type.DataSourceType.NSXTMANAGERDATASOURCE: "add_nsxt_manager_datasource",
                  data_source_type.DataSourceType.INFOBLOXMANAGERDATASOURCE: "add_infoblox_manager_datasource"}

    return datasource[datasource_type]


def get_add_request_body(datasource, proxy_id=None, vcenter_id=None):
    body = {
        "ip": "%s" % datasource['IP'],
        "fqdn": "",
        "proxy_id": "%s" % proxy_id,
        "enabled": True,
        "nickname": datasource["NickName"],
        "notes": "added by public api",
        "credentials": {"username": "%s" % datasource['Username'],
                        "password": "%s" % datasource['Password']},
    }
    if datasource['CentralCliEnabled']:
        body["central_cli_enabled"] = datasource['CentralCliEnabled']
    if datasource['IPFixEnabled']:
        body["ipfix_enabled"] = datasource['IPFixEnabled']
    if vcenter_id:
        body['vcenter_id'] = vcenter_id
    if datasource['SwitchType']:
        body["switch_type"] = datasource['SwitchType']
    if datasource['IsVMC']:
        body["is_vmc"] = datasource['IsVMC']

    return body


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
    with open("%s" % args.data_sources_csv, 'rb') as csvFile:
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
            add_data_source_api_fn = getattr(data_source_api, data_source_api_name)
            try:
                response = add_data_source_api_fn(body=get_add_request_body(data_source, proxy_id, vcenter_id))
                print("Successfully added: {} {} : Response : {}".format(data_source_type, data_source['IP'], response))
            except ApiException as e:
                print("Failed adding data source: %s : Error : %s " % (data_source['IP'], json.loads(e.body)))

if __name__ == '__main__':
    args = init_api_client.parse_arguments()
    api_client = init_api_client.get_api_client(args)
    main(api_client, args)
