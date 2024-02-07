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


class FlowPropertiesResponse(object):
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
        'property_type': 'str',
        'count': 'int',
        'query': 'str'
    }

    attribute_map = {
        'property_type': 'property_type',
        'count': 'count',
        'query': 'query'
    }

    def __init__(self, property_type=None, count=None, query=None):
        """
        FlowPropertiesResponse - a model defined in Swagger
        """

        self._property_type = None
        self._count = None
        self._query = None

        if property_type is not None:
          self.property_type = property_type
        if count is not None:
          self.count = count
        if query is not None:
          self.query = query

    @property
    def property_type(self):
        """
        Gets the property_type of this FlowPropertiesResponse.

        :return: The property_type of this FlowPropertiesResponse.
        :rtype: str
        """
        return self._property_type

    @property_type.setter
    def property_type(self, property_type):
        """
        Sets the property_type of this FlowPropertiesResponse.

        :param property_type: The property_type of this FlowPropertiesResponse.
        :type: str
        """

        self._property_type = property_type

    @property
    def count(self):
        """
        Gets the count of this FlowPropertiesResponse.

        :return: The count of this FlowPropertiesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this FlowPropertiesResponse.

        :param count: The count of this FlowPropertiesResponse.
        :type: int
        """

        self._count = count

    @property
    def query(self):
        """
        Gets the query of this FlowPropertiesResponse.

        :return: The query of this FlowPropertiesResponse.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this FlowPropertiesResponse.

        :param query: The query of this FlowPropertiesResponse.
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
        if not isinstance(other, FlowPropertiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
