# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NSXTManagerDataSource(object):
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
        'entity_id': 'str',
        'entity_type': 'DataSourceType',
        'ip': 'str',
        'fqdn': 'str',
        'proxy_id': 'str',
        'nickname': 'str',
        'enabled': 'bool',
        'notes': 'str',
        'credentials': 'PasswordCredentials',
        'ipfix_enabled': 'bool',
        'latency_enabled': 'bool',
        'nsxi_enabled': 'bool'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'ip': 'ip',
        'fqdn': 'fqdn',
        'proxy_id': 'proxy_id',
        'nickname': 'nickname',
        'enabled': 'enabled',
        'notes': 'notes',
        'credentials': 'credentials',
        'ipfix_enabled': 'ipfix_enabled',
        'latency_enabled': 'latency_enabled',
        'nsxi_enabled': 'nsxi_enabled'
    }

    def __init__(self, entity_id=None, entity_type=None, ip=None, fqdn=None, proxy_id=None, nickname=None, enabled=True, notes=None, credentials=None, ipfix_enabled=False, latency_enabled=False, nsxi_enabled=False):
        """
        NSXTManagerDataSource - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
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

        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if ip is not None:
          self.ip = ip
        if fqdn is not None:
          self.fqdn = fqdn
        if proxy_id is not None:
          self.proxy_id = proxy_id
        if nickname is not None:
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

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSXTManagerDataSource.

        :return: The entity_id of this NSXTManagerDataSource.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSXTManagerDataSource.

        :param entity_id: The entity_id of this NSXTManagerDataSource.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSXTManagerDataSource.

        :return: The entity_type of this NSXTManagerDataSource.
        :rtype: DataSourceType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSXTManagerDataSource.

        :param entity_type: The entity_type of this NSXTManagerDataSource.
        :type: DataSourceType
        """

        self._entity_type = entity_type

    @property
    def ip(self):
        """
        Gets the ip of this NSXTManagerDataSource.

        :return: The ip of this NSXTManagerDataSource.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this NSXTManagerDataSource.

        :param ip: The ip of this NSXTManagerDataSource.
        :type: str
        """

        self._ip = ip

    @property
    def fqdn(self):
        """
        Gets the fqdn of this NSXTManagerDataSource.

        :return: The fqdn of this NSXTManagerDataSource.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this NSXTManagerDataSource.

        :param fqdn: The fqdn of this NSXTManagerDataSource.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def proxy_id(self):
        """
        Gets the proxy_id of this NSXTManagerDataSource.
        proxy vm which should register this vcenter

        :return: The proxy_id of this NSXTManagerDataSource.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """
        Sets the proxy_id of this NSXTManagerDataSource.
        proxy vm which should register this vcenter

        :param proxy_id: The proxy_id of this NSXTManagerDataSource.
        :type: str
        """

        self._proxy_id = proxy_id

    @property
    def nickname(self):
        """
        Gets the nickname of this NSXTManagerDataSource.

        :return: The nickname of this NSXTManagerDataSource.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this NSXTManagerDataSource.

        :param nickname: The nickname of this NSXTManagerDataSource.
        :type: str
        """

        self._nickname = nickname

    @property
    def enabled(self):
        """
        Gets the enabled of this NSXTManagerDataSource.

        :return: The enabled of this NSXTManagerDataSource.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this NSXTManagerDataSource.

        :param enabled: The enabled of this NSXTManagerDataSource.
        :type: bool
        """

        self._enabled = enabled

    @property
    def notes(self):
        """
        Gets the notes of this NSXTManagerDataSource.

        :return: The notes of this NSXTManagerDataSource.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this NSXTManagerDataSource.

        :param notes: The notes of this NSXTManagerDataSource.
        :type: str
        """

        self._notes = notes

    @property
    def credentials(self):
        """
        Gets the credentials of this NSXTManagerDataSource.

        :return: The credentials of this NSXTManagerDataSource.
        :rtype: PasswordCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this NSXTManagerDataSource.

        :param credentials: The credentials of this NSXTManagerDataSource.
        :type: PasswordCredentials
        """

        self._credentials = credentials

    @property
    def ipfix_enabled(self):
        """
        Gets the ipfix_enabled of this NSXTManagerDataSource.

        :return: The ipfix_enabled of this NSXTManagerDataSource.
        :rtype: bool
        """
        return self._ipfix_enabled

    @ipfix_enabled.setter
    def ipfix_enabled(self, ipfix_enabled):
        """
        Sets the ipfix_enabled of this NSXTManagerDataSource.

        :param ipfix_enabled: The ipfix_enabled of this NSXTManagerDataSource.
        :type: bool
        """

        self._ipfix_enabled = ipfix_enabled

    @property
    def latency_enabled(self):
        """
        Gets the latency_enabled of this NSXTManagerDataSource.

        :return: The latency_enabled of this NSXTManagerDataSource.
        :rtype: bool
        """
        return self._latency_enabled

    @latency_enabled.setter
    def latency_enabled(self, latency_enabled):
        """
        Sets the latency_enabled of this NSXTManagerDataSource.

        :param latency_enabled: The latency_enabled of this NSXTManagerDataSource.
        :type: bool
        """

        self._latency_enabled = latency_enabled

    @property
    def nsxi_enabled(self):
        """
        Gets the nsxi_enabled of this NSXTManagerDataSource.

        :return: The nsxi_enabled of this NSXTManagerDataSource.
        :rtype: bool
        """
        return self._nsxi_enabled

    @nsxi_enabled.setter
    def nsxi_enabled(self, nsxi_enabled):
        """
        Sets the nsxi_enabled of this NSXTManagerDataSource.

        :param nsxi_enabled: The nsxi_enabled of this NSXTManagerDataSource.
        :type: bool
        """

        self._nsxi_enabled = nsxi_enabled

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
        if not isinstance(other, NSXTManagerDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
