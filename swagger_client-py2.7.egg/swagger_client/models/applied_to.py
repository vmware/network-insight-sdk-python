# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppliedTo(object):
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
        'referred_entity': 'EntityId',
        'name': 'str',
        'value': 'str',
        'vendor_type': 'str'
    }

    attribute_map = {
        'referred_entity': 'referred_entity',
        'name': 'name',
        'value': 'value',
        'vendor_type': 'vendor_type'
    }

    def __init__(self, referred_entity=None, name=None, value=None, vendor_type=None):
        """
        AppliedTo - a model defined in Swagger
        """

        self._referred_entity = None
        self._name = None
        self._value = None
        self._vendor_type = None

        if referred_entity is not None:
          self.referred_entity = referred_entity
        if name is not None:
          self.name = name
        if value is not None:
          self.value = value
        if vendor_type is not None:
          self.vendor_type = vendor_type

    @property
    def referred_entity(self):
        """
        Gets the referred_entity of this AppliedTo.

        :return: The referred_entity of this AppliedTo.
        :rtype: EntityId
        """
        return self._referred_entity

    @referred_entity.setter
    def referred_entity(self, referred_entity):
        """
        Sets the referred_entity of this AppliedTo.

        :param referred_entity: The referred_entity of this AppliedTo.
        :type: EntityId
        """

        self._referred_entity = referred_entity

    @property
    def name(self):
        """
        Gets the name of this AppliedTo.

        :return: The name of this AppliedTo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AppliedTo.

        :param name: The name of this AppliedTo.
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """
        Gets the value of this AppliedTo.

        :return: The value of this AppliedTo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AppliedTo.

        :param value: The value of this AppliedTo.
        :type: str
        """

        self._value = value

    @property
    def vendor_type(self):
        """
        Gets the vendor_type of this AppliedTo.

        :return: The vendor_type of this AppliedTo.
        :rtype: str
        """
        return self._vendor_type

    @vendor_type.setter
    def vendor_type(self, vendor_type):
        """
        Sets the vendor_type of this AppliedTo.

        :param vendor_type: The vendor_type of this AppliedTo.
        :type: str
        """

        self._vendor_type = vendor_type

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
        if not isinstance(other, AppliedTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
