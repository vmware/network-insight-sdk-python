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


class DistributedVirtualPortgroup(object):
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
        'vendor_id': 'str',
        'vcenter_manager': 'Reference',
        'distributed_virtual_switch': 'Reference'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'vendor_id': 'vendor_id',
        'vcenter_manager': 'vcenter_manager',
        'distributed_virtual_switch': 'distributed_virtual_switch'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, vendor_id=None, vcenter_manager=None, distributed_virtual_switch=None):
        """
        DistributedVirtualPortgroup - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._vendor_id = None
        self._vcenter_manager = None
        self._distributed_virtual_switch = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if vcenter_manager is not None:
          self.vcenter_manager = vcenter_manager
        if distributed_virtual_switch is not None:
          self.distributed_virtual_switch = distributed_virtual_switch

    @property
    def entity_id(self):
        """
        Gets the entity_id of this DistributedVirtualPortgroup.

        :return: The entity_id of this DistributedVirtualPortgroup.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this DistributedVirtualPortgroup.

        :param entity_id: The entity_id of this DistributedVirtualPortgroup.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this DistributedVirtualPortgroup.

        :return: The name of this DistributedVirtualPortgroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DistributedVirtualPortgroup.

        :param name: The name of this DistributedVirtualPortgroup.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this DistributedVirtualPortgroup.

        :return: The entity_type of this DistributedVirtualPortgroup.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this DistributedVirtualPortgroup.

        :param entity_type: The entity_type of this DistributedVirtualPortgroup.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this DistributedVirtualPortgroup.

        :return: The vendor_id of this DistributedVirtualPortgroup.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this DistributedVirtualPortgroup.

        :param vendor_id: The vendor_id of this DistributedVirtualPortgroup.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def vcenter_manager(self):
        """
        Gets the vcenter_manager of this DistributedVirtualPortgroup.

        :return: The vcenter_manager of this DistributedVirtualPortgroup.
        :rtype: Reference
        """
        return self._vcenter_manager

    @vcenter_manager.setter
    def vcenter_manager(self, vcenter_manager):
        """
        Sets the vcenter_manager of this DistributedVirtualPortgroup.

        :param vcenter_manager: The vcenter_manager of this DistributedVirtualPortgroup.
        :type: Reference
        """

        self._vcenter_manager = vcenter_manager

    @property
    def distributed_virtual_switch(self):
        """
        Gets the distributed_virtual_switch of this DistributedVirtualPortgroup.

        :return: The distributed_virtual_switch of this DistributedVirtualPortgroup.
        :rtype: Reference
        """
        return self._distributed_virtual_switch

    @distributed_virtual_switch.setter
    def distributed_virtual_switch(self, distributed_virtual_switch):
        """
        Sets the distributed_virtual_switch of this DistributedVirtualPortgroup.

        :param distributed_virtual_switch: The distributed_virtual_switch of this DistributedVirtualPortgroup.
        :type: Reference
        """

        self._distributed_virtual_switch = distributed_virtual_switch

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
        if not isinstance(other, DistributedVirtualPortgroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
