import argparse
import swagger_client


def get_api_client(args):
    config = swagger_client.Configuration()
    config.verify_ssl = False

    api_client = swagger_client.ApiClient(host="https://{}/api/ni".format(args.platform_ip))
    user_creds = swagger_client.UserCredential(username=args.username, password=args.password,
                                               domain=dict(domain_type=args.domain_type))

    auth_api = swagger_client.AuthenticationApi(api_client=api_client)

    auth_token = auth_api.create(user_creds)

    config.api_key['Authorization'] = auth_token.token
    config.api_key_prefix['Authorization'] = 'NetworkInsight'
    config.api_client = api_client
    return api_client


def parse_arguments():
    parser = argparse.ArgumentParser(description='Run Public APIs on vRNI Platform')
    parser.add_argument('--platform_ip', action='store',
                        help='IP address of vRNI platform. In case of cluster IP address of Platform-1')
    parser.add_argument('--username', action='store', default='admin@local',
                        help='user name for authentication')
    parser.add_argument("--password", action="store",
                        default='admin', help="password for authentication")
    parser.add_argument("--domain_type", action="store",
                        default='LOCAL', help="domain type for authentication")
    parser.add_argument("--data_sources_csv", action="store",
                        default='data_sources.csv', help="domain type for authentication")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    api_client = get_api_client(args)
