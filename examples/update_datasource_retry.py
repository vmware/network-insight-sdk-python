#!/usr/bin/env python3

# pylint: disable=line-too-long
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
from datetime import datetime
import functools32
import json
import logging
import time
import traceback

import swagger_client

from swagger_client.rest import ApiException
import swagger_client.models.data_source_type as ds_type

import init_api_client
import utilities

logger = logging.getLogger("vrni_sdk")
MAX_ATTEMPTS = 5
ENTITY_CACHE = {}


def get_api_function_name(datasource_type, function):
    datasource = {
        ds_type.DataSourceType.CISCOSWITCHDATASOURCE: {"update_snmp_config": "update_cisco_switch_snmp_config",
                                                                "get_snmp_config": "get_cisco_switch_snmp_config",
                                                                "update": "update_cisco_switch",
                                                                "get": "get_cisco_switch",
                                                                "list": "list_cisco_switches",
                                                                "enable": "enable_cisco_switch",
                                                                "disable": "disable_cisco_switch"},
        ds_type.DataSourceType.DELLSWITCHDATASOURCE: {"update_snmp_config": "update_dell_switch_snmp_config",
                                                               "get_snmp_config": "get_dell_switch_snmp_config",
                                                               "update": "update_dell_switch",
                                                               "get": "get_dell_switch",
                                                               "list": "list_dell_switches",
                                                               "enable": "enable_dell_switch",
                                                               "disable": "disable_dell_switch"},
        ds_type.DataSourceType.ARISTASWITCHDATASOURCE: {"update_snmp_config": "update_arista_switch_snmp_config",
                                                                 "get_snmp_config": "get_arista_switch_snmp_config",
                                                                 "update": "update_arista_switch",
                                                                 "get": "get_arista_switch",
                                                                 "list": "list_arista_switches",
                                                                 "enable": "enable_arista_switch",
                                                                 "disable": "disable_arista_switch"},
        ds_type.DataSourceType.BROCADESWITCHDATASOURCE: {"update_snmp_config": "update_brocade_switch_snmp_config",
                                                                  "get_snmp_config": "get_brocade_switch_snmp_config",
                                                                  "update": "update_brocade_switch",
                                                                  "get": "get_brocade_switch",
                                                                  "list": "list_brocade_switches",
                                                                  "enable": "enable_brocade_switch",
                                                                  "disable": "disable_brocade_switch"},
        ds_type.DataSourceType.JUNIPERSWITCHDATASOURCE: {"update_snmp_config": "update_juniper_switch_snmp_config",
                                                                  "get_snmp_config": "get_juniper_switch_snmp_config",
                                                                  "update": "update_juniper_switch",
                                                                  "get": "get_juniper_switch",
                                                                  "list": "list_juniper_switches",
                                                                  "enable": "enable_juniper_switch",
                                                                  "disable": "disable_juniper_switch"},
        ds_type.DataSourceType.VCENTERDATASOURCE: {"update": "update_vcenter",
                                                            "get": "get_vcenter",
                                                            "list": "list_vcenters",
                                                            "enable": "enable_vcenter",
                                                            "disable": "disable_vcenter"},
        ds_type.DataSourceType.NSXVMANAGERDATASOURCE: {"update": "update_nsxv_manager",
                                                                "get": "get_nsxv_manager",
                                                                "list": "list_nsxv_managers",
                                                                "enable": "enable_nsxv_manager",
                                                                "disable": "disable_nsxv_manager"},
        ds_type.DataSourceType.UCSMANAGERDATASOURCE: {"update_snmp_config": "update_ucs_snmp_config",
                                                               "get_snmp_config": "get_ucs_snmp_config",
                                                               "update": "update_ucs_manager",
                                                               "get": "get_ucs_manager",
                                                               "list": "list_ucs_managers",
                                                               "enable": "enable_ucs_manager",
                                                               "disable": "disable_ucs_manager"},
        ds_type.DataSourceType.HPVCMANAGERDATASOURCE: {"update": "update_hpvc_manager",
                                                                "get": "get_hpvc_manager",
                                                                "list": "list_hpvc_managers",
                                                                "enable": "enable_hpvc_manager",
                                                                "disable": "disable_hpvc_manager"},
        ds_type.DataSourceType.HPONEVIEWDATASOURCE: {"update": "update_hpov_manager",
                                                              "get": "get_hpov_manager",
                                                              "list": "list_hpov_managers",
                                                              "enable": "enable_hpov_manager",
                                                              "disable": "disable_hpov_manager"},
        ds_type.DataSourceType.PANFIREWALLDATASOURCE: {"update": "update_panorama_firewall",
                                                                "get": "get_panorama_firewall",
                                                                "list": "list_panorama_firewalls",
                                                                "enable": "enable_panorama_firewall",
                                                                "disable": "disable_panorama_firewall"},
        ds_type.DataSourceType.CHECKPOINTFIREWALLDATASOURCE: {"update": "update_checkpoint_firewall",
                                                                       "get": "get_checkpoint_firewall",
                                                                       "list": "list_checkpoint_firewalls",
                                                                       "enable": "enable_checkpoint_firewall",
                                                                       "disable": "disable_checkpoint_firewall"},
        ds_type.DataSourceType.NSXTMANAGERDATASOURCE: {"update": "update_nsxt_manager",
                                                                "get": "get_nsxt_manager",
                                                                "list": "list_nsxt_managers",
                                                                "enable": "enable_nsxt_manager",
                                                                "disable": "disable_nsxt_manager"},
        ds_type.DataSourceType.KUBERNETESDATASOURCE: {"update": "update_kubernetes_datasource",
                                                               "get": "get_kubernetes_cluster",
                                                               "list": "list_kubernetes_clusters",
                                                               "enable": "enable_kubernetes_cluster",
                                                               "disable": "disable_kubernetes_cluster"},
        ds_type.DataSourceType.F5BIGIPDATASOURCE: {"update_snmp_config": "update_f5_bigip_snmp_config",
                                                            "get_snmp_config": "get_f5_bigip_snmp_config",
                                                            "update": "update_f5_bigip",
                                                            "get": "get_f5_bigip",
                                                            "list": "list_f5_bigip",
                                                            "enable": "enable_f5_bigip",
                                                            "disable": "disable_f5_bigip"},
        ds_type.DataSourceType.POLICYMANAGERDATASOURCE: {"update": "update_policy_manager",
                                                                  "get": "get_policy_manager",
                                                                  "list": "list_policy_managers",
                                                                  "enable": "enable_policy_manager",
                                                                  "disable": "disable_policy_manager"}}

    return datasource[datasource_type][function]


