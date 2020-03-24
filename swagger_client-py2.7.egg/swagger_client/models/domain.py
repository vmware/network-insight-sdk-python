# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Domain(object):
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
        'domain_type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'domain_type': 'domain_type',
        'value': 'value'
    }

    def __init__(self, domain_type=None, value=None):
        """
        Domain - a model defined in Swagger
        """

        self._domain_type = None
        self._value = None

        if domain_type is not None:
          self.domain_type = domain_type
        if value is not None:
          self.value = value

    @property
    def domain_type(self):
        """
        Gets the domain_type of this Domain.

        :return: The domain_type of this Domain.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """
        Sets the domain_type of this Domain.

        :param domain_type: The domain_type of this Domain.
        :type: str
        """
        allowed_values = ["LDAP", "LOCAL"]
        if domain_type not in allowed_values:
            raise ValueError(
                "Invalid value for `domain_type` ({0}), must be one of {1}"
                .format(domain_type, allowed_values)
            )

        self._domain_type = domain_type

    @property
    def value(self):
        """
        Gets the value of this Domain.
        domain value, not required for LOCAL domain

        :return: The value of this Domain.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Domain.
        domain value, not required for LOCAL domain

        :param value: The value of this Domain.
        :type: str
        """

        self._value = value

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
        if not isinstance(other, Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
