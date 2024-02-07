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


class IpRange(object):
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
        'subnet': 'str',
        'ip_address_range': 'IpAddressRange'
    }

    attribute_map = {
        'subnet': 'subnet',
        'ip_address_range': 'ip_address_range'
    }

    def __init__(self, subnet=None, ip_address_range=None):
        """
        IpRange - a model defined in Swagger
        """

        self._subnet = None
        self._ip_address_range = None

        if subnet is not None:
          self.subnet = subnet
        if ip_address_range is not None:
          self.ip_address_range = ip_address_range

    @property
    def subnet(self):
        """
        Gets the subnet of this IpRange.

        :return: The subnet of this IpRange.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """
        Sets the subnet of this IpRange.

        :param subnet: The subnet of this IpRange.
        :type: str
        """

        self._subnet = subnet

    @property
    def ip_address_range(self):
        """
        Gets the ip_address_range of this IpRange.

        :return: The ip_address_range of this IpRange.
        :rtype: IpAddressRange
        """
        return self._ip_address_range

    @ip_address_range.setter
    def ip_address_range(self, ip_address_range):
        """
        Sets the ip_address_range of this IpRange.

        :param ip_address_range: The ip_address_range of this IpRange.
        :type: IpAddressRange
        """

        self._ip_address_range = ip_address_range

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
        if not isinstance(other, IpRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other