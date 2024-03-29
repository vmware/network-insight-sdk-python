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


class SaveBulkDiscoveredAppResponse(object):
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
        'request_id': 'str',
        'callback_api': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'callback_api': 'callback_API'
    }

    def __init__(self, request_id=None, callback_api=None):
        """
        SaveBulkDiscoveredAppResponse - a model defined in Swagger
        """

        self._request_id = None
        self._callback_api = None

        if request_id is not None:
          self.request_id = request_id
        if callback_api is not None:
          self.callback_api = callback_api

    @property
    def request_id(self):
        """
        Gets the request_id of this SaveBulkDiscoveredAppResponse.
        RequestId of bulk application save request.

        :return: The request_id of this SaveBulkDiscoveredAppResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this SaveBulkDiscoveredAppResponse.
        RequestId of bulk application save request.

        :param request_id: The request_id of this SaveBulkDiscoveredAppResponse.
        :type: str
        """

        self._request_id = request_id

    @property
    def callback_api(self):
        """
        Gets the callback_api of this SaveBulkDiscoveredAppResponse.
        Path of API which should be called to check status of bulk application save request.

        :return: The callback_api of this SaveBulkDiscoveredAppResponse.
        :rtype: str
        """
        return self._callback_api

    @callback_api.setter
    def callback_api(self, callback_api):
        """
        Sets the callback_api of this SaveBulkDiscoveredAppResponse.
        Path of API which should be called to check status of bulk application save request.

        :param callback_api: The callback_api of this SaveBulkDiscoveredAppResponse.
        :type: str
        """

        self._callback_api = callback_api

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
        if not isinstance(other, SaveBulkDiscoveredAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
