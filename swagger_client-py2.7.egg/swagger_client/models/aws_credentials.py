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


class AWSCredentials(object):
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
        'access_key': 'str',
        'secret_key': 'str'
    }

    attribute_map = {
        'access_key': 'access_key',
        'secret_key': 'secret_key'
    }

    def __init__(self, access_key=None, secret_key=None):
        """
        AWSCredentials - a model defined in Swagger
        """

        self._access_key = None
        self._secret_key = None

        self.access_key = access_key
        if secret_key is not None:
          self.secret_key = secret_key

    @property
    def access_key(self):
        """
        Gets the access_key of this AWSCredentials.
        AWS Access Key to authenticate with

        :return: The access_key of this AWSCredentials.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """
        Sets the access_key of this AWSCredentials.
        AWS Access Key to authenticate with

        :param access_key: The access_key of this AWSCredentials.
        :type: str
        """
        if access_key is None:
            raise ValueError("Invalid value for `access_key`, must not be `None`")

        self._access_key = access_key

    @property
    def secret_key(self):
        """
        Gets the secret_key of this AWSCredentials.
        AWS Secret Key to authenticate with

        :return: The secret_key of this AWSCredentials.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """
        Sets the secret_key of this AWSCredentials.
        AWS Secret Key to authenticate with

        :param secret_key: The secret_key of this AWSCredentials.
        :type: str
        """

        self._secret_key = secret_key

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
        if not isinstance(other, AWSCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
