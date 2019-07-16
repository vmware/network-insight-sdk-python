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


class NSXVManager(object):
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
        'name': 'str',
        'entity_type': 'EntityType',
        'fqdn': 'str',
        'ip_address': 'IpV4Address',
        'version': 'str',
        'primary_nsx_manager': 'Reference',
        'vm': 'Reference',
        'role': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'fqdn': 'fqdn',
        'ip_address': 'ip_address',
        'version': 'version',
        'primary_nsx_manager': 'primary_nsx_manager',
        'vm': 'vm',
        'role': 'role'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, fqdn=None, ip_address=None, version=None, primary_nsx_manager=None, vm=None, role=None):
        """
        NSXVManager - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._fqdn = None
        self._ip_address = None
        self._version = None
        self._primary_nsx_manager = None
        self._vm = None
        self._role = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if fqdn is not None:
          self.fqdn = fqdn
        if ip_address is not None:
          self.ip_address = ip_address
        if version is not None:
          self.version = version
        if primary_nsx_manager is not None:
          self.primary_nsx_manager = primary_nsx_manager
        if vm is not None:
          self.vm = vm
        if role is not None:
          self.role = role

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSXVManager.

        :return: The entity_id of this NSXVManager.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSXVManager.

        :param entity_id: The entity_id of this NSXVManager.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this NSXVManager.

        :return: The name of this NSXVManager.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NSXVManager.

        :param name: The name of this NSXVManager.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSXVManager.

        :return: The entity_type of this NSXVManager.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSXVManager.

        :param entity_type: The entity_type of this NSXVManager.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def fqdn(self):
        """
        Gets the fqdn of this NSXVManager.

        :return: The fqdn of this NSXVManager.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this NSXVManager.

        :param fqdn: The fqdn of this NSXVManager.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def ip_address(self):
        """
        Gets the ip_address of this NSXVManager.

        :return: The ip_address of this NSXVManager.
        :rtype: IpV4Address
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this NSXVManager.

        :param ip_address: The ip_address of this NSXVManager.
        :type: IpV4Address
        """

        self._ip_address = ip_address

    @property
    def version(self):
        """
        Gets the version of this NSXVManager.

        :return: The version of this NSXVManager.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this NSXVManager.

        :param version: The version of this NSXVManager.
        :type: str
        """

        self._version = version

    @property
    def primary_nsx_manager(self):
        """
        Gets the primary_nsx_manager of this NSXVManager.

        :return: The primary_nsx_manager of this NSXVManager.
        :rtype: Reference
        """
        return self._primary_nsx_manager

    @primary_nsx_manager.setter
    def primary_nsx_manager(self, primary_nsx_manager):
        """
        Sets the primary_nsx_manager of this NSXVManager.

        :param primary_nsx_manager: The primary_nsx_manager of this NSXVManager.
        :type: Reference
        """

        self._primary_nsx_manager = primary_nsx_manager

    @property
    def vm(self):
        """
        Gets the vm of this NSXVManager.

        :return: The vm of this NSXVManager.
        :rtype: Reference
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """
        Sets the vm of this NSXVManager.

        :param vm: The vm of this NSXVManager.
        :type: Reference
        """

        self._vm = vm

    @property
    def role(self):
        """
        Gets the role of this NSXVManager.

        :return: The role of this NSXVManager.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this NSXVManager.

        :param role: The role of this NSXVManager.
        :type: str
        """

        self._role = role

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
        if not isinstance(other, NSXVManager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
