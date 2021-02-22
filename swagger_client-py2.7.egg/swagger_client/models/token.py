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


class Token(object):
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
        'token': 'str',
        'expiry': 'int'
    }

    attribute_map = {
        'token': 'token',
        'expiry': 'expiry'
    }

    def __init__(self, token=None, expiry=None):
        """
        Token - a model defined in Swagger
        """

        self._token = None
        self._expiry = None

        if token is not None:
          self.token = token
        if expiry is not None:
          self.expiry = expiry

    @property
    def token(self):
        """
        Gets the token of this Token.

        :return: The token of this Token.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this Token.

        :param token: The token of this Token.
        :type: str
        """

        self._token = token

    @property
    def expiry(self):
        """
        Gets the expiry of this Token.
        expiry epoch time in secs.

        :return: The expiry of this Token.
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """
        Sets the expiry of this Token.
        expiry epoch time in secs.

        :param expiry: The expiry of this Token.
        :type: int
        """

        self._expiry = expiry

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
        if not isinstance(other, Token):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
