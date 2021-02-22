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


class LicenseUsageInner(object):
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
        'type': 'LicenseUsageObject',
        'unit': 'LicenseUsageCapacity',
        'count': 'int',
        'sockets_used': 'int',
        'cores_used': 'int',
        'edges_used': 'int',
        'devices_used': 'int',
        'query': 'str'
    }

    attribute_map = {
        'type': 'type',
        'unit': 'unit',
        'count': 'count',
        'sockets_used': 'socketsUsed',
        'cores_used': 'coresUsed',
        'edges_used': 'edgesUsed',
        'devices_used': 'devicesUsed',
        'query': 'query'
    }

    def __init__(self, type=None, unit=None, count=None, sockets_used=None, cores_used=None, edges_used=None, devices_used=None, query=None):
        """
        LicenseUsageInner - a model defined in Swagger
        """

        self._type = None
        self._unit = None
        self._count = None
        self._sockets_used = None
        self._cores_used = None
        self._edges_used = None
        self._devices_used = None
        self._query = None

        if type is not None:
          self.type = type
        if unit is not None:
          self.unit = unit
        if count is not None:
          self.count = count
        if sockets_used is not None:
          self.sockets_used = sockets_used
        if cores_used is not None:
          self.cores_used = cores_used
        if edges_used is not None:
          self.edges_used = edges_used
        if devices_used is not None:
          self.devices_used = devices_used
        if query is not None:
          self.query = query

    @property
    def type(self):
        """
        Gets the type of this LicenseUsageInner.

        :return: The type of this LicenseUsageInner.
        :rtype: LicenseUsageObject
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LicenseUsageInner.

        :param type: The type of this LicenseUsageInner.
        :type: LicenseUsageObject
        """

        self._type = type

    @property
    def unit(self):
        """
        Gets the unit of this LicenseUsageInner.

        :return: The unit of this LicenseUsageInner.
        :rtype: LicenseUsageCapacity
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this LicenseUsageInner.

        :param unit: The unit of this LicenseUsageInner.
        :type: LicenseUsageCapacity
        """

        self._unit = unit

    @property
    def count(self):
        """
        Gets the count of this LicenseUsageInner.
        Count for entitlement in use

        :return: The count of this LicenseUsageInner.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this LicenseUsageInner.
        Count for entitlement in use

        :param count: The count of this LicenseUsageInner.
        :type: int
        """

        self._count = count

    @property
    def sockets_used(self):
        """
        Gets the sockets_used of this LicenseUsageInner.
        Count for sockets in use

        :return: The sockets_used of this LicenseUsageInner.
        :rtype: int
        """
        return self._sockets_used

    @sockets_used.setter
    def sockets_used(self, sockets_used):
        """
        Sets the sockets_used of this LicenseUsageInner.
        Count for sockets in use

        :param sockets_used: The sockets_used of this LicenseUsageInner.
        :type: int
        """

        self._sockets_used = sockets_used

    @property
    def cores_used(self):
        """
        Gets the cores_used of this LicenseUsageInner.
        Count for cores in use

        :return: The cores_used of this LicenseUsageInner.
        :rtype: int
        """
        return self._cores_used

    @cores_used.setter
    def cores_used(self, cores_used):
        """
        Sets the cores_used of this LicenseUsageInner.
        Count for cores in use

        :param cores_used: The cores_used of this LicenseUsageInner.
        :type: int
        """

        self._cores_used = cores_used

    @property
    def edges_used(self):
        """
        Gets the edges_used of this LicenseUsageInner.
        Count for edges in use

        :return: The edges_used of this LicenseUsageInner.
        :rtype: int
        """
        return self._edges_used

    @edges_used.setter
    def edges_used(self, edges_used):
        """
        Sets the edges_used of this LicenseUsageInner.
        Count for edges in use

        :param edges_used: The edges_used of this LicenseUsageInner.
        :type: int
        """

        self._edges_used = edges_used

    @property
    def devices_used(self):
        """
        Gets the devices_used of this LicenseUsageInner.
        Count for edges in use

        :return: The devices_used of this LicenseUsageInner.
        :rtype: int
        """
        return self._devices_used

    @devices_used.setter
    def devices_used(self, devices_used):
        """
        Sets the devices_used of this LicenseUsageInner.
        Count for edges in use

        :param devices_used: The devices_used of this LicenseUsageInner.
        :type: int
        """

        self._devices_used = devices_used

    @property
    def query(self):
        """
        Gets the query of this LicenseUsageInner.
        Search query used to calculate the usage

        :return: The query of this LicenseUsageInner.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this LicenseUsageInner.
        Search query used to calculate the usage

        :param query: The query of this LicenseUsageInner.
        :type: str
        """

        self._query = query

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
        if not isinstance(other, LicenseUsageInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
