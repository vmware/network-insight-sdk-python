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


class SyslogStatus(object):
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
        'enabled': 'bool',
        'change_time': 'int',
        'message': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'change_time': 'change_time',
        'message': 'message'
    }

    def __init__(self, enabled=None, change_time=None, message=None):
        """
        SyslogStatus - a model defined in Swagger
        """

        self._enabled = None
        self._change_time = None
        self._message = None

        if enabled is not None:
          self.enabled = enabled
        if change_time is not None:
          self.change_time = change_time
        if message is not None:
          self.message = message

    @property
    def enabled(self):
        """
        Gets the enabled of this SyslogStatus.
        Whether Syslog functionality is enabled or disabled

        :return: The enabled of this SyslogStatus.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SyslogStatus.
        Whether Syslog functionality is enabled or disabled

        :param enabled: The enabled of this SyslogStatus.
        :type: bool
        """

        self._enabled = enabled

    @property
    def change_time(self):
        """
        Gets the change_time of this SyslogStatus.
        Change time of the syslog status

        :return: The change_time of this SyslogStatus.
        :rtype: int
        """
        return self._change_time

    @change_time.setter
    def change_time(self, change_time):
        """
        Sets the change_time of this SyslogStatus.
        Change time of the syslog status

        :param change_time: The change_time of this SyslogStatus.
        :type: int
        """

        self._change_time = change_time

    @property
    def message(self):
        """
        Gets the message of this SyslogStatus.
        Success in sending enable/disable log

        :return: The message of this SyslogStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this SyslogStatus.
        Success in sending enable/disable log

        :param message: The message of this SyslogStatus.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, SyslogStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other