def get_update_request_body(response, data_source):
    if hasattr(response, "credentials"):
        response.credentials.username = data_source['Username']
        response.credentials.password = data_source['Password']
    if hasattr(response, "csp_refresh_token"):
        response.csp_refresh_token = data_source['CSPRefreshToken']
    response.nickname = data_source['NickName']
    response.notes = data_source['Notes']
    return response

def update_snmp_config(entity_id, data_source_api, data_source):
    try:
        update_snmp_api_fn = getattr(data_source_api, get_api_function_name(data_source['DataSourceType'], 'update_snmp_config'))
        get_snmp_api_fn = getattr(data_source_api, get_api_function_name(data_source['DataSourceType'], 'get_snmp_config'))
        response = get_snmp_api_fn(id=entity_id)
        if data_source['snmp_version'] == 'v2c':
            if  response.snmp_version == 'v2c':
                response.config_snmp_2c.community_string = data_source['snmp_community_string']
            else: # updating to v2c from v3
                response = {"snmp_enabled": True,
                    "snmp_version": "{}".format(data_source['snmp_version'])}
                snmp_config = dict(
                    config_snmp_2c=dict(community_string='{}'.format(data_source['snmp_community_string'])))
                response.update(snmp_config)
        elif data_source['snmp_version'] == 'v3':
            if response.snmp_version == 'v3':
                response.config_snmp_3.username = data_source['snmp_username']
                response.config_snmp_3.authentication_password = data_source['snmp_password']
                response.config_snmp_3.authentication_type = data_source['snmp_auth_type']
                response.config_snmp_3.privacy_type = data_source['snmp_privacy_type']
            else:  # updating to v3 from v2c
                response = {"snmp_enabled": True,
                            "snmp_version": "{}".format(data_source['snmp_version']),
                            }
                snmp_config = dict(config_snmp_3=dict(
                        username="{}".format(data_source['snmp_username']),
                        authentication_password="{}".format(data_source['snmp_password']),
                        context_name="",
                        authentication_type="{}".format(data_source['snmp_auth_type']),
                        privacy_type="{}".format(data_source['snmp_privacy_type'])))
                response.update(snmp_config)
    except ApiException as e:
        logger.error("Failed to get snmp config: Error : {} ".format(json.loads(e.body)))
    # if 'retry' throws an Exception, let the calling method handle it
    retry(update_snmp_api_fn, id=entity_id, body=response)

