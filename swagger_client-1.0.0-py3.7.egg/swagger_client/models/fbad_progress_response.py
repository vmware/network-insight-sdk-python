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


class FBADProgressResponse(object):
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
        'last_success': 'int',
        'progress': 'float',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'last_success': 'last_success',
        'progress': 'progress',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, last_success=-1, progress=0.0, error_code='', error_message=''):
        """
        FBADProgressResponse - a model defined in Swagger
        """

        self._last_success = None
        self._progress = None
        self._error_code = None
        self._error_message = None

        if last_success is not None:
          self.last_success = last_success
        if progress is not None:
          self.progress = progress
        if error_code is not None:
          self.error_code = error_code
        if error_message is not None:
          self.error_message = error_message

    @property
    def last_success(self):
        """
        Gets the last_success of this FBADProgressResponse.
        The timestamp of when flow based application discovery was last successful

        :return: The last_success of this FBADProgressResponse.
        :rtype: int
        """
        return self._last_success

    @last_success.setter
    def last_success(self, last_success):
        """
        Sets the last_success of this FBADProgressResponse.
        The timestamp of when flow based application discovery was last successful

        :param last_success: The last_success of this FBADProgressResponse.
        :type: int
        """

        self._last_success = last_success

    @property
    def progress(self):
        """
        Gets the progress of this FBADProgressResponse.
        The current progress percentage of flow based application discovery task. It will be set to 100 if no flow based discovery task is currently running

        :return: The progress of this FBADProgressResponse.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this FBADProgressResponse.
        The current progress percentage of flow based application discovery task. It will be set to 100 if no flow based discovery task is currently running

        :param progress: The progress of this FBADProgressResponse.
        :type: float
        """

        self._progress = progress

    @property
    def error_code(self):
        """
        Gets the error_code of this FBADProgressResponse.
        Error code of the error that occurs during flow based application discovery

        :return: The error_code of this FBADProgressResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this FBADProgressResponse.
        Error code of the error that occurs during flow based application discovery

        :param error_code: The error_code of this FBADProgressResponse.
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """
        Gets the error_message of this FBADProgressResponse.
        Detailed description of the error that occurs during flow based application discovery

        :return: The error_message of this FBADProgressResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this FBADProgressResponse.
        Detailed description of the error that occurs during flow based application discovery

        :param error_message: The error_message of this FBADProgressResponse.
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
        if not isinstance(other, FBADProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
