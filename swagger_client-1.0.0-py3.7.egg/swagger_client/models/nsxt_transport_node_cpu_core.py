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


class NSXTTransportNodeCPUCore(object):
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
        'manager': 'Reference',
        'transport_node': 'Reference',
        'cpu_core_type': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'manager': 'manager',
        'transport_node': 'transport_node',
        'cpu_core_type': 'cpu_core_type'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, manager=None, transport_node=None, cpu_core_type=None):
        """
        NSXTTransportNodeCPUCore - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._manager = None
        self._transport_node = None
        self._cpu_core_type = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if manager is not None:
          self.manager = manager
        if transport_node is not None:
          self.transport_node = transport_node
        if cpu_core_type is not None:
          self.cpu_core_type = cpu_core_type

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSXTTransportNodeCPUCore.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this NSXTTransportNodeCPUCore.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSXTTransportNodeCPUCore.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this NSXTTransportNodeCPUCore.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this NSXTTransportNodeCPUCore.

        :return: The name of this NSXTTransportNodeCPUCore.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NSXTTransportNodeCPUCore.

        :param name: The name of this NSXTTransportNodeCPUCore.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSXTTransportNodeCPUCore.

        :return: The entity_type of this NSXTTransportNodeCPUCore.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSXTTransportNodeCPUCore.

        :param entity_type: The entity_type of this NSXTTransportNodeCPUCore.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def manager(self):
        """
        Gets the manager of this NSXTTransportNodeCPUCore.

        :return: The manager of this NSXTTransportNodeCPUCore.
        :rtype: Reference
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this NSXTTransportNodeCPUCore.

        :param manager: The manager of this NSXTTransportNodeCPUCore.
        :type: Reference
        """

        self._manager = manager

    @property
    def transport_node(self):
        """
        Gets the transport_node of this NSXTTransportNodeCPUCore.

        :return: The transport_node of this NSXTTransportNodeCPUCore.
        :rtype: Reference
        """
        return self._transport_node

    @transport_node.setter
    def transport_node(self, transport_node):
        """
        Sets the transport_node of this NSXTTransportNodeCPUCore.

        :param transport_node: The transport_node of this NSXTTransportNodeCPUCore.
        :type: Reference
        """

        self._transport_node = transport_node

    @property
    def cpu_core_type(self):
        """
        Gets the cpu_core_type of this NSXTTransportNodeCPUCore.

        :return: The cpu_core_type of this NSXTTransportNodeCPUCore.
        :rtype: str
        """
        return self._cpu_core_type

    @cpu_core_type.setter
    def cpu_core_type(self, cpu_core_type):
        """
        Sets the cpu_core_type of this NSXTTransportNodeCPUCore.

        :param cpu_core_type: The cpu_core_type of this NSXTTransportNodeCPUCore.
        :type: str
        """

        self._cpu_core_type = cpu_core_type

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
        if not isinstance(other, NSXTTransportNodeCPUCore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
