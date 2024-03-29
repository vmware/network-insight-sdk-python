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


class CustomDashboardPreference(object):
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
        'preference': 'list[str]'
    }

    attribute_map = {
        'preference': 'preference'
    }

    def __init__(self, preference=None):
        """
        CustomDashboardPreference - a model defined in Swagger
        """

        self._preference = None

        if preference is not None:
          self.preference = preference

    @property
    def preference(self):
        """
        Gets the preference of this CustomDashboardPreference.
        Custom dashboard model keys/OOTB dashboard ids in order of preference upto a maximum of 5. GET_STARTED is the only OOTB dashboard supported.

        :return: The preference of this CustomDashboardPreference.
        :rtype: list[str]
        """
        return self._preference

    @preference.setter
    def preference(self, preference):
        """
        Sets the preference of this CustomDashboardPreference.
        Custom dashboard model keys/OOTB dashboard ids in order of preference upto a maximum of 5. GET_STARTED is the only OOTB dashboard supported.

        :param preference: The preference of this CustomDashboardPreference.
        :type: list[str]
        """

        self._preference = preference

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
        if not isinstance(other, CustomDashboardPreference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
