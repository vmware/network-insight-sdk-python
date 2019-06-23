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
        if not args.refresh_token:
            logger.error("Please provide refresh token for niaas setup !!!")
            sys.exit()
        return get_niaas_api_client(args)

def get_onprem_api_client(args):
    config = swagger_client.Configuration()
    config.verify_ssl = False

    logger.info("Getting api client for IP <{}>".format(args.platform_ip))
    api_client = swagger_client.ApiClient(host="https://{}/api/ni".format(args.platform_ip))
    user_creds = swagger_client.UserCredential(username=args.username, password=args.password,
                                               domain=dict(domain_type=args.domain_type))

    auth_api = swagger_client.AuthenticationApi(api_client=api_client)

    auth_token = auth_api.create(user_creds)

    config.api_key['Authorization'] = auth_token.token
    config.api_key_prefix['Authorization'] = 'NetworkInsight'
    config.api_client = api_client
    return api_client

def get_niaas_api_client(args):
    public_api_url = "https://api.mgmt.cloud.vmware.com/ni/api/ni"
    public_api_client = swagger_client.ApiClient(host=public_api_url)
    config = swagger_client.Configuration()
    config.verify_ssl = False
    logger = logging.getLogger('vrni_sdk')

    logger.info("Getting api client for NIAAS")
    config.api_key['csp-auth-token'] = get_niaas_csp_auth_token(args, config.api_client)
    config.deployment_type = args.deployment_type
    config.api_client = public_api_client
    return public_api_client

def get_niaas_csp_auth_token(args, api_client):
    authorize_api_url = "https://console.cloud.vmware.com/csp/gateway/am/api/auth/api-tokens/authorize" \
                        "?refresh_token={}".format(args.refresh_token)
    response = requests.post(authorize_api_url)
    response = json.loads(str(response.text))
    csp_auth_token = response['access_token']
    return csp_auth_token


def parse_arguments():
    parser = argparse.ArgumentParser(description='Run Public APIs on vRNI Platform')
    parser.add_argument("--deployment_type", action="store",
                     help="Setup deployment type: onprem or niaas", default='onprem')
    parser.add_argument('--platform_ip', action='store',
                        help='IP address of vRNI platform. In case of cluster IP address of Platform-1')
    parser.add_argument('--username', action='store', default='admin@local',
                        help='user name for authentication')
    parser.add_argument("--password", action="store",
                        default='admin', help="password for authentication")
    parser.add_argument("--domain_type", action="store",
                        default='LOCAL', help="domain type for authentication")

    # Network Insight as a service (NIAAS) parameters
    # To obtain org-scoped refresh token from NetworkInsight UI refer API documentation.
    # https://vdc-download.vmware.com/vmwb-repository/dcr-public/e6fbbf75-fa7c-4cb2-b71b-0aa899c6d0ad/eed49fce-d8dc-48cb-b92a-2a5b252be673/vRealize-Network-Insight-API-Guide.pdf
    parser.add_argument('--refresh_token', action='store',
                        help='Provide niaas refresh token')

    return parser


if __name__ == '__main__':
    parser = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client_onprem = get_api_client(parser.parse_args())