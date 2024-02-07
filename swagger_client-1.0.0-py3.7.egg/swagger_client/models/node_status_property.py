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


class NodeStatusProperty(object):
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
        'cpu_cores': 'int',
        'total_ram': 'int',
        'total_swap': 'int'
    }

    attribute_map = {
        'cpu_cores': 'cpu_cores',
        'total_ram': 'total_ram',
        'total_swap': 'total_swap'
    }

    def __init__(self, cpu_cores=None, total_ram=None, total_swap=None):
        """
        NodeStatusProperty - a model defined in Swagger
        """

        self._cpu_cores = None
        self._total_ram = None
        self._total_swap = None

        if cpu_cores is not None:
          self.cpu_cores = cpu_cores
        if total_ram is not None:
          self.total_ram = total_ram
        if total_swap is not None:
          self.total_swap = total_swap

    @property
    def cpu_cores(self):
        """
        Gets the cpu_cores of this NodeStatusProperty.

        :return: The cpu_cores of this NodeStatusProperty.
        :rtype: int
        """
        return self._cpu_cores

    @cpu_cores.setter
    def cpu_cores(self, cpu_cores):
        """
        Sets the cpu_cores of this NodeStatusProperty.

        :param cpu_cores: The cpu_cores of this NodeStatusProperty.
        :type: int
        """

        self._cpu_cores = cpu_cores

    @property
    def total_ram(self):
        """
        Gets the total_ram of this NodeStatusProperty.

        :return: The total_ram of this NodeStatusProperty.
        :rtype: int
        """
        return self._total_ram

    @total_ram.setter
    def total_ram(self, total_ram):
        """
        Sets the total_ram of this NodeStatusProperty.

        :param total_ram: The total_ram of this NodeStatusProperty.
        :type: int
        """

        self._total_ram = total_ram

    @property
    def total_swap(self):
        """
        Gets the total_swap of this NodeStatusProperty.

        :return: The total_swap of this NodeStatusProperty.
        :rtype: int
        """
        return self._total_swap

    @total_swap.setter
    def total_swap(self, total_swap):
        """
        Sets the total_swap of this NodeStatusProperty.

        :param total_swap: The total_swap of this NodeStatusProperty.
        :type: int
        """

        self._total_swap = total_swap

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
        if not isinstance(other, NodeStatusProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other