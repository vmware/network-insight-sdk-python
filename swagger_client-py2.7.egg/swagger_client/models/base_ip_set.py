# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BaseIPSet(object):
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
        'ip_addresses': 'list[IpV4Address]',
        'ip_ranges': 'list[IpAddressRange]',
        'ip_numeric_ranges': 'list[IpNumericRange]',
        'parent_security_groups': 'list[Reference]',
        'direct_source_rules': 'list[RuleSet]',
        'direct_destination_rules': 'list[RuleSet]',
        'indirect_source_rules': 'list[RuleSet]',
        'indirect_destination_rules': 'list[RuleSet]',
        'vendor_id': 'str',
        'vendor': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'ip_addresses': 'ip_addresses',
        'ip_ranges': 'ip_ranges',
        'ip_numeric_ranges': 'ip_numeric_ranges',
        'parent_security_groups': 'parent_security_groups',
        'direct_source_rules': 'direct_source_rules',
        'direct_destination_rules': 'direct_destination_rules',
        'indirect_source_rules': 'indirect_source_rules',
        'indirect_destination_rules': 'indirect_destination_rules',
        'vendor_id': 'vendor_id',
        'vendor': 'vendor'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, ip_addresses=None, ip_ranges=None, ip_numeric_ranges=None, parent_security_groups=None, direct_source_rules=None, direct_destination_rules=None, indirect_source_rules=None, indirect_destination_rules=None, vendor_id=None, vendor=None):
        """
        BaseIPSet - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._ip_addresses = None
        self._ip_ranges = None
        self._ip_numeric_ranges = None
        self._parent_security_groups = None
        self._direct_source_rules = None
        self._direct_destination_rules = None
        self._indirect_source_rules = None
        self._indirect_destination_rules = None
        self._vendor_id = None
        self._vendor = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if ip_addresses is not None:
          self.ip_addresses = ip_addresses
        if ip_ranges is not None:
          self.ip_ranges = ip_ranges
        if ip_numeric_ranges is not None:
          self.ip_numeric_ranges = ip_numeric_ranges
        if parent_security_groups is not None:
          self.parent_security_groups = parent_security_groups
        if direct_source_rules is not None:
          self.direct_source_rules = direct_source_rules
        if direct_destination_rules is not None:
          self.direct_destination_rules = direct_destination_rules
        if indirect_source_rules is not None:
          self.indirect_source_rules = indirect_source_rules
        if indirect_destination_rules is not None:
          self.indirect_destination_rules = indirect_destination_rules
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if vendor is not None:
          self.vendor = vendor

    @property
    def entity_id(self):
        """
        Gets the entity_id of this BaseIPSet.

        :return: The entity_id of this BaseIPSet.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this BaseIPSet.

        :param entity_id: The entity_id of this BaseIPSet.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this BaseIPSet.

        :return: The name of this BaseIPSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BaseIPSet.

        :param name: The name of this BaseIPSet.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this BaseIPSet.

        :return: The entity_type of this BaseIPSet.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this BaseIPSet.

        :param entity_type: The entity_type of this BaseIPSet.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def ip_addresses(self):
        """
        Gets the ip_addresses of this BaseIPSet.

        :return: The ip_addresses of this BaseIPSet.
        :rtype: list[IpV4Address]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this BaseIPSet.

        :param ip_addresses: The ip_addresses of this BaseIPSet.
        :type: list[IpV4Address]
        """

        self._ip_addresses = ip_addresses

    @property
    def ip_ranges(self):
        """
        Gets the ip_ranges of this BaseIPSet.

        :return: The ip_ranges of this BaseIPSet.
        :rtype: list[IpAddressRange]
        """
        return self._ip_ranges

    @ip_ranges.setter
    def ip_ranges(self, ip_ranges):
        """
        Sets the ip_ranges of this BaseIPSet.

        :param ip_ranges: The ip_ranges of this BaseIPSet.
        :type: list[IpAddressRange]
        """

        self._ip_ranges = ip_ranges

    @property
    def ip_numeric_ranges(self):
        """
        Gets the ip_numeric_ranges of this BaseIPSet.

        :return: The ip_numeric_ranges of this BaseIPSet.
        :rtype: list[IpNumericRange]
        """
        return self._ip_numeric_ranges

    @ip_numeric_ranges.setter
    def ip_numeric_ranges(self, ip_numeric_ranges):
        """
        Sets the ip_numeric_ranges of this BaseIPSet.

        :param ip_numeric_ranges: The ip_numeric_ranges of this BaseIPSet.
        :type: list[IpNumericRange]
        """

        self._ip_numeric_ranges = ip_numeric_ranges

    @property
    def parent_security_groups(self):
        """
        Gets the parent_security_groups of this BaseIPSet.

        :return: The parent_security_groups of this BaseIPSet.
        :rtype: list[Reference]
        """
        return self._parent_security_groups

    @parent_security_groups.setter
    def parent_security_groups(self, parent_security_groups):
        """
        Sets the parent_security_groups of this BaseIPSet.

        :param parent_security_groups: The parent_security_groups of this BaseIPSet.
        :type: list[Reference]
        """

        self._parent_security_groups = parent_security_groups

    @property
    def direct_source_rules(self):
        """
        Gets the direct_source_rules of this BaseIPSet.

        :return: The direct_source_rules of this BaseIPSet.
        :rtype: list[RuleSet]
        """
        return self._direct_source_rules

    @direct_source_rules.setter
    def direct_source_rules(self, direct_source_rules):
        """
        Sets the direct_source_rules of this BaseIPSet.

        :param direct_source_rules: The direct_source_rules of this BaseIPSet.
        :type: list[RuleSet]
        """

        self._direct_source_rules = direct_source_rules

    @property
    def direct_destination_rules(self):
        """
        Gets the direct_destination_rules of this BaseIPSet.

        :return: The direct_destination_rules of this BaseIPSet.
        :rtype: list[RuleSet]
        """
        return self._direct_destination_rules

    @direct_destination_rules.setter
    def direct_destination_rules(self, direct_destination_rules):
        """
        Sets the direct_destination_rules of this BaseIPSet.

        :param direct_destination_rules: The direct_destination_rules of this BaseIPSet.
        :type: list[RuleSet]
        """

        self._direct_destination_rules = direct_destination_rules

    @property
    def indirect_source_rules(self):
        """
        Gets the indirect_source_rules of this BaseIPSet.

        :return: The indirect_source_rules of this BaseIPSet.
        :rtype: list[RuleSet]
        """
        return self._indirect_source_rules

    @indirect_source_rules.setter
    def indirect_source_rules(self, indirect_source_rules):
        """
        Sets the indirect_source_rules of this BaseIPSet.

        :param indirect_source_rules: The indirect_source_rules of this BaseIPSet.
        :type: list[RuleSet]
        """

        self._indirect_source_rules = indirect_source_rules

    @property
    def indirect_destination_rules(self):
        """
        Gets the indirect_destination_rules of this BaseIPSet.

        :return: The indirect_destination_rules of this BaseIPSet.
        :rtype: list[RuleSet]
        """
        return self._indirect_destination_rules

    @indirect_destination_rules.setter
    def indirect_destination_rules(self, indirect_destination_rules):
        """
        Sets the indirect_destination_rules of this BaseIPSet.

        :param indirect_destination_rules: The indirect_destination_rules of this BaseIPSet.
        :type: list[RuleSet]
        """

        self._indirect_destination_rules = indirect_destination_rules

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this BaseIPSet.

        :return: The vendor_id of this BaseIPSet.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this BaseIPSet.

        :param vendor_id: The vendor_id of this BaseIPSet.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def vendor(self):
        """
        Gets the vendor of this BaseIPSet.

        :return: The vendor of this BaseIPSet.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this BaseIPSet.

        :param vendor: The vendor of this BaseIPSet.
        :type: str
        """

        self._vendor = vendor

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
        if not isinstance(other, BaseIPSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
