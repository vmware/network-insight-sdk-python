# Example: Bulk import applications from CSV
#
# START Description
# Imports applications that are defined in a file called cmdb_ci_hardware.csv.
# END Description
#
# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later

import csv
import collections
import json
import netaddr
import swagger_client
import init_api_client
import utilities

import logging
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger("vrni_sdk")

# CSV format - required for running this script.
# u_app_name    |   u_subsystem |   ip_address  |
# app_1         |   tier_1      | 10.53.212.34  |
# app_1         |   tier_2      | 10.53.213.42  |
# app_2         |   tier_1      | 10.53.112.65  |


def add_tier_and_ip(apps_tiers, raw):
    if raw['u_app_name'] not in apps_tiers.keys():
        apps_tiers[raw['u_app_name']] = dict()
        apps_tiers[raw['u_app_name']][raw['u_subsystem']] = []
        apps_tiers[raw['u_app_name']][raw['u_subsystem']].append(
            raw["ip_address"])
    elif raw['u_subsystem'] not in apps_tiers[raw['u_app_name']]:
        apps_tiers[raw['u_app_name']][raw['u_subsystem']] = []
        apps_tiers[raw['u_app_name']][raw['u_subsystem']].append(
            raw["ip_address"])
    else:
        apps_tiers[raw['u_app_name']][raw['u_subsystem']].append(
            raw["ip_address"])


def delete_token(api_client):
    logger.info("Deleting API token")
    auth_api = swagger_client.AuthenticationApi(api_client=api_client)
    auth_api.delete()


def main(api_client, args):
    application_api = swagger_client.ApplicationsApi()
    if args.delete_apps:
        delete_application(application_api)
        delete_token(api_client)
        return

    reader = csv.DictReader(open("cmdb_ci_hardware.csv"))

    app_names = set()
    locations = collections.defaultdict(int)
    app_ips = collections.defaultdict(list)
    apps_tiers = collections.defaultdict(dict)
    total_rows = 0
    rows = 0
    for raw in reader:
        total_rows += 1
        raw['u_app_name'] = raw['u_app_name'].encode("utf-8")
        raw['u_app_name'] = raw['u_app_name'].lower()
        if raw['u_app_name']:
            add_tier_and_ip(apps_tiers, raw)
            app_names.add(raw['u_app_name'])
            rows += 1
            locations[raw['u_location']] += 1
            app_ips[raw['u_app_name']].append(raw["ip_address"])

    print("Total Apps discovered: {}".format(len(app_names)))
    print(app_names)
    print("Total rows: {}, Rows with apps: {}".format(total_rows, rows))
    print("Location wise distribution")
    print(json.dumps(locations, indent=4))
    for app, ips in app_ips.items():
        print("App Name: {:50} No of IPs: {}".format(app, len(ips)))
    print(json.dumps(app_ips, indent=4))

    app_no = 1
    for app_name, value in apps_tiers.items():
        vrni_app = create_application(application_api, app_name)
        logger.info("{} App Created: [{}]".format(app_no, app_name))
        create_tiers(app_name, application_api, vrni_app, apps_tiers[app_name])
        app_no += 1

    delete_token(api_client)


def get_applications(application_api):
    apps_list = []
    logger.info(
        "Getting list of all applications starting with name 'vrni_auto_'")
    app_no = 1
    apps = application_api.list_applications(size=100, cursor="")
    while True:
        for i in apps.results:
            app = application_api.get_application(i.entity_id)
            if app.name.startswith('vrni_auto_'):
                logger.info("Getting app {} : {}".format(app_no, app.name))
                apps_list.append(app)
                app_no += 1
        if not apps.cursor:
            break
        apps = application_api.list_applications(cursor=apps.cursor, size=100)
    return apps_list


def delete_application(application_api):
    app_no = 1
    apps = get_applications(application_api)
    for app in apps:
        tiers = application_api.list_application_tiers(id=app.entity_id)
        for t in tiers.results:
            application_api.delete_tier(app.entity_id, t.entity_id)
            logger.info("    Tier Deleted [{}].".format(t.name))
        application_api.delete_application(app.entity_id)
        logger.info("{}: App Deleted [{}].".format(app_no, app.name))
        app_no += 1


def create_application(application_api, application_name):
    app_name = "vrni_auto_{}".format(application_name)
    body = {"name": app_name}
    app = application_api.add_application(body)
    return app


def create_tiers(app_name, application_api, app, cmdb_app):
    # Create tier using swagger models
    # create tier using json
    tier_defn = {
        "name": "dummy_name",
        "entity_type": "Tier",
        "group_membership_criteria": [
            {
                "membership_type": "IPAddressMembershipCriteria",
                "ip_address_membership_criteria": {
                    "ip_addresses": []
                }
            }
        ]
    }

    for tier_name, ips in cmdb_app.items():
        if not ips:
            continue
        invalid_ips = False
        for ip in ips:
            if not ip:
                invalid_ips = True
                break
            if not netaddr.valid_ipv4(ip):
                invalid_ips = True
                break
        if invalid_ips:
            logger.info("INVALID IPS: {}".format(ips))
            continue
        if not tier_name:
            tier_name = "no_name"
        tier_defn['name'] = tier_name
        tier_defn['group_membership_criteria'][0]['ip_address_membership_criteria']['ip_addresses'] = ips

        application_api.add_tier(app.entity_id, tier_defn)
        logger.info("    Tier [{}] created".format(tier_name))


def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument("--delete_apps", action='store_true',
                        help="Delete all vrni_auto_* apps")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main(api_client, args)
