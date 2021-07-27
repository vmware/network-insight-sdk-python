# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NSXControllerCluster(object):
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
        'controllers': 'list[Reference]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'manager': 'manager',
        'controllers': 'controllers'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, manager=None, controllers=None):
        """
        NSXControllerCluster - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._manager = None
        self._controllers = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if manager is not None:
          self.manager = manager
        if controllers is not None:
          self.controllers = controllers

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSXControllerCluster.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this NSXControllerCluster.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSXControllerCluster.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this NSXControllerCluster.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this NSXControllerCluster.
        Name of the object

        :return: The name of this NSXControllerCluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NSXControllerCluster.
        Name of the object

        :param name: The name of this NSXControllerCluster.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSXControllerCluster.

        :return: The entity_type of this NSXControllerCluster.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSXControllerCluster.

        :param entity_type: The entity_type of this NSXControllerCluster.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def manager(self):
        """
        Gets the manager of this NSXControllerCluster.

        :return: The manager of this NSXControllerCluster.
        :rtype: Reference
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this NSXControllerCluster.

        :param manager: The manager of this NSXControllerCluster.
        :type: Reference
        """

        self._manager = manager

    @property
    def controllers(self):
        """
        Gets the controllers of this NSXControllerCluster.

        :return: The controllers of this NSXControllerCluster.
        :rtype: list[Reference]
        """
        return self._controllers

    @controllers.setter
    def controllers(self, controllers):
        """
        Sets the controllers of this NSXControllerCluster.

        :param controllers: The controllers of this NSXControllerCluster.
        :type: list[Reference]
        """

        self._controllers = controllers

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
        if not isinstance(other, NSXControllerCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
