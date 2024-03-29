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


class HCXServiceMesh(object):
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
        'state': 'str',
        'services': 'list[Reference]',
        'compute_profiles': 'list[Reference]',
        'hcx_manager_pair': 'list[Reference]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'vendor_id': 'vendor_id',
        'state': 'state',
        'services': 'services',
        'compute_profiles': 'compute_profiles',
        'hcx_manager_pair': 'hcx_manager_pair'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, vendor_id=None, state=None, services=None, compute_profiles=None, hcx_manager_pair=None):
        """
        HCXServiceMesh - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._vendor_id = None
        self._state = None
        self._services = None
        self._compute_profiles = None
        self._hcx_manager_pair = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if state is not None:
          self.state = state
        if services is not None:
          self.services = services
        if compute_profiles is not None:
          self.compute_profiles = compute_profiles
        if hcx_manager_pair is not None:
          self.hcx_manager_pair = hcx_manager_pair

    @property
    def entity_id(self):
        """
        Gets the entity_id of this HCXServiceMesh.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this HCXServiceMesh.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this HCXServiceMesh.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this HCXServiceMesh.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this HCXServiceMesh.
        Name of the object

        :return: The name of this HCXServiceMesh.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HCXServiceMesh.
        Name of the object

        :param name: The name of this HCXServiceMesh.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this HCXServiceMesh.

        :return: The entity_type of this HCXServiceMesh.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this HCXServiceMesh.

        :param entity_type: The entity_type of this HCXServiceMesh.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this HCXServiceMesh.

        :return: The vendor_id of this HCXServiceMesh.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this HCXServiceMesh.

        :param vendor_id: The vendor_id of this HCXServiceMesh.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def state(self):
        """
        Gets the state of this HCXServiceMesh.

        :return: The state of this HCXServiceMesh.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this HCXServiceMesh.

        :param state: The state of this HCXServiceMesh.
        :type: str
        """

        self._state = state

    @property
    def services(self):
        """
        Gets the services of this HCXServiceMesh.

        :return: The services of this HCXServiceMesh.
        :rtype: list[Reference]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this HCXServiceMesh.

        :param services: The services of this HCXServiceMesh.
        :type: list[Reference]
        """

        self._services = services

    @property
    def compute_profiles(self):
        """
        Gets the compute_profiles of this HCXServiceMesh.

        :return: The compute_profiles of this HCXServiceMesh.
        :rtype: list[Reference]
        """
        return self._compute_profiles

    @compute_profiles.setter
    def compute_profiles(self, compute_profiles):
        """
        Sets the compute_profiles of this HCXServiceMesh.

        :param compute_profiles: The compute_profiles of this HCXServiceMesh.
        :type: list[Reference]
        """

        self._compute_profiles = compute_profiles

    @property
    def hcx_manager_pair(self):
        """
        Gets the hcx_manager_pair of this HCXServiceMesh.

        :return: The hcx_manager_pair of this HCXServiceMesh.
        :rtype: list[Reference]
        """
        return self._hcx_manager_pair

    @hcx_manager_pair.setter
    def hcx_manager_pair(self, hcx_manager_pair):
        """
        Sets the hcx_manager_pair of this HCXServiceMesh.

        :param hcx_manager_pair: The hcx_manager_pair of this HCXServiceMesh.
        :type: list[Reference]
        """

        self._hcx_manager_pair = hcx_manager_pair

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
        if not isinstance(other, HCXServiceMesh):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
