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


class SubscriptionResponse(object):
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
        'entity_id': 'str',
        'active': 'bool',
        'event_name': 'str',
        'is_problem': 'bool',
        'severity': 'Severity',
        'search_criteria': 'str',
        'generate_event_criteria': 'GenerateEventCritera',
        'email_frequency': 'EmailFrequency',
        'daily_at_utc': 'str',
        'email_ids': 'list[str]',
        'snmp_trap_entity_ids': 'list[str]',
        'notification_settings': 'list[NotificationSetting]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'active': 'active',
        'event_name': 'event_name',
        'is_problem': 'is_problem',
        'severity': 'severity',
        'search_criteria': 'search_criteria',
        'generate_event_criteria': 'generate_event_criteria',
        'email_frequency': 'email_frequency',
        'daily_at_utc': 'daily_at_utc',
        'email_ids': 'email_ids',
        'snmp_trap_entity_ids': 'snmp_trap_entity_ids',
        'notification_settings': 'notification_settings'
    }

    def __init__(self, entity_id=None, active=None, event_name=None, is_problem=None, severity=None, search_criteria=None, generate_event_criteria=None, email_frequency=None, daily_at_utc=None, email_ids=None, snmp_trap_entity_ids=None, notification_settings=None):
        """
        SubscriptionResponse - a model defined in Swagger
        """

        self._entity_id = None
        self._active = None
        self._event_name = None
        self._is_problem = None
        self._severity = None
        self._search_criteria = None
        self._generate_event_criteria = None
        self._email_frequency = None
        self._daily_at_utc = None
        self._email_ids = None
        self._snmp_trap_entity_ids = None
        self._notification_settings = None

        if entity_id is not None:
          self.entity_id = entity_id
        if active is not None:
          self.active = active
        if event_name is not None:
          self.event_name = event_name
        if is_problem is not None:
          self.is_problem = is_problem
        if severity is not None:
          self.severity = severity
        if search_criteria is not None:
          self.search_criteria = search_criteria
        if generate_event_criteria is not None:
          self.generate_event_criteria = generate_event_criteria
        if email_frequency is not None:
          self.email_frequency = email_frequency
        if daily_at_utc is not None:
          self.daily_at_utc = daily_at_utc
        if email_ids is not None:
          self.email_ids = email_ids
        if snmp_trap_entity_ids is not None:
          self.snmp_trap_entity_ids = snmp_trap_entity_ids
        if notification_settings is not None:
          self.notification_settings = notification_settings

    @property
    def entity_id(self):
        """
        Gets the entity_id of this SubscriptionResponse.

        :return: The entity_id of this SubscriptionResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this SubscriptionResponse.

        :param entity_id: The entity_id of this SubscriptionResponse.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def active(self):
        """
        Gets the active of this SubscriptionResponse.

        :return: The active of this SubscriptionResponse.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this SubscriptionResponse.

        :param active: The active of this SubscriptionResponse.
        :type: bool
        """

        self._active = active

    @property
    def event_name(self):
        """
        Gets the event_name of this SubscriptionResponse.

        :return: The event_name of this SubscriptionResponse.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this SubscriptionResponse.

        :param event_name: The event_name of this SubscriptionResponse.
        :type: str
        """

        self._event_name = event_name

    @property
    def is_problem(self):
        """
        Gets the is_problem of this SubscriptionResponse.

        :return: The is_problem of this SubscriptionResponse.
        :rtype: bool
        """
        return self._is_problem

    @is_problem.setter
    def is_problem(self, is_problem):
        """
        Sets the is_problem of this SubscriptionResponse.

        :param is_problem: The is_problem of this SubscriptionResponse.
        :type: bool
        """

        self._is_problem = is_problem

    @property
    def severity(self):
        """
        Gets the severity of this SubscriptionResponse.

        :return: The severity of this SubscriptionResponse.
        :rtype: Severity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this SubscriptionResponse.

        :param severity: The severity of this SubscriptionResponse.
        :type: Severity
        """

        self._severity = severity

    @property
    def search_criteria(self):
        """
        Gets the search_criteria of this SubscriptionResponse.

        :return: The search_criteria of this SubscriptionResponse.
        :rtype: str
        """
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria):
        """
        Sets the search_criteria of this SubscriptionResponse.

        :param search_criteria: The search_criteria of this SubscriptionResponse.
        :type: str
        """

        self._search_criteria = search_criteria

    @property
    def generate_event_criteria(self):
        """
        Gets the generate_event_criteria of this SubscriptionResponse.

        :return: The generate_event_criteria of this SubscriptionResponse.
        :rtype: GenerateEventCritera
        """
        return self._generate_event_criteria

    @generate_event_criteria.setter
    def generate_event_criteria(self, generate_event_criteria):
        """
        Sets the generate_event_criteria of this SubscriptionResponse.

        :param generate_event_criteria: The generate_event_criteria of this SubscriptionResponse.
        :type: GenerateEventCritera
        """

        self._generate_event_criteria = generate_event_criteria

    @property
    def email_frequency(self):
        """
        Gets the email_frequency of this SubscriptionResponse.

        :return: The email_frequency of this SubscriptionResponse.
        :rtype: EmailFrequency
        """
        return self._email_frequency

    @email_frequency.setter
    def email_frequency(self, email_frequency):
        """
        Sets the email_frequency of this SubscriptionResponse.

        :param email_frequency: The email_frequency of this SubscriptionResponse.
        :type: EmailFrequency
        """

        self._email_frequency = email_frequency

    @property
    def daily_at_utc(self):
        """
        Gets the daily_at_utc of this SubscriptionResponse.

        :return: The daily_at_utc of this SubscriptionResponse.
        :rtype: str
        """
        return self._daily_at_utc

    @daily_at_utc.setter
    def daily_at_utc(self, daily_at_utc):
        """
        Sets the daily_at_utc of this SubscriptionResponse.

        :param daily_at_utc: The daily_at_utc of this SubscriptionResponse.
        :type: str
        """

        self._daily_at_utc = daily_at_utc

    @property
    def email_ids(self):
        """
        Gets the email_ids of this SubscriptionResponse.

        :return: The email_ids of this SubscriptionResponse.
        :rtype: list[str]
        """
        return self._email_ids

    @email_ids.setter
    def email_ids(self, email_ids):
        """
        Sets the email_ids of this SubscriptionResponse.

        :param email_ids: The email_ids of this SubscriptionResponse.
        :type: list[str]
        """

        self._email_ids = email_ids

    @property
    def snmp_trap_entity_ids(self):
        """
        Gets the snmp_trap_entity_ids of this SubscriptionResponse.

        :return: The snmp_trap_entity_ids of this SubscriptionResponse.
        :rtype: list[str]
        """
        return self._snmp_trap_entity_ids

    @snmp_trap_entity_ids.setter
    def snmp_trap_entity_ids(self, snmp_trap_entity_ids):
        """
        Sets the snmp_trap_entity_ids of this SubscriptionResponse.

        :param snmp_trap_entity_ids: The snmp_trap_entity_ids of this SubscriptionResponse.
        :type: list[str]
        """

        self._snmp_trap_entity_ids = snmp_trap_entity_ids

    @property
    def notification_settings(self):
        """
        Gets the notification_settings of this SubscriptionResponse.
        Notifications configured for alerts corresponding to this alert configuration.

        :return: The notification_settings of this SubscriptionResponse.
        :rtype: list[NotificationSetting]
        """
        return self._notification_settings

    @notification_settings.setter
    def notification_settings(self, notification_settings):
        """
        Sets the notification_settings of this SubscriptionResponse.
        Notifications configured for alerts corresponding to this alert configuration.

        :param notification_settings: The notification_settings of this SubscriptionResponse.
        :type: list[NotificationSetting]
        """

        self._notification_settings = notification_settings

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
        if not isinstance(other, SubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