@functools32.lru_cache()
def get_entities_by_type(datasource_type, api):
    list_datasource_api_fn = get_api_function_name(datasource_type, 'list')
    #this log message will only print when the datasource_type is not cached
    logger.info("Fetching all entities of type '{}'".format(datasource_type))
    return getattr(api, list_datasource_api_fn)()

def get_data_source_entity(get_datasource_fn, data_source_list, to_find):
    # init the cache for this datasource type if needed
    if not to_find['DataSourceType'] in ENTITY_CACHE:
        ENTITY_CACHE[to_find['DataSourceType']] = []
    datasource_cache = ENTITY_CACHE.get(to_find['DataSourceType'])

    # check to see if we've already fetched this entity
    in_cache = next(iter(filter(lambda x: x.ip == to_find['IP'] or x.fqdn == to_find['fqdn'], datasource_cache)), None)
    if in_cache:
        logger.debug("Found {} in cache".format(_get_label(to_find)))
        return in_cache

    # iterate over list of entity_id's and fetch their entity instances
    for index, entity in enumerate(data_source_list.results):
        already_fetched = next(iter(filter(lambda x: x.entity_id == entity.entity_id, datasource_cache)), None)
        if already_fetched:
            #this entity is already in the cache and not the ds we're looking for
            continue

        # not in the cache, fetch it
        logger.debug("Fetching entity with ID: {}  ({} of {})".format(entity.entity_id, index + 1, len(data_source_list.results)))
        ds = get_datasource_fn(id=entity.entity_id)

        ENTITY_CACHE[to_find['DataSourceType']].append(ds)

        # this is the entity we're looking for, exit early
        if ds.ip == to_find['IP'] or ds.fqdn == to_find['fqdn']:
            return ds
    return None

def retry(fun, *args, **kwargs):
    """Attempt to run the function 'fun'.  If it throws an Exception, wait 1 second then try again
       Catches any possible Exception typess but only throws an ApiException if all attempts fail"""
    last_error = None
    for i in range(MAX_ATTEMPTS):
        try:
            return fun(*args, **kwargs)
        except ApiException as e:
            logger.info("Failed to run <{}> (attempt {} of {}), {}".format(fun.__name__, i + 1, MAX_ATTEMPTS, json.loads(e.body)))
            last_error = ApiException(reason=json.loads(e.body))
            time.sleep(1)
        except Exception as e:
            logger.info("Failed to run <{}> (attempt {} of {}), {}".format(fun.__name__, i + 1, MAX_ATTEMPTS, traceback.format_exc()))
            last_error = ApiException(reason=traceback.format_exc())
            time.sleep(1)
    raise last_error

def _get_label(csv_row):
    return "{} '{}'".format(csv_row['DataSourceType'], csv_row['IP'] if csv_row['IP'] else csv_row['fqdn'])

