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


class ValidateConnectionViaWebProxyResponseList(object):
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
        'results': 'list[ValidateConnectionViaWebProxyResponse]'
    }

    attribute_map = {
        'results': 'results'
    }

    def __init__(self, results=None):
        """
        ValidateConnectionViaWebProxyResponseList - a model defined in Swagger
        """

        self._results = None

        if results is not None:
          self.results = results

    @property
    def results(self):
        """
        Gets the results of this ValidateConnectionViaWebProxyResponseList.

        :return: The results of this ValidateConnectionViaWebProxyResponseList.
        :rtype: list[ValidateConnectionViaWebProxyResponse]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this ValidateConnectionViaWebProxyResponseList.

        :param results: The results of this ValidateConnectionViaWebProxyResponseList.
        :type: list[ValidateConnectionViaWebProxyResponse]
        """

        self._results = results

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
        if not isinstance(other, ValidateConnectionViaWebProxyResponseList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
