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


class DvsIpfixResponse(object):
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
        'ipfix_enabled_for': 'str',
        'ipfix_disabled_for': 'str',
        'ipfix_disabling_failed': 'str',
        'ipfix_enabling_failed': 'str'
    }

    attribute_map = {
        'ipfix_enabled_for': 'ipfix_enabled_for',
        'ipfix_disabled_for': 'ipfix_disabled_for',
        'ipfix_disabling_failed': 'ipfix_disabling_failed',
        'ipfix_enabling_failed': 'ipfix_enabling_failed'
    }

    def __init__(self, ipfix_enabled_for=None, ipfix_disabled_for=None, ipfix_disabling_failed=None, ipfix_enabling_failed=None):
        """
        DvsIpfixResponse - a model defined in Swagger
        """

        self._ipfix_enabled_for = None
        self._ipfix_disabled_for = None
        self._ipfix_disabling_failed = None
        self._ipfix_enabling_failed = None

        if ipfix_enabled_for is not None:
          self.ipfix_enabled_for = ipfix_enabled_for
        if ipfix_disabled_for is not None:
          self.ipfix_disabled_for = ipfix_disabled_for
        if ipfix_disabling_failed is not None:
          self.ipfix_disabling_failed = ipfix_disabling_failed
        if ipfix_enabling_failed is not None:
          self.ipfix_enabling_failed = ipfix_enabling_failed

    @property
    def ipfix_enabled_for(self):
        """
        Gets the ipfix_enabled_for of this DvsIpfixResponse.

        :return: The ipfix_enabled_for of this DvsIpfixResponse.
        :rtype: str
        """
        return self._ipfix_enabled_for

    @ipfix_enabled_for.setter
    def ipfix_enabled_for(self, ipfix_enabled_for):
        """
        Sets the ipfix_enabled_for of this DvsIpfixResponse.

        :param ipfix_enabled_for: The ipfix_enabled_for of this DvsIpfixResponse.
        :type: str
        """

        self._ipfix_enabled_for = ipfix_enabled_for

    @property
    def ipfix_disabled_for(self):
        """
        Gets the ipfix_disabled_for of this DvsIpfixResponse.

        :return: The ipfix_disabled_for of this DvsIpfixResponse.
        :rtype: str
        """
        return self._ipfix_disabled_for

    @ipfix_disabled_for.setter
    def ipfix_disabled_for(self, ipfix_disabled_for):
        """
        Sets the ipfix_disabled_for of this DvsIpfixResponse.

        :param ipfix_disabled_for: The ipfix_disabled_for of this DvsIpfixResponse.
        :type: str
        """

        self._ipfix_disabled_for = ipfix_disabled_for

    @property
    def ipfix_disabling_failed(self):
        """
        Gets the ipfix_disabling_failed of this DvsIpfixResponse.

        :return: The ipfix_disabling_failed of this DvsIpfixResponse.
        :rtype: str
        """
        return self._ipfix_disabling_failed

    @ipfix_disabling_failed.setter
    def ipfix_disabling_failed(self, ipfix_disabling_failed):
        """
        Sets the ipfix_disabling_failed of this DvsIpfixResponse.

        :param ipfix_disabling_failed: The ipfix_disabling_failed of this DvsIpfixResponse.
        :type: str
        """

        self._ipfix_disabling_failed = ipfix_disabling_failed

    @property
    def ipfix_enabling_failed(self):
        """
        Gets the ipfix_enabling_failed of this DvsIpfixResponse.

        :return: The ipfix_enabling_failed of this DvsIpfixResponse.
        :rtype: str
        """
        return self._ipfix_enabling_failed

    @ipfix_enabling_failed.setter
    def ipfix_enabling_failed(self, ipfix_enabling_failed):
        """
        Sets the ipfix_enabling_failed of this DvsIpfixResponse.

        :param ipfix_enabling_failed: The ipfix_enabling_failed of this DvsIpfixResponse.
        :type: str
        """

        self._ipfix_enabling_failed = ipfix_enabling_failed

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
        if not isinstance(other, DvsIpfixResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
