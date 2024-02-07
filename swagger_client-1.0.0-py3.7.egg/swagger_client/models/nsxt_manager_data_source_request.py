# coding: utf-8

"""
    VMware Aria Operations for Networks API Reference

    Operations for Networks API Reference

    OpenAPI spec version: 6.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NSXTManagerDataSourceRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ip': 'str',
        'fqdn': 'str',
        'proxy_id': 'str',
        'nickname': 'str',
        'enabled': 'bool',
        'notes': 'str',
        'credentials': 'PasswordCredentials',
        'ipfix_enabled': 'bool',
        'latency_enabled': 'bool',
        'nsxi_enabled': 'bool',
        'cloud_provider_type': 'CloudProviderTypeEnum',
        'cred_type': 'NSXCredTypeEnum',
        'client_certificate': 'str',
        'client_private_key': 'str',
        'ds_sub_type': 'str',
        'tags': 'list[LocalTag]',
        'enable_ds_associated_tags': 'bool'
    }

    attribute_map = {
        'ip': 'ip',
        'fqdn': 'fqdn',
        'proxy_id': 'proxy_id',
        'nickname': 'nickname',
        'enabled': 'enabled',
        'notes': 'notes',
        'credentials': 'credentials',
        'ipfix_enabled': 'ipfix_enabled',
        'latency_enabled': 'latency_enabled',
        'nsxi_enabled': 'nsxi_enabled',
        'cloud_provider_type': 'cloud_provider_type',
        'cred_type': 'cred_type',
        'client_certificate': 'client_certificate',
        'client_private_key': 'client_private_key',
        'ds_sub_type': 'ds_sub_type',
        'tags': 'tags',
        'enable_ds_associated_tags': 'enable_ds_associated_tags'
    }

    def __init__(self, ip=None, fqdn=None, proxy_id=None, nickname=None, enabled=True, notes=None, credentials=None, ipfix_enabled=False, latency_enabled=False, nsxi_enabled=False, cloud_provider_type=None, cred_type=None, client_certificate=None, client_private_key=None, ds_sub_type=None, tags=None, enable_ds_associated_tags=None):
        """
        NSXTManagerDataSourceRequest - a model defined in Swagger
        """

        self._ip = None
        self._fqdn = None
        self._proxy_id = None
        self._nickname = None
        self._enabled = None
        self._notes = None
        self._credentials = None
        self._ipfix_enabled = None
        self._latency_enabled = None
        self._nsxi_enabled = None
        self._cloud_provider_type = None
        self._cred_type = None
        self._client_certificate = None
        self._client_private_key = None
        self._ds_sub_type = None
        self._tags = None
        self._enable_ds_associated_tags = None

        if ip is not None:
          self.ip = ip
        if fqdn is not None:
          self.fqdn = fqdn
        self.proxy_id = proxy_id
        self.nickname = nickname
        if enabled is not None:
          self.enabled = enabled
        if notes is not None:
          self.notes = notes
        if credentials is not None:
          self.credentials = credentials
        if ipfix_enabled is not None:
          self.ipfix_enabled = ipfix_enabled
        if latency_enabled is not None:
          self.latency_enabled = latency_enabled
        if nsxi_enabled is not None:
          self.nsxi_enabled = nsxi_enabled
        if cloud_provider_type is not None:
          self.cloud_provider_type = cloud_provider_type
        if cred_type is not None:
          self.cred_type = cred_type
        if client_certificate is not None:
          self.client_certificate = client_certificate
        if client_private_key is not None:
          self.client_private_key = client_private_key
        if ds_sub_type is not None:
          self.ds_sub_type = ds_sub_type
        if tags is not None:
          self.tags = tags
        if enable_ds_associated_tags is not None:
          self.enable_ds_associated_tags = enable_ds_associated_tags

    @property
    def ip(self):
        """
        Gets the ip of this NSXTManagerDataSourceRequest.
        IP address of data source (use either IP or FQDN, not both)

        :return: The ip of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this NSXTManagerDataSourceRequest.
        IP address of data source (use either IP or FQDN, not both)

        :param ip: The ip of this NSXTManagerDataSourceRequest.
        :type: str
        """

        self._ip = ip

    @property
    def fqdn(self):
        """
        Gets the fqdn of this NSXTManagerDataSourceRequest.
        Hostname of data source (use either IP or FQDN, not both)

        :return: The fqdn of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this NSXTManagerDataSourceRequest.
        Hostname of data source (use either IP or FQDN, not both)

        :param fqdn: The fqdn of this NSXTManagerDataSourceRequest.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def proxy_id(self):
        """
        Gets the proxy_id of this NSXTManagerDataSourceRequest.
        ID of Collector VM which should register this vcenter

        :return: The proxy_id of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """
        Sets the proxy_id of this NSXTManagerDataSourceRequest.
        ID of Collector VM which should register this vcenter

        :param proxy_id: The proxy_id of this NSXTManagerDataSourceRequest.
        :type: str
        """
        if proxy_id is None:
            raise ValueError("Invalid value for `proxy_id`, must not be `None`")

        self._proxy_id = proxy_id

    @property
    def nickname(self):
        """
        Gets the nickname of this NSXTManagerDataSourceRequest.
        A friendly nickname for the data source

        :return: The nickname of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this NSXTManagerDataSourceRequest.
        A friendly nickname for the data source

        :param nickname: The nickname of this NSXTManagerDataSourceRequest.
        :type: str
        """
        if nickname is None:
            raise ValueError("Invalid value for `nickname`, must not be `None`")

        self._nickname = nickname

    @property
    def enabled(self):
        """
        Gets the enabled of this NSXTManagerDataSourceRequest.
        Whether or not data collection is enabled

        :return: The enabled of this NSXTManagerDataSourceRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this NSXTManagerDataSourceRequest.
        Whether or not data collection is enabled

        :param enabled: The enabled of this NSXTManagerDataSourceRequest.
        :type: bool
        """

        self._enabled = enabled

    @property
    def notes(self):
        """
        Gets the notes of this NSXTManagerDataSourceRequest.
        Room for notes or comments about the data source

        :return: The notes of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this NSXTManagerDataSourceRequest.
        Room for notes or comments about the data source

        :param notes: The notes of this NSXTManagerDataSourceRequest.
        :type: str
        """

        self._notes = notes

    @property
    def credentials(self):
        """
        Gets the credentials of this NSXTManagerDataSourceRequest.

        :return: The credentials of this NSXTManagerDataSourceRequest.
        :rtype: PasswordCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this NSXTManagerDataSourceRequest.

        :param credentials: The credentials of this NSXTManagerDataSourceRequest.
        :type: PasswordCredentials
        """

        self._credentials = credentials

    @property
    def ipfix_enabled(self):
        """
        Gets the ipfix_enabled of this NSXTManagerDataSourceRequest.
        Whether or not to configure NSX-T to send IPFIX to Operations for Networks

        :return: The ipfix_enabled of this NSXTManagerDataSourceRequest.
        :rtype: bool
        """
        return self._ipfix_enabled

    @ipfix_enabled.setter
    def ipfix_enabled(self, ipfix_enabled):
        """
        Sets the ipfix_enabled of this NSXTManagerDataSourceRequest.
        Whether or not to configure NSX-T to send IPFIX to Operations for Networks

        :param ipfix_enabled: The ipfix_enabled of this NSXTManagerDataSourceRequest.
        :type: bool
        """

        self._ipfix_enabled = ipfix_enabled

    @property
    def latency_enabled(self):
        """
        Gets the latency_enabled of this NSXTManagerDataSourceRequest.
        Whether or not to configure NSX-T to send virtual infrastructure latency metrics to Operations for Networks

        :return: The latency_enabled of this NSXTManagerDataSourceRequest.
        :rtype: bool
        """
        return self._latency_enabled

    @latency_enabled.setter
    def latency_enabled(self, latency_enabled):
        """
        Sets the latency_enabled of this NSXTManagerDataSourceRequest.
        Whether or not to configure NSX-T to send virtual infrastructure latency metrics to Operations for Networks

        :param latency_enabled: The latency_enabled of this NSXTManagerDataSourceRequest.
        :type: bool
        """

        self._latency_enabled = latency_enabled

    @property
    def nsxi_enabled(self):
        """
        Gets the nsxi_enabled of this NSXTManagerDataSourceRequest.
        Whether or not to configure NSX Intelligence to send additional traffic information to Operations for Networks

        :return: The nsxi_enabled of this NSXTManagerDataSourceRequest.
        :rtype: bool
        """
        return self._nsxi_enabled

    @nsxi_enabled.setter
    def nsxi_enabled(self, nsxi_enabled):
        """
        Sets the nsxi_enabled of this NSXTManagerDataSourceRequest.
        Whether or not to configure NSX Intelligence to send additional traffic information to Operations for Networks

        :param nsxi_enabled: The nsxi_enabled of this NSXTManagerDataSourceRequest.
        :type: bool
        """

        self._nsxi_enabled = nsxi_enabled

    @property
    def cloud_provider_type(self):
        """
        Gets the cloud_provider_type of this NSXTManagerDataSourceRequest.
        Identifier of the type of VMware Cloud Provider.

        :return: The cloud_provider_type of this NSXTManagerDataSourceRequest.
        :rtype: CloudProviderTypeEnum
        """
        return self._cloud_provider_type

    @cloud_provider_type.setter
    def cloud_provider_type(self, cloud_provider_type):
        """
        Sets the cloud_provider_type of this NSXTManagerDataSourceRequest.
        Identifier of the type of VMware Cloud Provider.

        :param cloud_provider_type: The cloud_provider_type of this NSXTManagerDataSourceRequest.
        :type: CloudProviderTypeEnum
        """

        self._cloud_provider_type = cloud_provider_type

    @property
    def cred_type(self):
        """
        Gets the cred_type of this NSXTManagerDataSourceRequest.
        Type of crendential mechanism. USERNAME_PASSWORD or CERTIFICATE.

        :return: The cred_type of this NSXTManagerDataSourceRequest.
        :rtype: NSXCredTypeEnum
        """
        return self._cred_type

    @cred_type.setter
    def cred_type(self, cred_type):
        """
        Sets the cred_type of this NSXTManagerDataSourceRequest.
        Type of crendential mechanism. USERNAME_PASSWORD or CERTIFICATE.

        :param cred_type: The cred_type of this NSXTManagerDataSourceRequest.
        :type: NSXCredTypeEnum
        """

        self._cred_type = cred_type

    @property
    def client_certificate(self):
        """
        Gets the client_certificate of this NSXTManagerDataSourceRequest.
        Public Certificate to connect to NSX-T

        :return: The client_certificate of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._client_certificate

    @client_certificate.setter
    def client_certificate(self, client_certificate):
        """
        Sets the client_certificate of this NSXTManagerDataSourceRequest.
        Public Certificate to connect to NSX-T

        :param client_certificate: The client_certificate of this NSXTManagerDataSourceRequest.
        :type: str
        """

        self._client_certificate = client_certificate

    @property
    def client_private_key(self):
        """
        Gets the client_private_key of this NSXTManagerDataSourceRequest.
        Private Key to connect to NSX-T

        :return: The client_private_key of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._client_private_key

    @client_private_key.setter
    def client_private_key(self, client_private_key):
        """
        Sets the client_private_key of this NSXTManagerDataSourceRequest.
        Private Key to connect to NSX-T

        :param client_private_key: The client_private_key of this NSXTManagerDataSourceRequest.
        :type: str
        """

        self._client_private_key = client_private_key

    @property
    def ds_sub_type(self):
        """
        Gets the ds_sub_type of this NSXTManagerDataSourceRequest.
        Data source sub type

        :return: The ds_sub_type of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._ds_sub_type

    @ds_sub_type.setter
    def ds_sub_type(self, ds_sub_type):
        """
        Sets the ds_sub_type of this NSXTManagerDataSourceRequest.
        Data source sub type

        :param ds_sub_type: The ds_sub_type of this NSXTManagerDataSourceRequest.
        :type: str
        """

        self._ds_sub_type = ds_sub_type

    @property
    def tags(self):
        """
        Gets the tags of this NSXTManagerDataSourceRequest.

        :return: The tags of this NSXTManagerDataSourceRequest.
        :rtype: list[LocalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this NSXTManagerDataSourceRequest.

        :param tags: The tags of this NSXTManagerDataSourceRequest.
        :type: list[LocalTag]
        """

        self._tags = tags

    @property
    def enable_ds_associated_tags(self):
        """
        Gets the enable_ds_associated_tags of this NSXTManagerDataSourceRequest.

        :return: The enable_ds_associated_tags of this NSXTManagerDataSourceRequest.
        :rtype: bool
        """
        return self._enable_ds_associated_tags

    @enable_ds_associated_tags.setter
    def enable_ds_associated_tags(self, enable_ds_associated_tags):
        """
        Sets the enable_ds_associated_tags of this NSXTManagerDataSourceRequest.

        :param enable_ds_associated_tags: The enable_ds_associated_tags of this NSXTManagerDataSourceRequest.
        :type: bool
        """

        self._enable_ds_associated_tags = enable_ds_associated_tags

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, NSXTManagerDataSourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other