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


class IncompleteSessionDrillDownListResponse(object):
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
        'results': 'list[IncompleteSessionDrillDownResponse]',
        'start_time': 'int',
        'end_time': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'results': 'results',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'total_count': 'total_count'
    }

    def __init__(self, results=None, start_time=None, end_time=None, total_count=None):
        """
        IncompleteSessionDrillDownListResponse - a model defined in Swagger
        """

        self._results = None
        self._start_time = None
        self._end_time = None
        self._total_count = None

        if results is not None:
          self.results = results
        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time
        if total_count is not None:
          self.total_count = total_count

    @property
    def results(self):
        """
        Gets the results of this IncompleteSessionDrillDownListResponse.

        :return: The results of this IncompleteSessionDrillDownListResponse.
        :rtype: list[IncompleteSessionDrillDownResponse]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this IncompleteSessionDrillDownListResponse.

        :param results: The results of this IncompleteSessionDrillDownListResponse.
        :type: list[IncompleteSessionDrillDownResponse]
        """

        self._results = results

    @property
    def start_time(self):
        """
        Gets the start_time of this IncompleteSessionDrillDownListResponse.

        :return: The start_time of this IncompleteSessionDrillDownListResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this IncompleteSessionDrillDownListResponse.

        :param start_time: The start_time of this IncompleteSessionDrillDownListResponse.
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this IncompleteSessionDrillDownListResponse.

        :return: The end_time of this IncompleteSessionDrillDownListResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this IncompleteSessionDrillDownListResponse.

        :param end_time: The end_time of this IncompleteSessionDrillDownListResponse.
        :type: int
        """

        self._end_time = end_time

    @property
    def total_count(self):
        """
        Gets the total_count of this IncompleteSessionDrillDownListResponse.

        :return: The total_count of this IncompleteSessionDrillDownListResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this IncompleteSessionDrillDownListResponse.

        :param total_count: The total_count of this IncompleteSessionDrillDownListResponse.
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, IncompleteSessionDrillDownListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other