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


class IntentNotifySchedule(object):
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
        'type': 'str',
        'period_in_ms': 'int',
        'start_timestamp': 'int'
    }

    attribute_map = {
        'type': 'type',
        'period_in_ms': 'periodInMS',
        'start_timestamp': 'startTimestamp'
    }

    def __init__(self, type=None, period_in_ms=None, start_timestamp=None):
        """
        IntentNotifySchedule - a model defined in Swagger
        """

        self._type = None
        self._period_in_ms = None
        self._start_timestamp = None

        if type is not None:
          self.type = type
        if period_in_ms is not None:
          self.period_in_ms = period_in_ms
        if start_timestamp is not None:
          self.start_timestamp = start_timestamp

    @property
    def type(self):
        """
        Gets the type of this IntentNotifySchedule.
        Intent type

        :return: The type of this IntentNotifySchedule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IntentNotifySchedule.
        Intent type

        :param type: The type of this IntentNotifySchedule.
        :type: str
        """
        allowed_values = ["PERIODIC", "NONE"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def period_in_ms(self):
        """
        Gets the period_in_ms of this IntentNotifySchedule.
        Intent period

        :return: The period_in_ms of this IntentNotifySchedule.
        :rtype: int
        """
        return self._period_in_ms

    @period_in_ms.setter
    def period_in_ms(self, period_in_ms):
        """
        Sets the period_in_ms of this IntentNotifySchedule.
        Intent period

        :param period_in_ms: The period_in_ms of this IntentNotifySchedule.
        :type: int
        """

        self._period_in_ms = period_in_ms

    @property
    def start_timestamp(self):
        """
        Gets the start_timestamp of this IntentNotifySchedule.
        Intent time stamp

        :return: The start_timestamp of this IntentNotifySchedule.
        :rtype: int
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """
        Sets the start_timestamp of this IntentNotifySchedule.
        Intent time stamp

        :param start_timestamp: The start_timestamp of this IntentNotifySchedule.
        :type: int
        """

        self._start_timestamp = start_timestamp

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
        if not isinstance(other, IntentNotifySchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other