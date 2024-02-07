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


class BackupSchedule(object):
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
        'enable': 'bool',
        'schedule_period': 'BackupSchedulePeriod',
        'minute': 'int',
        'hour': 'int',
        'day_of_week': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'schedule_period': 'schedule_period',
        'minute': 'minute',
        'hour': 'hour',
        'day_of_week': 'day_of_week'
    }

    def __init__(self, enable=True, schedule_period=None, minute=None, hour=None, day_of_week=None):
        """
        BackupSchedule - a model defined in Swagger
        """

        self._enable = None
        self._schedule_period = None
        self._minute = None
        self._hour = None
        self._day_of_week = None

        if enable is not None:
          self.enable = enable
        if schedule_period is not None:
          self.schedule_period = schedule_period
        if minute is not None:
          self.minute = minute
        if hour is not None:
          self.hour = hour
        if day_of_week is not None:
          self.day_of_week = day_of_week

    @property
    def enable(self):
        """
        Gets the enable of this BackupSchedule.
        True, to enable scheduled backup

        :return: The enable of this BackupSchedule.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """
        Sets the enable of this BackupSchedule.
        True, to enable scheduled backup

        :param enable: The enable of this BackupSchedule.
        :type: bool
        """

        self._enable = enable

    @property
    def schedule_period(self):
        """
        Gets the schedule_period of this BackupSchedule.

        :return: The schedule_period of this BackupSchedule.
        :rtype: BackupSchedulePeriod
        """
        return self._schedule_period

    @schedule_period.setter
    def schedule_period(self, schedule_period):
        """
        Sets the schedule_period of this BackupSchedule.

        :param schedule_period: The schedule_period of this BackupSchedule.
        :type: BackupSchedulePeriod
        """

        self._schedule_period = schedule_period

    @property
    def minute(self):
        """
        Gets the minute of this BackupSchedule.
        The minute at which backup needs to run (permitted values 0 - 59)

        :return: The minute of this BackupSchedule.
        :rtype: int
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        """
        Sets the minute of this BackupSchedule.
        The minute at which backup needs to run (permitted values 0 - 59)

        :param minute: The minute of this BackupSchedule.
        :type: int
        """

        self._minute = minute

    @property
    def hour(self):
        """
        Gets the hour of this BackupSchedule.
        The hour at which backup needs to run (permitted values 0 - 23)

        :return: The hour of this BackupSchedule.
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """
        Sets the hour of this BackupSchedule.
        The hour at which backup needs to run (permitted values 0 - 23)

        :param hour: The hour of this BackupSchedule.
        :type: int
        """

        self._hour = hour

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this BackupSchedule.
        The day of the week when backup to be scheduled (permitted values 1{Sunday} - 7{Saturday})

        :return: The day_of_week of this BackupSchedule.
        :rtype: int
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this BackupSchedule.
        The day of the week when backup to be scheduled (permitted values 1{Sunday} - 7{Saturday})

        :param day_of_week: The day_of_week of this BackupSchedule.
        :type: int
        """

        self._day_of_week = day_of_week

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
        if not isinstance(other, BackupSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other