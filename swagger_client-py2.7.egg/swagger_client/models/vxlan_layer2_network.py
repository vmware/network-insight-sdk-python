# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VxlanLayer2Network(object):
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
        'network_addresses': 'list[str]',
        'gateways': 'list[str]',
        'segment_id': 'int',
        'vteps': 'list[Reference]',
        'scope': 'ScopeEnum',
        'nsx_managers': 'list[Reference]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'network_addresses': 'network_addresses',
        'gateways': 'gateways',
        'segment_id': 'segment_id',
        'vteps': 'vteps',
        'scope': 'scope',
        'nsx_managers': 'nsx_managers'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, network_addresses=None, gateways=None, segment_id=None, vteps=None, scope=None, nsx_managers=None):
        """
        VxlanLayer2Network - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._network_addresses = None
        self._gateways = None
        self._segment_id = None
        self._vteps = None
        self._scope = None
        self._nsx_managers = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if network_addresses is not None:
          self.network_addresses = network_addresses
        if gateways is not None:
          self.gateways = gateways
        if segment_id is not None:
          self.segment_id = segment_id
        if vteps is not None:
          self.vteps = vteps
        if scope is not None:
          self.scope = scope
        if nsx_managers is not None:
          self.nsx_managers = nsx_managers

    @property
    def entity_id(self):
        """
        Gets the entity_id of this VxlanLayer2Network.

        :return: The entity_id of this VxlanLayer2Network.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this VxlanLayer2Network.

        :param entity_id: The entity_id of this VxlanLayer2Network.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this VxlanLayer2Network.

        :return: The name of this VxlanLayer2Network.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VxlanLayer2Network.

        :param name: The name of this VxlanLayer2Network.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this VxlanLayer2Network.

        :return: The entity_type of this VxlanLayer2Network.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this VxlanLayer2Network.

        :param entity_type: The entity_type of this VxlanLayer2Network.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def network_addresses(self):
        """
        Gets the network_addresses of this VxlanLayer2Network.

        :return: The network_addresses of this VxlanLayer2Network.
        :rtype: list[str]
        """
        return self._network_addresses

    @network_addresses.setter
    def network_addresses(self, network_addresses):
        """
        Sets the network_addresses of this VxlanLayer2Network.

        :param network_addresses: The network_addresses of this VxlanLayer2Network.
        :type: list[str]
        """

        self._network_addresses = network_addresses

    @property
    def gateways(self):
        """
        Gets the gateways of this VxlanLayer2Network.

        :return: The gateways of this VxlanLayer2Network.
        :rtype: list[str]
        """
        return self._gateways

    @gateways.setter
    def gateways(self, gateways):
        """
        Sets the gateways of this VxlanLayer2Network.

        :param gateways: The gateways of this VxlanLayer2Network.
        :type: list[str]
        """

        self._gateways = gateways

    @property
    def segment_id(self):
        """
        Gets the segment_id of this VxlanLayer2Network.

        :return: The segment_id of this VxlanLayer2Network.
        :rtype: int
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """
        Sets the segment_id of this VxlanLayer2Network.

        :param segment_id: The segment_id of this VxlanLayer2Network.
        :type: int
        """

        self._segment_id = segment_id

    @property
    def vteps(self):
        """
        Gets the vteps of this VxlanLayer2Network.

        :return: The vteps of this VxlanLayer2Network.
        :rtype: list[Reference]
        """
        return self._vteps

    @vteps.setter
    def vteps(self, vteps):
        """
        Sets the vteps of this VxlanLayer2Network.

        :param vteps: The vteps of this VxlanLayer2Network.
        :type: list[Reference]
        """

        self._vteps = vteps

    @property
    def scope(self):
        """
        Gets the scope of this VxlanLayer2Network.

        :return: The scope of this VxlanLayer2Network.
        :rtype: ScopeEnum
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this VxlanLayer2Network.

        :param scope: The scope of this VxlanLayer2Network.
        :type: ScopeEnum
        """

        self._scope = scope

    @property
    def nsx_managers(self):
        """
        Gets the nsx_managers of this VxlanLayer2Network.

        :return: The nsx_managers of this VxlanLayer2Network.
        :rtype: list[Reference]
        """
        return self._nsx_managers

    @nsx_managers.setter
    def nsx_managers(self, nsx_managers):
        """
        Sets the nsx_managers of this VxlanLayer2Network.

        :param nsx_managers: The nsx_managers of this VxlanLayer2Network.
        :type: list[Reference]
        """

        self._nsx_managers = nsx_managers

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
        if not isinstance(other, VxlanLayer2Network):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