def main(api_client, args):

    failure_log = []
    notfound_log = []
    # Create data source API client object
    start_time = datetime.now()
    data_source_api = swagger_client.DataSourcesApi(api_client=api_client)
    total_lines = len(open(args.data_sources_csv).readlines()) - 1 #subtract header row
    with open(args.data_sources_csv, 'rt') as csvFile:
        data_sources = csv.DictReader(csvFile)
        for csv_row in data_sources:
            data_source_type = csv_row['DataSourceType']
            if (datetime.now() - start_time).total_seconds() > 1500:
                init_api_client.delete_token(args, api_client)
                api_client = init_api_client.get_api_client(args)
                data_source_api = swagger_client.DataSourcesApi(api_client=api_client)

            logger.info("Adding: {} [{} of {}]".format(_get_label(csv_row), data_sources.line_num - 1, total_lines))
            # Get the Data source add api fn
            get_datasource_fn = getattr(data_source_api, get_api_function_name(data_source_type, 'get'))
            update_datasource_fn = getattr(data_source_api, get_api_function_name(data_source_type, 'update'))
            try:
                data_source_list = get_entities_by_type(data_source_type, data_source_api)
                logger.info("Successfully got list of {} : Total Count : {}".format(data_source_type, data_source_list.total_count))

                entity = get_data_source_entity(get_datasource_fn, data_source_list, csv_row)
                if not entity:
                    logger.error("Could not find datasource entity: {}".format(_get_label(csv_row)))
                    notfound_log.append("Line {}: {}".format(data_sources.line_num, ';'.join(list(csv_row.values()))))
                    continue

                logger.info("Attempting to update {}".format(_get_label(csv_row)))
                updated_request_body = get_update_request_body(entity, csv_row)
                retry(update_datasource_fn, id=entity.entity_id, body=updated_request_body)
                logger.info("Successfully updated {}".format(_get_label(csv_row)))

                if csv_row['snmp_version']:
                    try:
                        logger.info("Attempting to update SNMP Config for {}".format(_get_label(csv_row)))
                        retry(update_snmp_config, entity.entity_id, data_source_api, csv_row)
                        logger.info("Successfully updated SNMP Config for {}".format(_get_label(csv_row)))
                    except ApiException as e:
                        logger.error("Failed to update snmp config for {}: Error : {} ".format(_get_label(csv_row), e.reason))
                        failure_log.append("Line {}: {}".format(data_sources.line_num, ';'.join(list(csv_row.values()))))

                #modifying credentials via API doesn't restart datasource with those new credentials prior to vRNI 6.0
                if args.restart:
                    logger.info("Stopping datasource: {}".format(_get_label(csv_row)))
                    disable_datasource_fn = getattr(data_source_api, get_api_function_name(data_source_type, 'disable'))
                    disable_datasource_fn(entity.entity_id)
                    time.sleep(1)
                    logger.info("Starting datasource: {}".format(_get_label(csv_row)))
                    enable_datasource_fn = getattr(data_source_api, get_api_function_name(data_source_type, 'enable'))
                    enable_datasource_fn(entity.entity_id)
                    logger.info("Successfully Restarted: {}".format(_get_label(csv_row)))
            except ApiException as e:
                logger.error("Failed to update {}: Error : {} ".format(_get_label(csv_row), e.reason))
                failure_log.append("Line {}: {}".format(data_sources.line_num, ';'.join(list(csv_row.values()))))
    return (failure_log, notfound_log)



def parse_arguments():
    global MAX_ATTEMPTS
    parser = init_api_client.parse_arguments()
    parser.add_argument("--data_sources_csv", action="store",
                        default='update_data_sources.csv', help="csv file with your own data sources")
    parser.add_argument("--max_attempts", action="store", type=int,
                        default=5, help="number of retry attempts per API call (default: {})".format(MAX_ATTEMPTS))
    parser.add_argument("--restart", action="store_true",
                        help="Restart datasources after successful modification (default: false)")
    args = parser.parse_args()
    if args.max_attempts:
        MAX_ATTEMPTS = args.max_attempts
    return args

if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/Users/sbhagwat/repos/network-insight-sdk-python/examples")
    api_client = init_api_client.get_api_client(args)
    (failure_log, notfound_log) = main(api_client, args)
    if failure_log:
        print("\n")
        print("-- API call failed for the following CSV line{}:".format('' if len(failure_log) == 1 else 's'))
        for failure in failure_log:
            print(failure)
    if notfound_log:
        print("\n")
        print("-- Could not find datasource corresponding to the following CSV line{}:".format('' if len(notfound_log) == 1 else 's'))
        for notfound in notfound_log:
            print(notfound)
