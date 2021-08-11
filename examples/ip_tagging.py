# Example: Add IP addresses/subnets to EAST_WEST or INTERNET settings
#
# START Description
# This script uses an input CSV (example: ip_tags.csv)
# To add or remove IP addresses to EAST-WEST or INTERNET Tags vRealize Network Insight Data Sources.
# Modify ip_tags ip_tags.csv to contain your own data sources
# The script also retrieves EAST-WEST and INTERNET IPs configured in vRNI and export as CSV
# END Description
#
# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later


import csv
import ipaddress
import json
import init_api_client
import argparse
import swagger_client
import utilities
import logging
from swagger_client.rest import ApiException

logger = logging.getLogger("vrni_sdk")


def main(args):
    settings_api = swagger_client.SettingsApi()

    if args.action == 'add':
        logger.info("Adding IP-Addresses to EAST_WEST/INTERNET Tag")
        with open("{}".format(args.ip_tags_csv), 'r') as csvFile:
            ip_tags = csv.DictReader(csvFile)
            for ip_tag in ip_tags:
                ip_addresses = ip_tag['IP_Addresses']
                tag_id = ip_tag['TAG_ID']
                body = get_body(ip_addresses, tag_id)
                try:
                    logger.info("Adding {} to {} tag".format(
                        ip_addresses, tag_id))
                    settings_api.add_ip_tag(tag_id, body)
                except ApiException as e:
                    logger.exception(
                        "Failed adding {} to tag: {} : Error : {} ".format(ip_addresses, tag_id,
                                                                           json.loads(e.body)))
    if args.action == 'remove':
        logger.info("Removing IP-Addresses from EAST_WEST/INTERNET Tag")
        with open("{}".format(args.ip_tags_csv), 'r') as csvFile:
            ip_tags = csv.DictReader(csvFile)
            for ip_tag in ip_tags:
                ip_addresses = ip_tag['IP_Addresses']
                tag_id = ip_tag['TAG_ID']
                body = get_body(ip_addresses, tag_id)
                try:
                    logger.info("removing {} from {} tag".format(
                        ip_addresses, tag_id))
                    settings_api.remove_ip_tag(tag_id, body)
                except ApiException as e:
                    logger.exception(
                        "Failed removing {} from tag: {} : Error : {} ".format(ip_addresses, tag_id,
                                                                               json.loads(e.body)))

    if args.action == 'get':
        logger.info("Getting IP-Addresses with EAST_WEST/INTERNET Tag")
        with open("{}".format(args.ip_tags_csv), 'w') as csvFile:
            fields = ["IP_Addresses", "TAG_ID"]
            writer = csv.DictWriter(csvFile, fieldnames=fields)
            writer.writeheader()
            ip_tag_ids = settings_api.get_ip_tag_ids()
            data = []
            for tag_id in ip_tag_ids.tag_ids:
                ip_tags = settings_api.get_ip_tag(tag_id)
                for ip_tag in ip_tags.ip_address_ranges:
                    data_dict = {}
                    data_dict['TAG_ID'] = ip_tags.tag_id
                    if ip_tag.start_ip == ip_tag.end_ip:
                        data_dict['IP_Addresses'] = ip_tag.start_ip
                        data.append(data_dict)
                    else:
                        data_dict['IP_Addresses'] = "{}-{}".format(
                            ip_tag.start_ip, ip_tag.end_ip)
                        data.append(data_dict)
                data = data + [{"IP_Addresses": subnet, 'TAG_ID': ip_tags.tag_id}
                               for subnet in ip_tags.subnets]
            writer.writerows(data)
        for value in data:
            logger.info("Got {} with {} Tag".format(
                value['IP_Addresses'], value['TAG_ID']))


def get_body(ip_address, tag_id):
    body = {"tag_id": "{}".format(tag_id)}
    if "-" in ip_address:
        ips = ip_address.split("-")
        start_ip = ips[0]
        end_ip = ips[1]
        body["ip_address_ranges"] = [{"start_ip": "{}".format(start_ip),
                                      "end_ip": "{}".format(end_ip)}]
    elif "/" in ip_address:
        body["subnets"] = ["{}".format(ip_address)]
    else:
        body["ip_address_ranges"] = [{"start_ip": "{}".format(ip_address),
                                      "end_ip": "{}".format(ip_address)}]
    return body


def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument("--ip_tags_csv", action="store",
                        default='ip_tags.csv', help="Name of csv file")
    parser.add_argument("--action", action="store",
                        default='get', help="Action can be 'add' 'get' or 'remove'")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main(args)
