# swagger Examples - Adding datasources in bulk
#
# This script uses an input CSV (example: data_sources.csv)
# To add multiple vRealize Network Insight Data Sources. Modify data_sources.csv to contain your own data sources (vCenters, NSX, switches, firewalls)
# and run this script with the param --datasourcesCSV to your CSV.
#
# Sandesh Bhagwat (@sbhagwat)
# sbhagwat@vmware.com
# Version 1.0

import swagger_client
import init_api_client
import csv
from swagger_client.rest import ApiException
import logging
import json


def get_datasource_type(datasource_type):
    datasource = {"CISCOSWITCHDATASOURCE" : "CiscoSwitchDataSource",
    "DELLSWITCHDATASOURCE" : "DellSwitchDataSource",
    "ARISTASWITCHDATASOURCE" : "AristaSwitchDataSource",
    "BROCADESWITCHDATASOURCE" : "BrocadeSwitchDataSource",
    "JUNIPERSWITCHDATASOURCE" : "JuniperSwitchDataSource",
    "VCENTERDATASOURCE" : "VCenterDataSource",
    "NSXVMANAGERDATASOURCE" : "NSXVManagerDataSource",
    "UCSMANAGERDATASOURCE" : "UCSManagerDataSource",
    "HPVCMANAGERDATASOURCE" : "HPVCManagerDataSource",
    "HPONEVIEWDATASOURCE" : "HPOneViewDataSource",
    "PANFIREWALLDATASOURCE" : "PanFirewallDataSource",
    "CHECKPOINTFIREWALLDATASOURCE" : "CheckpointFirewallDataSource",
    "NSXTMANAGERDATASOURCE" : "NSXTManagerDataSource",
    "INFOBLOXMANAGERDATASOURCE" : "InfobloxManagerDataSource"}
    return datasource

def get_api_function_name(datasource_type):
    datasource = {"cisco_switch" : "add_cisco_switch",
    "dell_Switch" : "add_dell_switch",
    "arista_switch" : "add_arista_switch",
    "brocade_switch" : "add_brocade_switch",
    "juniper_switch" : "add_juniper_switch",
    "vcenter" : "add_vcenter_datasource",
    "nsxv_manager" : "add_nsxv_manager_datasource",
    "ucs_manager" : "add_ucs_manager",
    "hpvc_manager" : "add_hpvc_manager",
    "hpov_manage" : "add_hpov_manager",
    "panorama_firewall" : "add_panorama_firewall",
    "checkpoint_firewall" : "add_checkpoint_firewall",
    "nsxt_manager" : "add_nsxt_manager_datasource",
    "infoblox_manager" : "add_infoblox_manager_datasource"}

    return datasource[datasource_type]


def get_add_request_body(datasource, proxy_id, vcenter_id):
    body = {
        "ip": "%s" % datasource['IP'],
        "fqdn": "",
        "proxy_id": "%s" % proxy_id,
        "enabled": True,
        "nickname": datasource["NickName"],
        "notes": "added by public api",
        "credentials": {"username": "%s" % datasource['Username'],
                        "password": "%s" % datasource['Password']},
        "is_vmc": False
    }
    if vcenter_id:
        body['vcenter_id'] = vcenter_id
    if datasource['SwitchType']:
        body["switch_type"] = datasource['SwitchType']
    return body

def get_node_entity_id(api_client, proxy_ip):
    infrastructure_api = swagger_client.InfrastructureApi(api_client=api_client)
    node_list = infrastructure_api.list_nodes()
    for entity in node_list.results:
        node = infrastructure_api.get_node(id=entity.id)
        return node.id

def get_vcenter_manager_entity_id(datasource_api, vcenter_ip):
    data_source_list = datasource_api.list_vcenters()
    for entity in data_source_list.results:
        ds = datasource_api.get_vcenter(id=entity.entity_id)
        if ds.ip == vcenter_ip:
            return entity.entity_id

def verify_datasource_using_be_api(cls, setup_test, add_request_body, datasource_type):
    be_data_source_list = cls.get_be_data_sources(setup_test)
    for be_datasource in be_data_source_list:
        if add_request_body['ip'] in be_datasource['dpId'] and be_datasource['dataSource_type'] == datasource_type:
            try:
                cls.verify(be_datasource['nickName'], add_request_body['nickname'], "nickname")
                if add_request_body['notes']:
                    cls.verify(be_datasource['notes'], add_request_body['notes'], "notes")
                return True
            except AssertionError:
                return False
    return False

def main(api_client, args):

    # Create datasource API client object
    datasource_api = swagger_client.DataSourcesApi(api_client=api_client)
    proxy_id = get_node_entity_id(api_client, 'PROXY_VM')
    with open("%s" % args.datasourcesCSV, 'rb') as csvFile:
        datasources = csv.DictReader(csvFile)
        for datasource in datasources:
            datasource_type = datasource['DataSourceType']
            vcenter_id = get_vcenter_manager_entity_id(datasource_api, datasource['ParentvCenter'])
            print("Adding: {} {}".format(datasource_type, datasource['IP']))
            datasource_api_name = get_api_function_name(datasource_type)
            add_datasource_api_fn = getattr(datasource_api, datasource_api_name)
            try:
                response = add_datasource_api_fn(body=get_add_request_body(datasource, proxy_id, vcenter_id))
                print("Successfully added: {} {} : Response : {}".format(datasource_type, datasource['IP'], response))
            except ApiException as e:
                logging.error("Failed adding datasource: %s : Error : %s " % (datasource['IP'], json.loads(e.body)))
    csvFile.close()

if __name__ == '__main__':
    args = init_api_client.parse_arguments()
    api_client = init_api_client.get_api_client(args)
    main(api_client, args)
