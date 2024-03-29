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


class FBADConfigRequest(object):
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
        'scope_object_type': 'int',
        'scope_entities': 'list[str]',
        'full_fetch_flow_interval_in_sec': 'int',
        'pause_discovery': 'bool',
        'application_naming_preferences': 'list[NamingPreference]',
        'tier_naming_preferences': 'list[NamingPreference]',
        'discovery_options': 'list[DiscoveryOption]'
    }

    attribute_map = {
        'scope_object_type': 'scope_object_type',
        'scope_entities': 'scope_entities',
        'full_fetch_flow_interval_in_sec': 'full_fetch_flow_interval_in_sec',
        'pause_discovery': 'pause_discovery',
        'application_naming_preferences': 'application_naming_preferences',
        'tier_naming_preferences': 'tier_naming_preferences',
        'discovery_options': 'discovery_options'
    }

    def __init__(self, scope_object_type=0, scope_entities=None, full_fetch_flow_interval_in_sec=0, pause_discovery=False, application_naming_preferences=None, tier_naming_preferences=None, discovery_options=None):
        """
        FBADConfigRequest - a model defined in Swagger
        """

        self._scope_object_type = None
        self._scope_entities = None
        self._full_fetch_flow_interval_in_sec = None
        self._pause_discovery = None
        self._application_naming_preferences = None
        self._tier_naming_preferences = None
        self._discovery_options = None

        if scope_object_type is not None:
          self.scope_object_type = scope_object_type
        if scope_entities is not None:
          self.scope_entities = scope_entities
        if full_fetch_flow_interval_in_sec is not None:
          self.full_fetch_flow_interval_in_sec = full_fetch_flow_interval_in_sec
        if pause_discovery is not None:
          self.pause_discovery = pause_discovery
        if application_naming_preferences is not None:
          self.application_naming_preferences = application_naming_preferences
        if tier_naming_preferences is not None:
          self.tier_naming_preferences = tier_naming_preferences
        if discovery_options is not None:
          self.discovery_options = discovery_options

    @property
    def scope_object_type(self):
        """
        Gets the scope_object_type of this FBADConfigRequest.
        The type of objects in the scope entities

        :return: The scope_object_type of this FBADConfigRequest.
        :rtype: int
        """
        return self._scope_object_type

    @scope_object_type.setter
    def scope_object_type(self, scope_object_type):
        """
        Sets the scope_object_type of this FBADConfigRequest.
        The type of objects in the scope entities

        :param scope_object_type: The scope_object_type of this FBADConfigRequest.
        :type: int
        """

        self._scope_object_type = scope_object_type

    @property
    def scope_entities(self):
        """
        Gets the scope_entities of this FBADConfigRequest.
        The list of name of the entities to be considered in discovery scope

        :return: The scope_entities of this FBADConfigRequest.
        :rtype: list[str]
        """
        return self._scope_entities

    @scope_entities.setter
    def scope_entities(self, scope_entities):
        """
        Sets the scope_entities of this FBADConfigRequest.
        The list of name of the entities to be considered in discovery scope

        :param scope_entities: The scope_entities of this FBADConfigRequest.
        :type: list[str]
        """

        self._scope_entities = scope_entities

    @property
    def full_fetch_flow_interval_in_sec(self):
        """
        Gets the full_fetch_flow_interval_in_sec of this FBADConfigRequest.
        Full fetch flow interval in seconds. Range of allowed values is number of seconds in one week to number of seconds in one month, both values included.

        :return: The full_fetch_flow_interval_in_sec of this FBADConfigRequest.
        :rtype: int
        """
        return self._full_fetch_flow_interval_in_sec

    @full_fetch_flow_interval_in_sec.setter
    def full_fetch_flow_interval_in_sec(self, full_fetch_flow_interval_in_sec):
        """
        Sets the full_fetch_flow_interval_in_sec of this FBADConfigRequest.
        Full fetch flow interval in seconds. Range of allowed values is number of seconds in one week to number of seconds in one month, both values included.

        :param full_fetch_flow_interval_in_sec: The full_fetch_flow_interval_in_sec of this FBADConfigRequest.
        :type: int
        """

        self._full_fetch_flow_interval_in_sec = full_fetch_flow_interval_in_sec

    @property
    def pause_discovery(self):
        """
        Gets the pause_discovery of this FBADConfigRequest.
        True means pause the application and tier discovery and false means resume flow based application and tier discovery

        :return: The pause_discovery of this FBADConfigRequest.
        :rtype: bool
        """
        return self._pause_discovery

    @pause_discovery.setter
    def pause_discovery(self, pause_discovery):
        """
        Sets the pause_discovery of this FBADConfigRequest.
        True means pause the application and tier discovery and false means resume flow based application and tier discovery

        :param pause_discovery: The pause_discovery of this FBADConfigRequest.
        :type: bool
        """

        self._pause_discovery = pause_discovery

    @property
    def application_naming_preferences(self):
        """
        Gets the application_naming_preferences of this FBADConfigRequest.
        List of application naming preferences. The order should be the same as tier naming preferences. VM Names preference will be added to the end of the naming preferences if not present already.

        :return: The application_naming_preferences of this FBADConfigRequest.
        :rtype: list[NamingPreference]
        """
        return self._application_naming_preferences

    @application_naming_preferences.setter
    def application_naming_preferences(self, application_naming_preferences):
        """
        Sets the application_naming_preferences of this FBADConfigRequest.
        List of application naming preferences. The order should be the same as tier naming preferences. VM Names preference will be added to the end of the naming preferences if not present already.

        :param application_naming_preferences: The application_naming_preferences of this FBADConfigRequest.
        :type: list[NamingPreference]
        """

        self._application_naming_preferences = application_naming_preferences

    @property
    def tier_naming_preferences(self):
        """
        Gets the tier_naming_preferences of this FBADConfigRequest.
        List of tier naming preferences. The order should be the same as application naming preferences. VM Names preference will be added to the end of the naming preferences if not present already.

        :return: The tier_naming_preferences of this FBADConfigRequest.
        :rtype: list[NamingPreference]
        """
        return self._tier_naming_preferences

    @tier_naming_preferences.setter
    def tier_naming_preferences(self, tier_naming_preferences):
        """
        Sets the tier_naming_preferences of this FBADConfigRequest.
        List of tier naming preferences. The order should be the same as application naming preferences. VM Names preference will be added to the end of the naming preferences if not present already.

        :param tier_naming_preferences: The tier_naming_preferences of this FBADConfigRequest.
        :type: list[NamingPreference]
        """

        self._tier_naming_preferences = tier_naming_preferences

    @property
    def discovery_options(self):
        """
        Gets the discovery_options of this FBADConfigRequest.
        The ordered list of preferences to be used for discovery of applications and tiers to improve flow based application discovery. Add CSV enrichment preference to use the uploaded CSV in improving discovery. LB enrichment preference will be added at the end of the list if not present already.

        :return: The discovery_options of this FBADConfigRequest.
        :rtype: list[DiscoveryOption]
        """
        return self._discovery_options

    @discovery_options.setter
    def discovery_options(self, discovery_options):
        """
        Sets the discovery_options of this FBADConfigRequest.
        The ordered list of preferences to be used for discovery of applications and tiers to improve flow based application discovery. Add CSV enrichment preference to use the uploaded CSV in improving discovery. LB enrichment preference will be added at the end of the list if not present already.

        :param discovery_options: The discovery_options of this FBADConfigRequest.
        :type: list[DiscoveryOption]
        """

        self._discovery_options = discovery_options

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
        if not isinstance(other, FBADConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
