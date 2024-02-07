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


class BucketValue(object):
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
        'field': 'str',
        'value': 'str'
    }

    attribute_map = {
        'field': 'field',
        'value': 'value'
    }

    def __init__(self, field=None, value=None):
        """
        BucketValue - a model defined in Swagger
        """

        self._field = None
        self._value = None

        if field is not None:
          self.field = field
        if value is not None:
          self.value = value

    @property
    def field(self):
        """
        Gets the field of this BucketValue.

        :return: The field of this BucketValue.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this BucketValue.

        :param field: The field of this BucketValue.
        :type: str
        """

        self._field = field

    @property
    def value(self):
        """
        Gets the value of this BucketValue.

        :return: The value of this BucketValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this BucketValue.

        :param value: The value of this BucketValue.
        :type: str
        """

        self._value = value

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
        if not isinstance(other, BucketValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other