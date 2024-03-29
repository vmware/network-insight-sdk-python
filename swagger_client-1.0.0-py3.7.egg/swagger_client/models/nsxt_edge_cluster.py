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


class NSXTEdgeCluster(object):
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
        'deployment_type': 'str',
        'member_node_type': 'str',
        'members': 'list[Reference]',
        'vendor_id': 'str',
        'ecmp': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'manager': 'manager',
        'deployment_type': 'deployment_type',
        'member_node_type': 'member_node_type',
        'members': 'members',
        'vendor_id': 'vendor_id',
        'ecmp': 'ecmp'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, manager=None, deployment_type=None, member_node_type=None, members=None, vendor_id=None, ecmp=None):
        """
        NSXTEdgeCluster - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._manager = None
        self._deployment_type = None
        self._member_node_type = None
        self._members = None
        self._vendor_id = None
        self._ecmp = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if manager is not None:
          self.manager = manager
        if deployment_type is not None:
          self.deployment_type = deployment_type
        if member_node_type is not None:
          self.member_node_type = member_node_type
        if members is not None:
          self.members = members
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if ecmp is not None:
          self.ecmp = ecmp

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSXTEdgeCluster.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this NSXTEdgeCluster.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSXTEdgeCluster.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this NSXTEdgeCluster.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this NSXTEdgeCluster.
        Name of the object

        :return: The name of this NSXTEdgeCluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NSXTEdgeCluster.
        Name of the object

        :param name: The name of this NSXTEdgeCluster.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSXTEdgeCluster.

        :return: The entity_type of this NSXTEdgeCluster.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSXTEdgeCluster.

        :param entity_type: The entity_type of this NSXTEdgeCluster.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def manager(self):
        """
        Gets the manager of this NSXTEdgeCluster.

        :return: The manager of this NSXTEdgeCluster.
        :rtype: Reference
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this NSXTEdgeCluster.

        :param manager: The manager of this NSXTEdgeCluster.
        :type: Reference
        """

        self._manager = manager

    @property
    def deployment_type(self):
        """
        Gets the deployment_type of this NSXTEdgeCluster.

        :return: The deployment_type of this NSXTEdgeCluster.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this NSXTEdgeCluster.

        :param deployment_type: The deployment_type of this NSXTEdgeCluster.
        :type: str
        """

        self._deployment_type = deployment_type

    @property
    def member_node_type(self):
        """
        Gets the member_node_type of this NSXTEdgeCluster.

        :return: The member_node_type of this NSXTEdgeCluster.
        :rtype: str
        """
        return self._member_node_type

    @member_node_type.setter
    def member_node_type(self, member_node_type):
        """
        Sets the member_node_type of this NSXTEdgeCluster.

        :param member_node_type: The member_node_type of this NSXTEdgeCluster.
        :type: str
        """

        self._member_node_type = member_node_type

    @property
    def members(self):
        """
        Gets the members of this NSXTEdgeCluster.

        :return: The members of this NSXTEdgeCluster.
        :rtype: list[Reference]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this NSXTEdgeCluster.

        :param members: The members of this NSXTEdgeCluster.
        :type: list[Reference]
        """

        self._members = members

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this NSXTEdgeCluster.

        :return: The vendor_id of this NSXTEdgeCluster.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this NSXTEdgeCluster.

        :param vendor_id: The vendor_id of this NSXTEdgeCluster.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def ecmp(self):
        """
        Gets the ecmp of this NSXTEdgeCluster.

        :return: The ecmp of this NSXTEdgeCluster.
        :rtype: str
        """
        return self._ecmp

    @ecmp.setter
    def ecmp(self, ecmp):
        """
        Sets the ecmp of this NSXTEdgeCluster.

        :param ecmp: The ecmp of this NSXTEdgeCluster.
        :type: str
        """

        self._ecmp = ecmp

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
        if not isinstance(other, NSXTEdgeCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
