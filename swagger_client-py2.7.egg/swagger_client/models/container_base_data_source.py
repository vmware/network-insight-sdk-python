# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ContainerBaseDataSource(object):
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
        'manager_id': 'str',
        'credentials': 'K8SCredentials'
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
        'manager_id': 'manager_id',
        'credentials': 'credentials'
    }

    def __init__(self, entity_id=None, entity_type=None, ip=None, fqdn=None, proxy_id=None, nickname=None, enabled=True, notes=None, manager_id=None, credentials=None):
        """
        ContainerBaseDataSource - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
        self._ip = None
        self._fqdn = None
        self._proxy_id = None
        self._nickname = None
        self._enabled = None
        self._notes = None
        self._manager_id = None
        self._credentials = None

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
        if manager_id is not None:
          self.manager_id = manager_id
        if credentials is not None:
          self.credentials = credentials

    @property
    def entity_id(self):
        """
        Gets the entity_id of this ContainerBaseDataSource.

        :return: The entity_id of this ContainerBaseDataSource.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this ContainerBaseDataSource.

        :param entity_id: The entity_id of this ContainerBaseDataSource.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this ContainerBaseDataSource.

        :return: The entity_type of this ContainerBaseDataSource.
        :rtype: DataSourceType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this ContainerBaseDataSource.

        :param entity_type: The entity_type of this ContainerBaseDataSource.
        :type: DataSourceType
        """

        self._entity_type = entity_type

    @property
    def ip(self):
        """
        Gets the ip of this ContainerBaseDataSource.

        :return: The ip of this ContainerBaseDataSource.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this ContainerBaseDataSource.

        :param ip: The ip of this ContainerBaseDataSource.
        :type: str
        """

        self._ip = ip

    @property
    def fqdn(self):
        """
        Gets the fqdn of this ContainerBaseDataSource.

        :return: The fqdn of this ContainerBaseDataSource.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this ContainerBaseDataSource.

        :param fqdn: The fqdn of this ContainerBaseDataSource.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def proxy_id(self):
        """
        Gets the proxy_id of this ContainerBaseDataSource.
        proxy vm which should register this vcenter

        :return: The proxy_id of this ContainerBaseDataSource.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """
        Sets the proxy_id of this ContainerBaseDataSource.
        proxy vm which should register this vcenter

        :param proxy_id: The proxy_id of this ContainerBaseDataSource.
        :type: str
        """

        self._proxy_id = proxy_id

    @property
    def nickname(self):
        """
        Gets the nickname of this ContainerBaseDataSource.

        :return: The nickname of this ContainerBaseDataSource.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this ContainerBaseDataSource.

        :param nickname: The nickname of this ContainerBaseDataSource.
        :type: str
        """

        self._nickname = nickname

    @property
    def enabled(self):
        """
        Gets the enabled of this ContainerBaseDataSource.

        :return: The enabled of this ContainerBaseDataSource.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ContainerBaseDataSource.

        :param enabled: The enabled of this ContainerBaseDataSource.
        :type: bool
        """

        self._enabled = enabled

    @property
    def notes(self):
        """
        Gets the notes of this ContainerBaseDataSource.

        :return: The notes of this ContainerBaseDataSource.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this ContainerBaseDataSource.

        :param notes: The notes of this ContainerBaseDataSource.
        :type: str
        """

        self._notes = notes

    @property
    def manager_id(self):
        """
        Gets the manager_id of this ContainerBaseDataSource.
        Associated nsxt data source entity Id

        :return: The manager_id of this ContainerBaseDataSource.
        :rtype: str
        """
        return self._manager_id

    @manager_id.setter
    def manager_id(self, manager_id):
        """
        Sets the manager_id of this ContainerBaseDataSource.
        Associated nsxt data source entity Id

        :param manager_id: The manager_id of this ContainerBaseDataSource.
        :type: str
        """

        self._manager_id = manager_id

    @property
    def credentials(self):
        """
        Gets the credentials of this ContainerBaseDataSource.

        :return: The credentials of this ContainerBaseDataSource.
        :rtype: K8SCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this ContainerBaseDataSource.

        :param credentials: The credentials of this ContainerBaseDataSource.
        :type: K8SCredentials
        """

        self._credentials = credentials

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
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
        if not isinstance(other, ContainerBaseDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
