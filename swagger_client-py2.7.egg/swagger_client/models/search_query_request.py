# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SearchQueryRequest(object):
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
        'query': 'str',
        'size': 'int',
        'cursor': 'str',
        'time_range': 'TimeRange'
    }

    attribute_map = {
        'query': 'query',
        'size': 'size',
        'cursor': 'cursor',
        'time_range': 'time_range'
    }

    def __init__(self, query=None, size=None, cursor=None, time_range=None):
        """
        SearchQueryRequest - a model defined in Swagger
        """

        self._query = None
        self._size = None
        self._cursor = None
        self._time_range = None

        if query is not None:
          self.query = query
        if size is not None:
          self.size = size
        if cursor is not None:
          self.cursor = cursor
        if time_range is not None:
          self.time_range = time_range

    @property
    def query(self):
        """
        Gets the query of this SearchQueryRequest.
        Query

        :return: The query of this SearchQueryRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this SearchQueryRequest.
        Query

        :param query: The query of this SearchQueryRequest.
        :type: str
        """

        self._query = query

    @property
    def size(self):
        """
        Gets the size of this SearchQueryRequest.
        Page size of results

        :return: The size of this SearchQueryRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this SearchQueryRequest.
        Page size of results

        :param size: The size of this SearchQueryRequest.
        :type: int
        """

        self._size = size

    @property
    def cursor(self):
        """
        Gets the cursor of this SearchQueryRequest.

        :return: The cursor of this SearchQueryRequest.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this SearchQueryRequest.

        :param cursor: The cursor of this SearchQueryRequest.
        :type: str
        """

        self._cursor = cursor

    @property
    def time_range(self):
        """
        Gets the time_range of this SearchQueryRequest.

        :return: The time_range of this SearchQueryRequest.
        :rtype: TimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """
        Sets the time_range of this SearchQueryRequest.

        :param time_range: The time_range of this SearchQueryRequest.
        :type: TimeRange
        """

        self._time_range = time_range

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
        if not isinstance(other, SearchQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
