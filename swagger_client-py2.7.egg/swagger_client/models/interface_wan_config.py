# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InterfaceWANConfig(object):
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
        'id': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, type=None):
        """
        InterfaceWANConfig - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._type = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if type is not None:
          self.type = type

    @property
    def id(self):
        """
        Gets the id of this InterfaceWANConfig.

        :return: The id of this InterfaceWANConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InterfaceWANConfig.

        :param id: The id of this InterfaceWANConfig.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this InterfaceWANConfig.

        :return: The name of this InterfaceWANConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InterfaceWANConfig.

        :param name: The name of this InterfaceWANConfig.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this InterfaceWANConfig.

        :return: The type of this InterfaceWANConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InterfaceWANConfig.

        :param type: The type of this InterfaceWANConfig.
        :type: str
        """
        allowed_values = ["MPLS", "INTERNET", "OTHER"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, InterfaceWANConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
