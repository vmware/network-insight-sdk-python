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


class SaveBulkAppProgressResponse(object):
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
        'entity_id': 'str',
        'name': 'str',
        'response_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'response_code': 'response_code',
        'error_message': 'error_message'
    }

    def __init__(self, entity_id=None, name=None, response_code=None, error_message=None):
        """
        SaveBulkAppProgressResponse - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._response_code = None
        self._error_message = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if response_code is not None:
          self.response_code = response_code
        if error_message is not None:
          self.error_message = error_message

    @property
    def entity_id(self):
        """
        Gets the entity_id of this SaveBulkAppProgressResponse.
        ID of discovered application which was requested to be saved.

        :return: The entity_id of this SaveBulkAppProgressResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this SaveBulkAppProgressResponse.
        ID of discovered application which was requested to be saved.

        :param entity_id: The entity_id of this SaveBulkAppProgressResponse.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this SaveBulkAppProgressResponse.
        Name of discovered application which was requested to be saved.

        :return: The name of this SaveBulkAppProgressResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SaveBulkAppProgressResponse.
        Name of discovered application which was requested to be saved.

        :param name: The name of this SaveBulkAppProgressResponse.
        :type: str
        """

        self._name = name

    @property
    def response_code(self):
        """
        Gets the response_code of this SaveBulkAppProgressResponse.
        Indicates save operation response. eg. SUCCESS

        :return: The response_code of this SaveBulkAppProgressResponse.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this SaveBulkAppProgressResponse.
        Indicates save operation response. eg. SUCCESS

        :param response_code: The response_code of this SaveBulkAppProgressResponse.
        :type: str
        """

        self._response_code = response_code

    @property
    def error_message(self):
        """
        Gets the error_message of this SaveBulkAppProgressResponse.
        Indicates why application could not be saved.

        :return: The error_message of this SaveBulkAppProgressResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this SaveBulkAppProgressResponse.
        Indicates why application could not be saved.

        :param error_message: The error_message of this SaveBulkAppProgressResponse.
        :type: str
        """

        self._error_message = error_message

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
        if not isinstance(other, SaveBulkAppProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
