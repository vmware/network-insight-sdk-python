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


class Node(object):
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
        'id': 'str',
        'entity_type': 'NodeType',
        'node_type': 'str',
        'node_id': 'str',
        'ip_address': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'entity_type': 'entity_type',
        'node_type': 'node_type',
        'node_id': 'node_id',
        'ip_address': 'ip_address',
        'name': 'name'
    }

    def __init__(self, id=None, entity_type=None, node_type=None, node_id=None, ip_address=None, name=None):
        """
        Node - a model defined in Swagger
        """

        self._id = None
        self._entity_type = None
        self._node_type = None
        self._node_id = None
        self._ip_address = None
        self._name = None

        if id is not None:
          self.id = id
        if entity_type is not None:
          self.entity_type = entity_type
        if node_type is not None:
          self.node_type = node_type
        if node_id is not None:
          self.node_id = node_id
        if ip_address is not None:
          self.ip_address = ip_address
        if name is not None:
          self.name = name

    @property
    def id(self):
        """
        Gets the id of this Node.

        :return: The id of this Node.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Node.

        :param id: The id of this Node.
        :type: str
        """

        self._id = id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this Node.

        :return: The entity_type of this Node.
        :rtype: NodeType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this Node.

        :param entity_type: The entity_type of this Node.
        :type: NodeType
        """

        self._entity_type = entity_type

    @property
    def node_type(self):
        """
        Gets the node_type of this Node.

        :return: The node_type of this Node.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this Node.

        :param node_type: The node_type of this Node.
        :type: str
        """
        allowed_values = ["PROXY_VM", "PLATFORM_VM"]
        if node_type not in allowed_values:
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

    @property
    def node_id(self):
        """
        Gets the node_id of this Node.

        :return: The node_id of this Node.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this Node.

        :param node_id: The node_id of this Node.
        :type: str
        """

        self._node_id = node_id

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Node.

        :return: The ip_address of this Node.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Node.

        :param ip_address: The ip_address of this Node.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def name(self):
        """
        Gets the name of this Node.

        :return: The name of this Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Node.

        :param name: The name of this Node.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Node):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
