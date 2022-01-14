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


class VmcAWSDxConnection(object):
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
        'local_asn': 'int',
        'learnt_subnets': 'list[IpV4Address]',
        'advertised_subnets_success': 'list[IpV4Address]',
        'advertised_subnets_failed': 'list[IpV4Address]',
        'dx_tunnels': 'list[DirectConnectInterface]',
        'sddc': 'Reference'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'local_asn': 'local_asn',
        'learnt_subnets': 'learnt_subnets',
        'advertised_subnets_success': 'advertised_subnets_success',
        'advertised_subnets_failed': 'advertised_subnets_failed',
        'dx_tunnels': 'dx_tunnels',
        'sddc': 'sddc'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, local_asn=None, learnt_subnets=None, advertised_subnets_success=None, advertised_subnets_failed=None, dx_tunnels=None, sddc=None):
        """
        VmcAWSDxConnection - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._local_asn = None
        self._learnt_subnets = None
        self._advertised_subnets_success = None
        self._advertised_subnets_failed = None
        self._dx_tunnels = None
        self._sddc = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if local_asn is not None:
          self.local_asn = local_asn
        if learnt_subnets is not None:
          self.learnt_subnets = learnt_subnets
        if advertised_subnets_success is not None:
          self.advertised_subnets_success = advertised_subnets_success
        if advertised_subnets_failed is not None:
          self.advertised_subnets_failed = advertised_subnets_failed
        if dx_tunnels is not None:
          self.dx_tunnels = dx_tunnels
        if sddc is not None:
          self.sddc = sddc

    @property
    def entity_id(self):
        """
        Gets the entity_id of this VmcAWSDxConnection.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this VmcAWSDxConnection.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this VmcAWSDxConnection.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this VmcAWSDxConnection.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this VmcAWSDxConnection.
        Name of the object

        :return: The name of this VmcAWSDxConnection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VmcAWSDxConnection.
        Name of the object

        :param name: The name of this VmcAWSDxConnection.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this VmcAWSDxConnection.

        :return: The entity_type of this VmcAWSDxConnection.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this VmcAWSDxConnection.

        :param entity_type: The entity_type of this VmcAWSDxConnection.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def local_asn(self):
        """
        Gets the local_asn of this VmcAWSDxConnection.

        :return: The local_asn of this VmcAWSDxConnection.
        :rtype: int
        """
        return self._local_asn

    @local_asn.setter
    def local_asn(self, local_asn):
        """
        Sets the local_asn of this VmcAWSDxConnection.

        :param local_asn: The local_asn of this VmcAWSDxConnection.
        :type: int
        """

        self._local_asn = local_asn

    @property
    def learnt_subnets(self):
        """
        Gets the learnt_subnets of this VmcAWSDxConnection.

        :return: The learnt_subnets of this VmcAWSDxConnection.
        :rtype: list[IpV4Address]
        """
        return self._learnt_subnets

    @learnt_subnets.setter
    def learnt_subnets(self, learnt_subnets):
        """
        Sets the learnt_subnets of this VmcAWSDxConnection.

        :param learnt_subnets: The learnt_subnets of this VmcAWSDxConnection.
        :type: list[IpV4Address]
        """

        self._learnt_subnets = learnt_subnets

    @property
    def advertised_subnets_success(self):
        """
        Gets the advertised_subnets_success of this VmcAWSDxConnection.

        :return: The advertised_subnets_success of this VmcAWSDxConnection.
        :rtype: list[IpV4Address]
        """
        return self._advertised_subnets_success

    @advertised_subnets_success.setter
    def advertised_subnets_success(self, advertised_subnets_success):
        """
        Sets the advertised_subnets_success of this VmcAWSDxConnection.

        :param advertised_subnets_success: The advertised_subnets_success of this VmcAWSDxConnection.
        :type: list[IpV4Address]
        """

        self._advertised_subnets_success = advertised_subnets_success

    @property
    def advertised_subnets_failed(self):
        """
        Gets the advertised_subnets_failed of this VmcAWSDxConnection.

        :return: The advertised_subnets_failed of this VmcAWSDxConnection.
        :rtype: list[IpV4Address]
        """
        return self._advertised_subnets_failed

    @advertised_subnets_failed.setter
    def advertised_subnets_failed(self, advertised_subnets_failed):
        """
        Sets the advertised_subnets_failed of this VmcAWSDxConnection.

        :param advertised_subnets_failed: The advertised_subnets_failed of this VmcAWSDxConnection.
        :type: list[IpV4Address]
        """

        self._advertised_subnets_failed = advertised_subnets_failed

    @property
    def dx_tunnels(self):
        """
        Gets the dx_tunnels of this VmcAWSDxConnection.

        :return: The dx_tunnels of this VmcAWSDxConnection.
        :rtype: list[DirectConnectInterface]
        """
        return self._dx_tunnels

    @dx_tunnels.setter
    def dx_tunnels(self, dx_tunnels):
        """
        Sets the dx_tunnels of this VmcAWSDxConnection.

        :param dx_tunnels: The dx_tunnels of this VmcAWSDxConnection.
        :type: list[DirectConnectInterface]
        """

        self._dx_tunnels = dx_tunnels

    @property
    def sddc(self):
        """
        Gets the sddc of this VmcAWSDxConnection.

        :return: The sddc of this VmcAWSDxConnection.
        :rtype: Reference
        """
        return self._sddc

    @sddc.setter
    def sddc(self, sddc):
        """
        Sets the sddc of this VmcAWSDxConnection.

        :param sddc: The sddc of this VmcAWSDxConnection.
        :type: Reference
        """

        self._sddc = sddc

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
        if not isinstance(other, VmcAWSDxConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other