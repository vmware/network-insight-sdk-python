# Python SDK Examples
#
# Script will create one application and three tiers in it
# Delete application snippet also included
#
# Copyright 2019 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later

import init_api_client
import swagger_client

import utilities
import logging

logger = logging.getLogger("vrni_sdk")


def create_appication_and_tiers(application_api, args):
    app_name = "{}".format(args.application_name)
    body = {"name": app_name}
    app = application_api.add_application(body)
    logger.info("Application {} created".format(app_name))
    create_tiers(app_name, application_api, app, args.vm_names)


def create_tiers(app_name, application_api, app, vm_names):
    # Create tier using swagger models
    tier1 = swagger_client.Tier()
    tier1.entity_type = swagger_client.AllEntityType.TIER
    tier1.name = "%s_tier" % app_name
    vms = vm_names.split(',')

    filter = "name={}".format(vms[0])
    if len(vms) > 1:
        for vm in vms[1:]:
            filter = filter+ "or name".format(vm)

    grp_membership_criteria = swagger_client.GroupMembershipCriteria()
    grp_membership_criteria.membership_type = "SearchMembershipCriteria"
    grp_membership_criteria.ip_address_membership_criteria = None
    grp_membership_criteria.search_membership_criteria = swagger_client.SearchMembershipCriteria(
        entity_type=swagger_client.AllEntityType.VIRTUALMACHINE,
        filter=filter)

    tier1.group_membership_criteria = [grp_membership_criteria]

    application_api.add_tier(app.entity_id, tier1)
    logger.info("{}_tier created".format(app_name))

def delete_application(application_api, application_name):
    apps = application_api.list_applications()
    for i in apps.results:
        app = application_api.get_application(i.entity_id)
        if application_name in app.name:
            tiers = application_api.list_application_tiers(id=app.entity_id)
            for t in tiers.results:
                application_api.delete_tier(app.entity_id, t.entity_id)
            application_api.delete_application(i.entity_id)
            break


def main(args):
    # Create application API client object
    application_api = swagger_client.ApplicationsApi()
    create_appication_and_tiers(application_api, args)

def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument("--application_name",action="store", help="Provide Application name", required=True)
    parser.add_argument("--vm_names", action="store", help="Provide comma separated names of vms", required=True)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main(args)
