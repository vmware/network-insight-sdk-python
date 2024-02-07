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


class HCXService(object):
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
        'service_mesh': 'Reference',
        'service_type': 'str',
        'status': 'str',
        'hcx_manager_pair': 'list[Reference]',
        'running_state': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'service_mesh': 'service_mesh',
        'service_type': 'service_type',
        'status': 'status',
        'hcx_manager_pair': 'hcx_manager_pair',
        'running_state': 'running_state'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, service_mesh=None, service_type=None, status=None, hcx_manager_pair=None, running_state=None):
        """
        HCXService - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._service_mesh = None
        self._service_type = None
        self._status = None
        self._hcx_manager_pair = None
        self._running_state = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if service_mesh is not None:
          self.service_mesh = service_mesh
        if service_type is not None:
          self.service_type = service_type
        if status is not None:
          self.status = status
        if hcx_manager_pair is not None:
          self.hcx_manager_pair = hcx_manager_pair
        if running_state is not None:
          self.running_state = running_state

    @property
    def entity_id(self):
        """
        Gets the entity_id of this HCXService.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this HCXService.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this HCXService.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this HCXService.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this HCXService.
        Name of the object

        :return: The name of this HCXService.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HCXService.
        Name of the object

        :param name: The name of this HCXService.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this HCXService.

        :return: The entity_type of this HCXService.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this HCXService.

        :param entity_type: The entity_type of this HCXService.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def service_mesh(self):
        """
        Gets the service_mesh of this HCXService.

        :return: The service_mesh of this HCXService.
        :rtype: Reference
        """
        return self._service_mesh

    @service_mesh.setter
    def service_mesh(self, service_mesh):
        """
        Sets the service_mesh of this HCXService.

        :param service_mesh: The service_mesh of this HCXService.
        :type: Reference
        """

        self._service_mesh = service_mesh

    @property
    def service_type(self):
        """
        Gets the service_type of this HCXService.

        :return: The service_type of this HCXService.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """
        Sets the service_type of this HCXService.

        :param service_type: The service_type of this HCXService.
        :type: str
        """

        self._service_type = service_type

    @property
    def status(self):
        """
        Gets the status of this HCXService.

        :return: The status of this HCXService.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this HCXService.

        :param status: The status of this HCXService.
        :type: str
        """

        self._status = status

    @property
    def hcx_manager_pair(self):
        """
        Gets the hcx_manager_pair of this HCXService.

        :return: The hcx_manager_pair of this HCXService.
        :rtype: list[Reference]
        """
        return self._hcx_manager_pair

    @hcx_manager_pair.setter
    def hcx_manager_pair(self, hcx_manager_pair):
        """
        Sets the hcx_manager_pair of this HCXService.

        :param hcx_manager_pair: The hcx_manager_pair of this HCXService.
        :type: list[Reference]
        """

        self._hcx_manager_pair = hcx_manager_pair

    @property
    def running_state(self):
        """
        Gets the running_state of this HCXService.

        :return: The running_state of this HCXService.
        :rtype: str
        """
        return self._running_state

    @running_state.setter
    def running_state(self, running_state):
        """
        Sets the running_state of this HCXService.

        :param running_state: The running_state of this HCXService.
        :type: str
        """

        self._running_state = running_state

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
        if not isinstance(other, HCXService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other