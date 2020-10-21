# Copyright 2019 VMware, Inc.
# SPDX-License-Identifier: GPL-2.0-or-later

import argparse
import swagger_client
import json
import sys
import utilities
import logging
import requests

logger = logging.getLogger('vrni_sdk')


def get_api_client(args):
    if args.deployment_type == "onprem":
        if not args.platform_ip:
            logger.error("Please provide platform_ip of onprem setup !!!")
            sys.exit()
        return get_onprem_api_client(args)
    else:
        if not args.api_token:
            logger.error("Please provide refresh token for VRNIC setup !!!")
            sys.exit()
        return get_vrnic_api_client(args)


def delete_token(args, api_client):
    if args.deployment_type == "onprem":
        logger.info("Deleting API token")
        auth_api = swagger_client.AuthenticationApi(api_client=api_client)
        auth_api.delete()


def get_onprem_api_client(args):
    config = swagger_client.Configuration()
    config.verify_ssl = False

    logger.info("Getting api client for IP <{}>".format(args.platform_ip))
    api_client = swagger_client.ApiClient(host="https://{}/api/ni".format(args.platform_ip))
    auth_api = swagger_client.AuthenticationApi(api_client=api_client)
    if args.domain_type == "LOCAL" or args.domain_type == "LDAP":
        user_creds = swagger_client.UserCredential(username=args.username, password=args.password,
                                                   domain=dict(domain_type=args.domain_type, value=args.domain_value))
        auth_token = auth_api.create(user_creds)
    elif args.domain_type == "VIDM":
        if args.get_vidm_client_id:
            client_id = auth_api.get_vidm_oauth_clien_id()
            logger.info("client-id for vIDM is - '{}'".format(client_id.client_id))
            return
        user_creds = swagger_client.VidmToken(vidm_token=args.vidm_token)
        auth_token = auth_api.create_vidm_user_token(user_creds)
    else:
        raise ValueError('Please give correct domain_type: LOCAL, LDAP or VIDM')

    config.api_key['Authorization'] = auth_token.token
    config.api_key_prefix['Authorization'] = 'NetworkInsight'
    config.api_client = api_client
    return api_client


def get_vrnic_api_client(args):
    public_api_url = "https://onecloud.api.mgmt.cloud.vmware.com/ni/api/ni"
    public_api_client = swagger_client.ApiClient(host=public_api_url)
    config = swagger_client.Configuration()
    config.verify_ssl = False
    logger = logging.getLogger('vrni_sdk')

    logger.info("Getting api client for VRNIC")
    config.api_key['csp-auth-token'] = get_vrnic_csp_auth_token(args, config.api_client)
    config.deployment_type = args.deployment_type
    config.api_client = public_api_client
    return public_api_client


def get_vrnic_csp_auth_token(args, api_client):
    authorize_api_url = "https://console.cloud.vmware.com/csp/gateway/am/api/auth/api-tokens/authorize" \
                        "?refresh_token={}".format(args.api_token)
    response = requests.post(authorize_api_url)
    response = json.loads(str(response.text))
    csp_auth_token = response['access_token']
    return csp_auth_token


def domain_type(type):
    if not type in ['LOCAL', 'LDAP', 'VIDM']:
        raise argparse.ArgumentTypeError('argument domain type must be one of type LOCAL, LDAP or VIDM')
    return type


def parse_arguments():
    parser = argparse.ArgumentParser(description='Run Public APIs on vRNI Platform')
    parser.add_argument("--deployment_type", action="store",
                        help="Setup deployment type: onprem or vrnic", default='onprem')
    parser.add_argument('--platform_ip', action='store',
                        help='IP address of vRNI platform. In case of cluster IP address of Platform-1')
    parser.add_argument('--username', action='store', default='admin@local',
                        help='user name for authentication')
    parser.add_argument("--password", action="store",
                        default='admin', help="password for authentication")
    parser.add_argument("--domain_type", action="store", type=domain_type,
                        default='LOCAL', help="domain type for authentication: LOCAL or LDAP or VIDM")
    parser.add_argument("--domain_value", action="store",
                        default='example.com', help="domain value for LDAP user: example.com")
    parser.add_argument("--get_vidm_client_id", action="store_true",
                        help="Get client-id for making user access-token request to vIDM")

    # Procedure to generate vidm_token
    #    1. Get the client-id for making user access-token request to VMware Identity Manager by executing
    #       init_api_client.py --get_vidm_client_id \
    #                          --domain_type VIDM \
    #                          --platform_ip $Platfrom-IP \
    #                          --deployment_type onprem
    #    2. Using client-id alongwith user credentials make an access token request to VMware Identity Manager.
    #       e.g. POST: https://xyz.com/SAAS/auth/oauthtoken?username=${username}&password=${password}&client_id=${client_id}&grant_type=password
    parser.add_argument('--vidm_token', action='store', help='Provide vidm_token')

    # Network Insight as a service (VRNIC) parameters.
    # Procedure to generate api token
    #    1. On the VMware Cloud Services toolbar, click your user name and select My Account > API Tokens.
    #    2. Click on Generate Token.
    #    3. Define Scopes : Check organistion member and Network Insight Administrator Roles or All roles.
    #    4. Click on generate and then Copy button on Token generated popup and pass it as input parameter to api_token
    parser.add_argument('--api_token', action='store', help='Provide VRNIC api token')

    return parser


if __name__ == '__main__':
    parser = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client_onprem = get_api_client(parser.parse_args())

# for nd setups -
# authorize_api_url = "https://csp.nd31.vrni-symphony.com/csp/gateway/am/api/auth/api-tokens/authorize?refresh_token={}".format(
#         args.api_token)
# public_api_url = "https://nd31.us.www.main.vrni-symphony.com/ni/api/ni"
