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


class CurrentLicenses(object):
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
        'to_remove': 'list[VRNILicense]',
        'to_retain': 'list[VRNILicense]'
    }

    attribute_map = {
        'to_remove': 'toRemove',
        'to_retain': 'toRetain'
    }

    def __init__(self, to_remove=None, to_retain=None):
        """
        CurrentLicenses - a model defined in Swagger
        """

        self._to_remove = None
        self._to_retain = None

        if to_remove is not None:
          self.to_remove = to_remove
        if to_retain is not None:
          self.to_retain = to_retain

    @property
    def to_remove(self):
        """
        Gets the to_remove of this CurrentLicenses.
        List of licenses that will be removed. This list will have Socket based licenses when Core based license is added.

        :return: The to_remove of this CurrentLicenses.
        :rtype: list[VRNILicense]
        """
        return self._to_remove

    @to_remove.setter
    def to_remove(self, to_remove):
        """
        Sets the to_remove of this CurrentLicenses.
        List of licenses that will be removed. This list will have Socket based licenses when Core based license is added.

        :param to_remove: The to_remove of this CurrentLicenses.
        :type: list[VRNILicense]
        """

        self._to_remove = to_remove

    @property
    def to_retain(self):
        """
        Gets the to_retain of this CurrentLicenses.
        List of licenses that will be retained.

        :return: The to_retain of this CurrentLicenses.
        :rtype: list[VRNILicense]
        """
        return self._to_retain

    @to_retain.setter
    def to_retain(self, to_retain):
        """
        Sets the to_retain of this CurrentLicenses.
        List of licenses that will be retained.

        :param to_retain: The to_retain of this CurrentLicenses.
        :type: list[VRNILicense]
        """

        self._to_retain = to_retain

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
        if not isinstance(other, CurrentLicenses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other