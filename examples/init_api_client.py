import swagger_client

# TODO: Change IP of vRNI platform
vRNI_IP = '10.197.17.236'
USERNAME = 'admin@local'
PASSWORD = 'admin123'

DOMAIN_TYPE = 'LOCAL'


def get_api_client():
    config = swagger_client.Configuration()
    config.verify_ssl = False

    api_client = swagger_client.ApiClient(host="https://{}/api/ni".format(vRNI_IP))
    user_creds = swagger_client.UserCredential(username=USERNAME, password=PASSWORD, domain=dict(domain_type=DOMAIN_TYPE))

    auth_api = swagger_client.AuthenticationApi(api_client=api_client)

    auth_token = auth_api.create(user_creds)

    config.api_key['Authorization'] = auth_token.token
    config.api_key_prefix['Authorization'] = 'NetworkInsight'
    return api_client


if __name__ == '__main__':
    get_api_client()
