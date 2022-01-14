# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 6.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PolicyManagerSegment(object):
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
        'realized_entities': 'list[Reference]',
        'sddc_type': 'SddcType',
        'network_type': 'str',
        'unique_id': 'str',
        'enforcement_point_uuid': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'network_addresses': 'network_addresses',
        'gateways': 'gateways',
        'realized_entities': 'realized_entities',
        'sddc_type': 'sddc_type',
        'network_type': 'network_type',
        'unique_id': 'unique_id',
        'enforcement_point_uuid': 'enforcement_point_uuid'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, network_addresses=None, gateways=None, realized_entities=None, sddc_type=None, network_type=None, unique_id=None, enforcement_point_uuid=None):
        """
        PolicyManagerSegment - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._network_addresses = None
        self._gateways = None
        self._realized_entities = None
        self._sddc_type = None
        self._network_type = None
        self._unique_id = None
        self._enforcement_point_uuid = None

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
        if realized_entities is not None:
          self.realized_entities = realized_entities
        if sddc_type is not None:
          self.sddc_type = sddc_type
        if network_type is not None:
          self.network_type = network_type
        if unique_id is not None:
          self.unique_id = unique_id
        if enforcement_point_uuid is not None:
          self.enforcement_point_uuid = enforcement_point_uuid

    @property
    def entity_id(self):
        """
        Gets the entity_id of this PolicyManagerSegment.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this PolicyManagerSegment.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this PolicyManagerSegment.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this PolicyManagerSegment.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this PolicyManagerSegment.
        Name of the object

        :return: The name of this PolicyManagerSegment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyManagerSegment.
        Name of the object

        :param name: The name of this PolicyManagerSegment.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this PolicyManagerSegment.

        :return: The entity_type of this PolicyManagerSegment.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this PolicyManagerSegment.

        :param entity_type: The entity_type of this PolicyManagerSegment.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def network_addresses(self):
        """
        Gets the network_addresses of this PolicyManagerSegment.

        :return: The network_addresses of this PolicyManagerSegment.
        :rtype: list[str]
        """
        return self._network_addresses

    @network_addresses.setter
    def network_addresses(self, network_addresses):
        """
        Sets the network_addresses of this PolicyManagerSegment.

        :param network_addresses: The network_addresses of this PolicyManagerSegment.
        :type: list[str]
        """

        self._network_addresses = network_addresses

    @property
    def gateways(self):
        """
        Gets the gateways of this PolicyManagerSegment.

        :return: The gateways of this PolicyManagerSegment.
        :rtype: list[str]
        """
        return self._gateways

    @gateways.setter
    def gateways(self, gateways):
        """
        Sets the gateways of this PolicyManagerSegment.

        :param gateways: The gateways of this PolicyManagerSegment.
        :type: list[str]
        """

        self._gateways = gateways

    @property
    def realized_entities(self):
        """
        Gets the realized_entities of this PolicyManagerSegment.

        :return: The realized_entities of this PolicyManagerSegment.
        :rtype: list[Reference]
        """
        return self._realized_entities

    @realized_entities.setter
    def realized_entities(self, realized_entities):
        """
        Sets the realized_entities of this PolicyManagerSegment.

        :param realized_entities: The realized_entities of this PolicyManagerSegment.
        :type: list[Reference]
        """

        self._realized_entities = realized_entities

    @property
    def sddc_type(self):
        """
        Gets the sddc_type of this PolicyManagerSegment.

        :return: The sddc_type of this PolicyManagerSegment.
        :rtype: SddcType
        """
        return self._sddc_type

    @sddc_type.setter
    def sddc_type(self, sddc_type):
        """
        Sets the sddc_type of this PolicyManagerSegment.

        :param sddc_type: The sddc_type of this PolicyManagerSegment.
        :type: SddcType
        """

        self._sddc_type = sddc_type

    @property
    def network_type(self):
        """
        Gets the network_type of this PolicyManagerSegment.

        :return: The network_type of this PolicyManagerSegment.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """
        Sets the network_type of this PolicyManagerSegment.

        :param network_type: The network_type of this PolicyManagerSegment.
        :type: str
        """

        self._network_type = network_type

    @property
    def unique_id(self):
        """
        Gets the unique_id of this PolicyManagerSegment.
        Unique ID of L2 Segment

        :return: The unique_id of this PolicyManagerSegment.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """
        Sets the unique_id of this PolicyManagerSegment.
        Unique ID of L2 Segment

        :param unique_id: The unique_id of this PolicyManagerSegment.
        :type: str
        """

        self._unique_id = unique_id

    @property
    def enforcement_point_uuid(self):
        """
        Gets the enforcement_point_uuid of this PolicyManagerSegment.
        Enforcement Point Unique ID of L2 Segment

        :return: The enforcement_point_uuid of this PolicyManagerSegment.
        :rtype: str
        """
        return self._enforcement_point_uuid

    @enforcement_point_uuid.setter
    def enforcement_point_uuid(self, enforcement_point_uuid):
        """
        Sets the enforcement_point_uuid of this PolicyManagerSegment.
        Enforcement Point Unique ID of L2 Segment

        :param enforcement_point_uuid: The enforcement_point_uuid of this PolicyManagerSegment.
        :type: str
        """

        self._enforcement_point_uuid = enforcement_point_uuid

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
        if not isinstance(other, PolicyManagerSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
