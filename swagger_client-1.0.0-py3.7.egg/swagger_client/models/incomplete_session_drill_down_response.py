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


class IncompleteSessionDrillDownResponse(object):
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
        'src_entity': 'str',
        'src_entity_id': 'str',
        'src_entity_type': 'str',
        'dst_port': 'str',
        'firewall_rule': 'str',
        'firewall_rule_id': 'str',
        'incomplete_tcp_session_count': 'int'
    }

    attribute_map = {
        'src_entity': 'src_entity',
        'src_entity_id': 'src_entity_id',
        'src_entity_type': 'src_entity_type',
        'dst_port': 'dst_Port',
        'firewall_rule': 'firewall_rule',
        'firewall_rule_id': 'firewall_rule_id',
        'incomplete_tcp_session_count': 'incomplete_tcp_session_count'
    }

    def __init__(self, src_entity=None, src_entity_id=None, src_entity_type=None, dst_port=None, firewall_rule=None, firewall_rule_id=None, incomplete_tcp_session_count=None):
        """
        IncompleteSessionDrillDownResponse - a model defined in Swagger
        """

        self._src_entity = None
        self._src_entity_id = None
        self._src_entity_type = None
        self._dst_port = None
        self._firewall_rule = None
        self._firewall_rule_id = None
        self._incomplete_tcp_session_count = None

        if src_entity is not None:
          self.src_entity = src_entity
        if src_entity_id is not None:
          self.src_entity_id = src_entity_id
        if src_entity_type is not None:
          self.src_entity_type = src_entity_type
        if dst_port is not None:
          self.dst_port = dst_port
        if firewall_rule is not None:
          self.firewall_rule = firewall_rule
        if firewall_rule_id is not None:
          self.firewall_rule_id = firewall_rule_id
        if incomplete_tcp_session_count is not None:
          self.incomplete_tcp_session_count = incomplete_tcp_session_count

    @property
    def src_entity(self):
        """
        Gets the src_entity of this IncompleteSessionDrillDownResponse.

        :return: The src_entity of this IncompleteSessionDrillDownResponse.
        :rtype: str
        """
        return self._src_entity

    @src_entity.setter
    def src_entity(self, src_entity):
        """
        Sets the src_entity of this IncompleteSessionDrillDownResponse.

        :param src_entity: The src_entity of this IncompleteSessionDrillDownResponse.
        :type: str
        """

        self._src_entity = src_entity

    @property
    def src_entity_id(self):
        """
        Gets the src_entity_id of this IncompleteSessionDrillDownResponse.

        :return: The src_entity_id of this IncompleteSessionDrillDownResponse.
        :rtype: str
        """
        return self._src_entity_id

    @src_entity_id.setter
    def src_entity_id(self, src_entity_id):
        """
        Sets the src_entity_id of this IncompleteSessionDrillDownResponse.

        :param src_entity_id: The src_entity_id of this IncompleteSessionDrillDownResponse.
        :type: str
        """

        self._src_entity_id = src_entity_id

    @property
    def src_entity_type(self):
        """
        Gets the src_entity_type of this IncompleteSessionDrillDownResponse.

        :return: The src_entity_type of this IncompleteSessionDrillDownResponse.
        :rtype: str
        """
        return self._src_entity_type

    @src_entity_type.setter
    def src_entity_type(self, src_entity_type):
        """
        Sets the src_entity_type of this IncompleteSessionDrillDownResponse.

        :param src_entity_type: The src_entity_type of this IncompleteSessionDrillDownResponse.
        :type: str
        """

        self._src_entity_type = src_entity_type

    @property
    def dst_port(self):
        """
        Gets the dst_port of this IncompleteSessionDrillDownResponse.

        :return: The dst_port of this IncompleteSessionDrillDownResponse.
        :rtype: str
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        """
        Sets the dst_port of this IncompleteSessionDrillDownResponse.

        :param dst_port: The dst_port of this IncompleteSessionDrillDownResponse.
        :type: str
        """

        self._dst_port = dst_port

    @property
    def firewall_rule(self):
        """
        Gets the firewall_rule of this IncompleteSessionDrillDownResponse.

        :return: The firewall_rule of this IncompleteSessionDrillDownResponse.
        :rtype: str
        """
        return self._firewall_rule

    @firewall_rule.setter
    def firewall_rule(self, firewall_rule):
        """
        Sets the firewall_rule of this IncompleteSessionDrillDownResponse.

        :param firewall_rule: The firewall_rule of this IncompleteSessionDrillDownResponse.
        :type: str
        """

        self._firewall_rule = firewall_rule

    @property
    def firewall_rule_id(self):
        """
        Gets the firewall_rule_id of this IncompleteSessionDrillDownResponse.

        :return: The firewall_rule_id of this IncompleteSessionDrillDownResponse.
        :rtype: str
        """
        return self._firewall_rule_id

    @firewall_rule_id.setter
    def firewall_rule_id(self, firewall_rule_id):
        """
        Sets the firewall_rule_id of this IncompleteSessionDrillDownResponse.

        :param firewall_rule_id: The firewall_rule_id of this IncompleteSessionDrillDownResponse.
        :type: str
        """

        self._firewall_rule_id = firewall_rule_id

    @property
    def incomplete_tcp_session_count(self):
        """
        Gets the incomplete_tcp_session_count of this IncompleteSessionDrillDownResponse.

        :return: The incomplete_tcp_session_count of this IncompleteSessionDrillDownResponse.
        :rtype: int
        """
        return self._incomplete_tcp_session_count

    @incomplete_tcp_session_count.setter
    def incomplete_tcp_session_count(self, incomplete_tcp_session_count):
        """
        Sets the incomplete_tcp_session_count of this IncompleteSessionDrillDownResponse.

        :param incomplete_tcp_session_count: The incomplete_tcp_session_count of this IncompleteSessionDrillDownResponse.
        :type: int
        """

        self._incomplete_tcp_session_count = incomplete_tcp_session_count

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
        if not isinstance(other, IncompleteSessionDrillDownResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
