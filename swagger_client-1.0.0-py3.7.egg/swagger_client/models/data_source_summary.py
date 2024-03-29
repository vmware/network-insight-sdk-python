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


class DataSourceSummary(object):
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
        'customer_id': 'int',
        'data_sources_count': 'int'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'data_sources_count': 'dataSourcesCount'
    }

    def __init__(self, customer_id=None, data_sources_count=None):
        """
        DataSourceSummary - a model defined in Swagger
        """

        self._customer_id = None
        self._data_sources_count = None

        if customer_id is not None:
          self.customer_id = customer_id
        if data_sources_count is not None:
          self.data_sources_count = data_sources_count

    @property
    def customer_id(self):
        """
        Gets the customer_id of this DataSourceSummary.
        customerId

        :return: The customer_id of this DataSourceSummary.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this DataSourceSummary.
        customerId

        :param customer_id: The customer_id of this DataSourceSummary.
        :type: int
        """

        self._customer_id = customer_id

    @property
    def data_sources_count(self):
        """
        Gets the data_sources_count of this DataSourceSummary.
        Count of data sources

        :return: The data_sources_count of this DataSourceSummary.
        :rtype: int
        """
        return self._data_sources_count

    @data_sources_count.setter
    def data_sources_count(self, data_sources_count):
        """
        Sets the data_sources_count of this DataSourceSummary.
        Count of data sources

        :param data_sources_count: The data_sources_count of this DataSourceSummary.
        :type: int
        """

        self._data_sources_count = data_sources_count

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
        if not isinstance(other, DataSourceSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
