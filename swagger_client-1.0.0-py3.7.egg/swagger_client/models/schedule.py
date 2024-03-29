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


class Schedule(object):
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
        'type': 'ScheduleType',
        'value': 'ScheduleValue'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, type=None, value=None):
        """
        Schedule - a model defined in Swagger
        """

        self._type = None
        self._value = None

        if type is not None:
          self.type = type
        if value is not None:
          self.value = value

    @property
    def type(self):
        """
        Gets the type of this Schedule.

        :return: The type of this Schedule.
        :rtype: ScheduleType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Schedule.

        :param type: The type of this Schedule.
        :type: ScheduleType
        """

        self._type = type

    @property
    def value(self):
        """
        Gets the value of this Schedule.

        :return: The value of this Schedule.
        :rtype: ScheduleValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Schedule.

        :param value: The value of this Schedule.
        :type: ScheduleValue
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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
