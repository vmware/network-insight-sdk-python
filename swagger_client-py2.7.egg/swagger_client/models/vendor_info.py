# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 6.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VendorInfo(object):
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
        'vendor_ids': 'list[VendorId]',
        'manager': 'Reference'
    }

    attribute_map = {
        'vendor_ids': 'vendor_ids',
        'manager': 'manager'
    }

    def __init__(self, vendor_ids=None, manager=None):
        """
        VendorInfo - a model defined in Swagger
        """

        self._vendor_ids = None
        self._manager = None

        if vendor_ids is not None:
          self.vendor_ids = vendor_ids
        if manager is not None:
          self.manager = manager

    @property
    def vendor_ids(self):
        """
        Gets the vendor_ids of this VendorInfo.

        :return: The vendor_ids of this VendorInfo.
        :rtype: list[VendorId]
        """
        return self._vendor_ids

    @vendor_ids.setter
    def vendor_ids(self, vendor_ids):
        """
        Sets the vendor_ids of this VendorInfo.

        :param vendor_ids: The vendor_ids of this VendorInfo.
        :type: list[VendorId]
        """

        self._vendor_ids = vendor_ids

    @property
    def manager(self):
        """
        Gets the manager of this VendorInfo.

        :return: The manager of this VendorInfo.
        :rtype: Reference
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this VendorInfo.

        :param manager: The manager of this VendorInfo.
        :type: Reference
        """

        self._manager = manager

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
        if not isinstance(other, VendorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
