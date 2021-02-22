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


class VPC(object):
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
        'cidr_block': 'IpV4Address',
        'state': 'str',
        'region': 'str',
        'default_vpc': 'bool',
        'vendor_id': 'str',
        'last_synched_time': 'int'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'cidr_block': 'cidr_block',
        'state': 'state',
        'region': 'region',
        'default_vpc': 'default_vpc',
        'vendor_id': 'vendor_id',
        'last_synched_time': 'last_synched_time'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, cidr_block=None, state=None, region=None, default_vpc=None, vendor_id=None, last_synched_time=None):
        """
        VPC - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._cidr_block = None
        self._state = None
        self._region = None
        self._default_vpc = None
        self._vendor_id = None
        self._last_synched_time = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if cidr_block is not None:
          self.cidr_block = cidr_block
        if state is not None:
          self.state = state
        if region is not None:
          self.region = region
        if default_vpc is not None:
          self.default_vpc = default_vpc
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if last_synched_time is not None:
          self.last_synched_time = last_synched_time

    @property
    def entity_id(self):
        """
        Gets the entity_id of this VPC.

        :return: The entity_id of this VPC.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this VPC.

        :param entity_id: The entity_id of this VPC.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this VPC.

        :return: The name of this VPC.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VPC.

        :param name: The name of this VPC.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this VPC.

        :return: The entity_type of this VPC.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this VPC.

        :param entity_type: The entity_type of this VPC.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this VPC.

        :return: The cidr_block of this VPC.
        :rtype: IpV4Address
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this VPC.

        :param cidr_block: The cidr_block of this VPC.
        :type: IpV4Address
        """

        self._cidr_block = cidr_block

    @property
    def state(self):
        """
        Gets the state of this VPC.

        :return: The state of this VPC.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this VPC.

        :param state: The state of this VPC.
        :type: str
        """

        self._state = state

    @property
    def region(self):
        """
        Gets the region of this VPC.

        :return: The region of this VPC.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this VPC.

        :param region: The region of this VPC.
        :type: str
        """

        self._region = region

    @property
    def default_vpc(self):
        """
        Gets the default_vpc of this VPC.

        :return: The default_vpc of this VPC.
        :rtype: bool
        """
        return self._default_vpc

    @default_vpc.setter
    def default_vpc(self, default_vpc):
        """
        Sets the default_vpc of this VPC.

        :param default_vpc: The default_vpc of this VPC.
        :type: bool
        """

        self._default_vpc = default_vpc

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this VPC.

        :return: The vendor_id of this VPC.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this VPC.

        :param vendor_id: The vendor_id of this VPC.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def last_synched_time(self):
        """
        Gets the last_synched_time of this VPC.

        :return: The last_synched_time of this VPC.
        :rtype: int
        """
        return self._last_synched_time

    @last_synched_time.setter
    def last_synched_time(self, last_synched_time):
        """
        Sets the last_synched_time of this VPC.

        :param last_synched_time: The last_synched_time of this VPC.
        :type: int
        """

        self._last_synched_time = last_synched_time

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
        if not isinstance(other, VPC):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
