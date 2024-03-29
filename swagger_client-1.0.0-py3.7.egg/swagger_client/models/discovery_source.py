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


class DiscoverySource(object):
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
        'source_type': 'DiscoveryType',
        'entity_id': 'str',
        'manager_entity_id': 'str'
    }

    attribute_map = {
        'source_type': 'source_type',
        'entity_id': 'entity_id',
        'manager_entity_id': 'manager_entity_id'
    }

    def __init__(self, source_type=None, entity_id=None, manager_entity_id=None):
        """
        DiscoverySource - a model defined in Swagger
        """

        self._source_type = None
        self._entity_id = None
        self._manager_entity_id = None

        if source_type is not None:
          self.source_type = source_type
        if entity_id is not None:
          self.entity_id = entity_id
        if manager_entity_id is not None:
          self.manager_entity_id = manager_entity_id

    @property
    def source_type(self):
        """
        Gets the source_type of this DiscoverySource.

        :return: The source_type of this DiscoverySource.
        :rtype: DiscoveryType
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this DiscoverySource.

        :param source_type: The source_type of this DiscoverySource.
        :type: DiscoveryType
        """

        self._source_type = source_type

    @property
    def entity_id(self):
        """
        Gets the entity_id of this DiscoverySource.

        :return: The entity_id of this DiscoverySource.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this DiscoverySource.

        :param entity_id: The entity_id of this DiscoverySource.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def manager_entity_id(self):
        """
        Gets the manager_entity_id of this DiscoverySource.

        :return: The manager_entity_id of this DiscoverySource.
        :rtype: str
        """
        return self._manager_entity_id

    @manager_entity_id.setter
    def manager_entity_id(self, manager_entity_id):
        """
        Sets the manager_entity_id of this DiscoverySource.

        :param manager_entity_id: The manager_entity_id of this DiscoverySource.
        :type: str
        """

        self._manager_entity_id = manager_entity_id

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
        if not isinstance(other, DiscoverySource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
