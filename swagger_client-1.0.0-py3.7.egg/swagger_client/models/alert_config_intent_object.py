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


class AlertConfigIntentObject(object):
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
        'name': 'str',
        'alert_type': 'str',
        'intent_type_id': 'str',
        'filter_rules': 'AlertConfigIntentObjectFilterRules',
        'param_values': 'list[IntentParam]',
        'selected_scope': 'str',
        'description': 'str',
        'enabled': 'bool',
        'severity': 'str',
        'notes': 'str',
        'tags': 'list[str]',
        'notification_settings': 'list[IntentNotification]'
    }

    attribute_map = {
        'name': 'name',
        'alert_type': 'alertType',
        'intent_type_id': 'intentTypeId',
        'filter_rules': 'filterRules',
        'param_values': 'paramValues',
        'selected_scope': 'selected_scope',
        'description': 'description',
        'enabled': 'enabled',
        'severity': 'severity',
        'notes': 'notes',
        'tags': 'tags',
        'notification_settings': 'notificationSettings'
    }

    def __init__(self, name=None, alert_type=None, intent_type_id=None, filter_rules=None, param_values=None, selected_scope=None, description=None, enabled=None, severity=None, notes=None, tags=None, notification_settings=None):
        """
        AlertConfigIntentObject - a model defined in Swagger
        """

        self._name = None
        self._alert_type = None
        self._intent_type_id = None
        self._filter_rules = None
        self._param_values = None
        self._selected_scope = None
        self._description = None
        self._enabled = None
        self._severity = None
        self._notes = None
        self._tags = None
        self._notification_settings = None

        if name is not None:
          self.name = name
        if alert_type is not None:
          self.alert_type = alert_type
        if intent_type_id is not None:
          self.intent_type_id = intent_type_id
        if filter_rules is not None:
          self.filter_rules = filter_rules
        if param_values is not None:
          self.param_values = param_values
        if selected_scope is not None:
          self.selected_scope = selected_scope
        if description is not None:
          self.description = description
        if enabled is not None:
          self.enabled = enabled
        if severity is not None:
          self.severity = severity
        if notes is not None:
          self.notes = notes
        if tags is not None:
          self.tags = tags
        if notification_settings is not None:
          self.notification_settings = notification_settings

    @property
    def name(self):
        """
        Gets the name of this AlertConfigIntentObject.
        Intent name

        :return: The name of this AlertConfigIntentObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AlertConfigIntentObject.
        Intent name

        :param name: The name of this AlertConfigIntentObject.
        :type: str
        """

        self._name = name

    @property
    def alert_type(self):
        """
        Gets the alert_type of this AlertConfigIntentObject.
        Intent type

        :return: The alert_type of this AlertConfigIntentObject.
        :rtype: str
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """
        Sets the alert_type of this AlertConfigIntentObject.
        Intent type

        :param alert_type: The alert_type of this AlertConfigIntentObject.
        :type: str
        """
        allowed_values = ["Intent"]
        if alert_type not in allowed_values:
            raise ValueError(
                "Invalid value for `alert_type` ({0}), must be one of {1}"
                .format(alert_type, allowed_values)
            )

        self._alert_type = alert_type

    @property
    def intent_type_id(self):
        """
        Gets the intent_type_id of this AlertConfigIntentObject.
        Intent type

        :return: The intent_type_id of this AlertConfigIntentObject.
        :rtype: str
        """
        return self._intent_type_id

    @intent_type_id.setter
    def intent_type_id(self, intent_type_id):
        """
        Sets the intent_type_id of this AlertConfigIntentObject.
        Intent type

        :param intent_type_id: The intent_type_id of this AlertConfigIntentObject.
        :type: str
        """
        allowed_values = ["MtuMismatch", "HsrpStpColocation", "PortModeMismatch", "Reachability", "Segmentation", "NativeVlanMismatch", "TrunkPortVlanMismatch", "DuplexMismatch", "PortChannelMismatch", "DuplicateMacAddress", "DuplicateIPAddress", "StpMetricInconsistency", "StigAccountPasswd", "StigConsolePasswd", "StigDefaultPasswd", "StigMgmtPasswd", "StigPlaintextPasswd", "Loop"]
        if intent_type_id not in allowed_values:
            raise ValueError(
                "Invalid value for `intent_type_id` ({0}), must be one of {1}"
                .format(intent_type_id, allowed_values)
            )

        self._intent_type_id = intent_type_id

    @property
    def filter_rules(self):
        """
        Gets the filter_rules of this AlertConfigIntentObject.

        :return: The filter_rules of this AlertConfigIntentObject.
        :rtype: AlertConfigIntentObjectFilterRules
        """
        return self._filter_rules

    @filter_rules.setter
    def filter_rules(self, filter_rules):
        """
        Sets the filter_rules of this AlertConfigIntentObject.

        :param filter_rules: The filter_rules of this AlertConfigIntentObject.
        :type: AlertConfigIntentObjectFilterRules
        """

        self._filter_rules = filter_rules

    @property
    def param_values(self):
        """
        Gets the param_values of this AlertConfigIntentObject.
        Intent parameters

        :return: The param_values of this AlertConfigIntentObject.
        :rtype: list[IntentParam]
        """
        return self._param_values

    @param_values.setter
    def param_values(self, param_values):
        """
        Sets the param_values of this AlertConfigIntentObject.
        Intent parameters

        :param param_values: The param_values of this AlertConfigIntentObject.
        :type: list[IntentParam]
        """

        self._param_values = param_values

    @property
    def selected_scope(self):
        """
        Gets the selected_scope of this AlertConfigIntentObject.
        Intent scope

        :return: The selected_scope of this AlertConfigIntentObject.
        :rtype: str
        """
        return self._selected_scope

    @selected_scope.setter
    def selected_scope(self, selected_scope):
        """
        Sets the selected_scope of this AlertConfigIntentObject.
        Intent scope

        :param selected_scope: The selected_scope of this AlertConfigIntentObject.
        :type: str
        """

        self._selected_scope = selected_scope

    @property
    def description(self):
        """
        Gets the description of this AlertConfigIntentObject.
        Intent description

        :return: The description of this AlertConfigIntentObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AlertConfigIntentObject.
        Intent description

        :param description: The description of this AlertConfigIntentObject.
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """
        Gets the enabled of this AlertConfigIntentObject.

        :return: The enabled of this AlertConfigIntentObject.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this AlertConfigIntentObject.

        :param enabled: The enabled of this AlertConfigIntentObject.
        :type: bool
        """

        self._enabled = enabled

    @property
    def severity(self):
        """
        Gets the severity of this AlertConfigIntentObject.
        Intent severity

        :return: The severity of this AlertConfigIntentObject.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this AlertConfigIntentObject.
        Intent severity

        :param severity: The severity of this AlertConfigIntentObject.
        :type: str
        """
        allowed_values = ["Warning", "Critical", "Moderate", "Info"]
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def notes(self):
        """
        Gets the notes of this AlertConfigIntentObject.
        Intent notes

        :return: The notes of this AlertConfigIntentObject.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this AlertConfigIntentObject.
        Intent notes

        :param notes: The notes of this AlertConfigIntentObject.
        :type: str
        """

        self._notes = notes

    @property
    def tags(self):
        """
        Gets the tags of this AlertConfigIntentObject.

        :return: The tags of this AlertConfigIntentObject.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AlertConfigIntentObject.

        :param tags: The tags of this AlertConfigIntentObject.
        :type: list[str]
        """

        self._tags = tags

    @property
    def notification_settings(self):
        """
        Gets the notification_settings of this AlertConfigIntentObject.

        :return: The notification_settings of this AlertConfigIntentObject.
        :rtype: list[IntentNotification]
        """
        return self._notification_settings

    @notification_settings.setter
    def notification_settings(self, notification_settings):
        """
        Sets the notification_settings of this AlertConfigIntentObject.

        :param notification_settings: The notification_settings of this AlertConfigIntentObject.
        :type: list[IntentNotification]
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
        if not isinstance(other, AlertConfigIntentObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other