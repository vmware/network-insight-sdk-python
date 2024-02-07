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


class SNMPEngineId(object):
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
        'engine_id': 'str'
    }

    attribute_map = {
        'engine_id': 'engine_id'
    }

    def __init__(self, engine_id=None):
        """
        SNMPEngineId - a model defined in Swagger
        """

        self._engine_id = None

        if engine_id is not None:
          self.engine_id = engine_id

    @property
    def engine_id(self):
        """
        Gets the engine_id of this SNMPEngineId.
        SNMP Engine ID as a hexadecimal string

        :return: The engine_id of this SNMPEngineId.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """
        Sets the engine_id of this SNMPEngineId.
        SNMP Engine ID as a hexadecimal string

        :param engine_id: The engine_id of this SNMPEngineId.
        :type: str
        """

        self._engine_id = engine_id

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
        if not isinstance(other, SNMPEngineId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other