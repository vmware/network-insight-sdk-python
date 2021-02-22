# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NSXTFirewallRule(object):
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
        'name': 'str',
        'entity_type': 'EntityType',
        'rule_id': 'str',
        'section_id': 'str',
        'section_name': 'str',
        'sequence_number': 'int',
        'source_any': 'bool',
        'destination_any': 'bool',
        'service_any': 'bool',
        'sources': 'list[Reference]',
        'destinations': 'list[Reference]',
        'services': 'list[Reference]',
        'action': 'FirewallAction',
        'disabled': 'bool',
        'source_inversion': 'bool',
        'destination_inversion': 'bool',
        'port_ranges': 'list[PortRange]',
        'logging_enabled': 'bool',
        'direction': 'FirewallDirection',
        'scope': 'ScopeEnum',
        'nsx_managers': 'list[Reference]',
        'applied_tos': 'list[AppliedTo]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'rule_id': 'rule_id',
        'section_id': 'section_id',
        'section_name': 'section_name',
        'sequence_number': 'sequence_number',
        'source_any': 'source_any',
        'destination_any': 'destination_any',
        'service_any': 'service_any',
        'sources': 'sources',
        'destinations': 'destinations',
        'services': 'services',
        'action': 'action',
        'disabled': 'disabled',
        'source_inversion': 'source_inversion',
        'destination_inversion': 'destination_inversion',
        'port_ranges': 'port_ranges',
        'logging_enabled': 'logging_enabled',
        'direction': 'direction',
        'scope': 'scope',
        'nsx_managers': 'nsx_managers',
        'applied_tos': 'applied_tos'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, rule_id=None, section_id=None, section_name=None, sequence_number=None, source_any=None, destination_any=None, service_any=None, sources=None, destinations=None, services=None, action=None, disabled=None, source_inversion=None, destination_inversion=None, port_ranges=None, logging_enabled=None, direction=None, scope=None, nsx_managers=None, applied_tos=None):
        """
        NSXTFirewallRule - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._rule_id = None
        self._section_id = None
        self._section_name = None
        self._sequence_number = None
        self._source_any = None
        self._destination_any = None
        self._service_any = None
        self._sources = None
        self._destinations = None
        self._services = None
        self._action = None
        self._disabled = None
        self._source_inversion = None
        self._destination_inversion = None
        self._port_ranges = None
        self._logging_enabled = None
        self._direction = None
        self._scope = None
        self._nsx_managers = None
        self._applied_tos = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if rule_id is not None:
          self.rule_id = rule_id
        if section_id is not None:
          self.section_id = section_id
        if section_name is not None:
          self.section_name = section_name
        if sequence_number is not None:
          self.sequence_number = sequence_number
        if source_any is not None:
          self.source_any = source_any
        if destination_any is not None:
          self.destination_any = destination_any
        if service_any is not None:
          self.service_any = service_any
        if sources is not None:
          self.sources = sources
        if destinations is not None:
          self.destinations = destinations
        if services is not None:
          self.services = services
        if action is not None:
          self.action = action
        if disabled is not None:
          self.disabled = disabled
        if source_inversion is not None:
          self.source_inversion = source_inversion
        if destination_inversion is not None:
          self.destination_inversion = destination_inversion
        if port_ranges is not None:
          self.port_ranges = port_ranges
        if logging_enabled is not None:
          self.logging_enabled = logging_enabled
        if direction is not None:
          self.direction = direction
        if scope is not None:
          self.scope = scope
        if nsx_managers is not None:
          self.nsx_managers = nsx_managers
        if applied_tos is not None:
          self.applied_tos = applied_tos

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSXTFirewallRule.

        :return: The entity_id of this NSXTFirewallRule.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSXTFirewallRule.

        :param entity_id: The entity_id of this NSXTFirewallRule.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this NSXTFirewallRule.

        :return: The name of this NSXTFirewallRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NSXTFirewallRule.

        :param name: The name of this NSXTFirewallRule.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSXTFirewallRule.

        :return: The entity_type of this NSXTFirewallRule.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSXTFirewallRule.

        :param entity_type: The entity_type of this NSXTFirewallRule.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def rule_id(self):
        """
        Gets the rule_id of this NSXTFirewallRule.

        :return: The rule_id of this NSXTFirewallRule.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """
        Sets the rule_id of this NSXTFirewallRule.

        :param rule_id: The rule_id of this NSXTFirewallRule.
        :type: str
        """

        self._rule_id = rule_id

    @property
    def section_id(self):
        """
        Gets the section_id of this NSXTFirewallRule.

        :return: The section_id of this NSXTFirewallRule.
        :rtype: str
        """
        return self._section_id

    @section_id.setter
    def section_id(self, section_id):
        """
        Sets the section_id of this NSXTFirewallRule.

        :param section_id: The section_id of this NSXTFirewallRule.
        :type: str
        """

        self._section_id = section_id

    @property
    def section_name(self):
        """
        Gets the section_name of this NSXTFirewallRule.

        :return: The section_name of this NSXTFirewallRule.
        :rtype: str
        """
        return self._section_name

    @section_name.setter
    def section_name(self, section_name):
        """
        Sets the section_name of this NSXTFirewallRule.

        :param section_name: The section_name of this NSXTFirewallRule.
        :type: str
        """

        self._section_name = section_name

    @property
    def sequence_number(self):
        """
        Gets the sequence_number of this NSXTFirewallRule.

        :return: The sequence_number of this NSXTFirewallRule.
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """
        Sets the sequence_number of this NSXTFirewallRule.

        :param sequence_number: The sequence_number of this NSXTFirewallRule.
        :type: int
        """

        self._sequence_number = sequence_number

    @property
    def source_any(self):
        """
        Gets the source_any of this NSXTFirewallRule.

        :return: The source_any of this NSXTFirewallRule.
        :rtype: bool
        """
        return self._source_any

    @source_any.setter
    def source_any(self, source_any):
        """
        Sets the source_any of this NSXTFirewallRule.

        :param source_any: The source_any of this NSXTFirewallRule.
        :type: bool
        """

        self._source_any = source_any

    @property
    def destination_any(self):
        """
        Gets the destination_any of this NSXTFirewallRule.

        :return: The destination_any of this NSXTFirewallRule.
        :rtype: bool
        """
        return self._destination_any

    @destination_any.setter
    def destination_any(self, destination_any):
        """
        Sets the destination_any of this NSXTFirewallRule.

        :param destination_any: The destination_any of this NSXTFirewallRule.
        :type: bool
        """

        self._destination_any = destination_any

    @property
    def service_any(self):
        """
        Gets the service_any of this NSXTFirewallRule.

        :return: The service_any of this NSXTFirewallRule.
        :rtype: bool
        """
        return self._service_any

    @service_any.setter
    def service_any(self, service_any):
        """
        Sets the service_any of this NSXTFirewallRule.

        :param service_any: The service_any of this NSXTFirewallRule.
        :type: bool
        """

        self._service_any = service_any

    @property
    def sources(self):
        """
        Gets the sources of this NSXTFirewallRule.

        :return: The sources of this NSXTFirewallRule.
        :rtype: list[Reference]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this NSXTFirewallRule.

        :param sources: The sources of this NSXTFirewallRule.
        :type: list[Reference]
        """

        self._sources = sources

    @property
    def destinations(self):
        """
        Gets the destinations of this NSXTFirewallRule.

        :return: The destinations of this NSXTFirewallRule.
        :rtype: list[Reference]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """
        Sets the destinations of this NSXTFirewallRule.

        :param destinations: The destinations of this NSXTFirewallRule.
        :type: list[Reference]
        """

        self._destinations = destinations

    @property
    def services(self):
        """
        Gets the services of this NSXTFirewallRule.

        :return: The services of this NSXTFirewallRule.
        :rtype: list[Reference]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this NSXTFirewallRule.

        :param services: The services of this NSXTFirewallRule.
        :type: list[Reference]
        """

        self._services = services

    @property
    def action(self):
        """
        Gets the action of this NSXTFirewallRule.

        :return: The action of this NSXTFirewallRule.
        :rtype: FirewallAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this NSXTFirewallRule.

        :param action: The action of this NSXTFirewallRule.
        :type: FirewallAction
        """

        self._action = action

    @property
    def disabled(self):
        """
        Gets the disabled of this NSXTFirewallRule.

        :return: The disabled of this NSXTFirewallRule.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """
        Sets the disabled of this NSXTFirewallRule.

        :param disabled: The disabled of this NSXTFirewallRule.
        :type: bool
        """

        self._disabled = disabled

    @property
    def source_inversion(self):
        """
        Gets the source_inversion of this NSXTFirewallRule.

        :return: The source_inversion of this NSXTFirewallRule.
        :rtype: bool
        """
        return self._source_inversion

    @source_inversion.setter
    def source_inversion(self, source_inversion):
        """
        Sets the source_inversion of this NSXTFirewallRule.

        :param source_inversion: The source_inversion of this NSXTFirewallRule.
        :type: bool
        """

        self._source_inversion = source_inversion

    @property
    def destination_inversion(self):
        """
        Gets the destination_inversion of this NSXTFirewallRule.

        :return: The destination_inversion of this NSXTFirewallRule.
        :rtype: bool
        """
        return self._destination_inversion

    @destination_inversion.setter
    def destination_inversion(self, destination_inversion):
        """
        Sets the destination_inversion of this NSXTFirewallRule.

        :param destination_inversion: The destination_inversion of this NSXTFirewallRule.
        :type: bool
        """

        self._destination_inversion = destination_inversion

    @property
    def port_ranges(self):
        """
        Gets the port_ranges of this NSXTFirewallRule.

        :return: The port_ranges of this NSXTFirewallRule.
        :rtype: list[PortRange]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        """
        Sets the port_ranges of this NSXTFirewallRule.

        :param port_ranges: The port_ranges of this NSXTFirewallRule.
        :type: list[PortRange]
        """

        self._port_ranges = port_ranges

    @property
    def logging_enabled(self):
        """
        Gets the logging_enabled of this NSXTFirewallRule.

        :return: The logging_enabled of this NSXTFirewallRule.
        :rtype: bool
        """
        return self._logging_enabled

    @logging_enabled.setter
    def logging_enabled(self, logging_enabled):
        """
        Sets the logging_enabled of this NSXTFirewallRule.

        :param logging_enabled: The logging_enabled of this NSXTFirewallRule.
        :type: bool
        """

        self._logging_enabled = logging_enabled

    @property
    def direction(self):
        """
        Gets the direction of this NSXTFirewallRule.

        :return: The direction of this NSXTFirewallRule.
        :rtype: FirewallDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this NSXTFirewallRule.

        :param direction: The direction of this NSXTFirewallRule.
        :type: FirewallDirection
        """

        self._direction = direction

    @property
    def scope(self):
        """
        Gets the scope of this NSXTFirewallRule.

        :return: The scope of this NSXTFirewallRule.
        :rtype: ScopeEnum
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this NSXTFirewallRule.

        :param scope: The scope of this NSXTFirewallRule.
        :type: ScopeEnum
        """

        self._scope = scope

    @property
    def nsx_managers(self):
        """
        Gets the nsx_managers of this NSXTFirewallRule.

        :return: The nsx_managers of this NSXTFirewallRule.
        :rtype: list[Reference]
        """
        return self._nsx_managers

    @nsx_managers.setter
    def nsx_managers(self, nsx_managers):
        """
        Sets the nsx_managers of this NSXTFirewallRule.

        :param nsx_managers: The nsx_managers of this NSXTFirewallRule.
        :type: list[Reference]
        """

        self._nsx_managers = nsx_managers

    @property
    def applied_tos(self):
        """
        Gets the applied_tos of this NSXTFirewallRule.

        :return: The applied_tos of this NSXTFirewallRule.
        :rtype: list[AppliedTo]
        """
        return self._applied_tos

    @applied_tos.setter
    def applied_tos(self, applied_tos):
        """
        Sets the applied_tos of this NSXTFirewallRule.

        :param applied_tos: The applied_tos of this NSXTFirewallRule.
        :type: list[AppliedTo]
        """

        self._applied_tos = applied_tos

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
        if not isinstance(other, NSXTFirewallRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
