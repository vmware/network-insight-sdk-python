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


class ApplicationUpdate(object):
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
        'basic_update_info': 'BasicUpdateInfo',
        'tiers': 'list[TierUpdate]'
    }

    attribute_map = {
        'basic_update_info': 'basic_update_info',
        'tiers': 'tiers'
    }

    def __init__(self, basic_update_info=None, tiers=None):
        """
        ApplicationUpdate - a model defined in Swagger
        """

        self._basic_update_info = None
        self._tiers = None

        if basic_update_info is not None:
          self.basic_update_info = basic_update_info
        if tiers is not None:
          self.tiers = tiers

    @property
    def basic_update_info(self):
        """
        Gets the basic_update_info of this ApplicationUpdate.

        :return: The basic_update_info of this ApplicationUpdate.
        :rtype: BasicUpdateInfo
        """
        return self._basic_update_info

    @basic_update_info.setter
    def basic_update_info(self, basic_update_info):
        """
        Sets the basic_update_info of this ApplicationUpdate.

        :param basic_update_info: The basic_update_info of this ApplicationUpdate.
        :type: BasicUpdateInfo
        """

        self._basic_update_info = basic_update_info

    @property
    def tiers(self):
        """
        Gets the tiers of this ApplicationUpdate.

        :return: The tiers of this ApplicationUpdate.
        :rtype: list[TierUpdate]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """
        Sets the tiers of this ApplicationUpdate.

        :param tiers: The tiers of this ApplicationUpdate.
        :type: list[TierUpdate]
        """

        self._tiers = tiers

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
        if not isinstance(other, ApplicationUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other