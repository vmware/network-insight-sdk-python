# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 6.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SearchRequest(object):
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
        'entity_type': 'AllEntityType',
        'filter': 'str',
        'sort_by': 'SortByClause',
        'size': 'int',
        'cursor': 'str',
        'time_range': 'TimeRange'
    }

    attribute_map = {
        'entity_type': 'entity_type',
        'filter': 'filter',
        'sort_by': 'sort_by',
        'size': 'size',
        'cursor': 'cursor',
        'time_range': 'time_range'
    }

    def __init__(self, entity_type=None, filter=None, sort_by=None, size=None, cursor=None, time_range=None):
        """
        SearchRequest - a model defined in Swagger
        """

        self._entity_type = None
        self._filter = None
        self._sort_by = None
        self._size = None
        self._cursor = None
        self._time_range = None

        if entity_type is not None:
          self.entity_type = entity_type
        if filter is not None:
          self.filter = filter
        if sort_by is not None:
          self.sort_by = sort_by
        if size is not None:
          self.size = size
        if cursor is not None:
          self.cursor = cursor
        if time_range is not None:
          self.time_range = time_range

    @property
    def entity_type(self):
        """
        Gets the entity_type of this SearchRequest.

        :return: The entity_type of this SearchRequest.
        :rtype: AllEntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this SearchRequest.

        :param entity_type: The entity_type of this SearchRequest.
        :type: AllEntityType
        """

        self._entity_type = entity_type

    @property
    def filter(self):
        """
        Gets the filter of this SearchRequest.
        query filter

        :return: The filter of this SearchRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this SearchRequest.
        query filter

        :param filter: The filter of this SearchRequest.
        :type: str
        """

        self._filter = filter

    @property
    def sort_by(self):
        """
        Gets the sort_by of this SearchRequest.

        :return: The sort_by of this SearchRequest.
        :rtype: SortByClause
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """
        Sets the sort_by of this SearchRequest.

        :param sort_by: The sort_by of this SearchRequest.
        :type: SortByClause
        """

        self._sort_by = sort_by

    @property
    def size(self):
        """
        Gets the size of this SearchRequest.

        :return: The size of this SearchRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this SearchRequest.

        :param size: The size of this SearchRequest.
        :type: int
        """

        self._size = size

    @property
    def cursor(self):
        """
        Gets the cursor of this SearchRequest.

        :return: The cursor of this SearchRequest.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this SearchRequest.

        :param cursor: The cursor of this SearchRequest.
        :type: str
        """

        self._cursor = cursor

    @property
    def time_range(self):
        """
        Gets the time_range of this SearchRequest.

        :return: The time_range of this SearchRequest.
        :rtype: TimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """
        Sets the time_range of this SearchRequest.

        :param time_range: The time_range of this SearchRequest.
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
        if not isinstance(other, SearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
