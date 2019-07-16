# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RecommendedRule(object):
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
        'sources': 'list[Reference]',
        'destinations': 'list[Reference]',
        'protocols': 'list[str]',
        'port_ranges': 'list[SimplePortRange]',
        'action': 'str'
    }

    attribute_map = {
        'sources': 'sources',
        'destinations': 'destinations',
        'protocols': 'protocols',
        'port_ranges': 'port_ranges',
        'action': 'action'
    }

    def __init__(self, sources=None, destinations=None, protocols=None, port_ranges=None, action=None):
        """
        RecommendedRule - a model defined in Swagger
        """

        self._sources = None
        self._destinations = None
        self._protocols = None
        self._port_ranges = None
        self._action = None

        if sources is not None:
          self.sources = sources
        if destinations is not None:
          self.destinations = destinations
        if protocols is not None:
          self.protocols = protocols
        if port_ranges is not None:
          self.port_ranges = port_ranges
        if action is not None:
          self.action = action

    @property
    def sources(self):
        """
        Gets the sources of this RecommendedRule.

        :return: The sources of this RecommendedRule.
        :rtype: list[Reference]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """
        Sets the sources of this RecommendedRule.

        :param sources: The sources of this RecommendedRule.
        :type: list[Reference]
        """

        self._sources = sources

    @property
    def destinations(self):
        """
        Gets the destinations of this RecommendedRule.

        :return: The destinations of this RecommendedRule.
        :rtype: list[Reference]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """
        Sets the destinations of this RecommendedRule.

        :param destinations: The destinations of this RecommendedRule.
        :type: list[Reference]
        """

        self._destinations = destinations

    @property
    def protocols(self):
        """
        Gets the protocols of this RecommendedRule.

        :return: The protocols of this RecommendedRule.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """
        Sets the protocols of this RecommendedRule.

        :param protocols: The protocols of this RecommendedRule.
        :type: list[str]
        """

        self._protocols = protocols

    @property
    def port_ranges(self):
        """
        Gets the port_ranges of this RecommendedRule.

        :return: The port_ranges of this RecommendedRule.
        :rtype: list[SimplePortRange]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        """
        Sets the port_ranges of this RecommendedRule.

        :param port_ranges: The port_ranges of this RecommendedRule.
        :type: list[SimplePortRange]
        """

        self._port_ranges = port_ranges

    @property
    def action(self):
        """
        Gets the action of this RecommendedRule.

        :return: The action of this RecommendedRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this RecommendedRule.

        :param action: The action of this RecommendedRule.
        :type: str
        """
        allowed_values = ["ALLOW", "DROP"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

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
        if not isinstance(other, RecommendedRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
