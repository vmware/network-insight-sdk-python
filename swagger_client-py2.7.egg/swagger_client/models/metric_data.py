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


class MetricData(object):
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
        'metric': 'str',
        'interval': 'int',
        'timestamp': 'int',
        'unit': 'str',
        'entity_type': 'EntityType',
        'points': 'list[EntityMetricValue]'
    }

    attribute_map = {
        'metric': 'metric',
        'interval': 'interval',
        'timestamp': 'timestamp',
        'unit': 'unit',
        'entity_type': 'entity_type',
        'points': 'points'
    }

    def __init__(self, metric=None, interval=None, timestamp=None, unit=None, entity_type=None, points=None):
        """
        MetricData - a model defined in Swagger
        """

        self._metric = None
        self._interval = None
        self._timestamp = None
        self._unit = None
        self._entity_type = None
        self._points = None

        if metric is not None:
          self.metric = metric
        if interval is not None:
          self.interval = interval
        if timestamp is not None:
          self.timestamp = timestamp
        if unit is not None:
          self.unit = unit
        if entity_type is not None:
          self.entity_type = entity_type
        if points is not None:
          self.points = points

    @property
    def metric(self):
        """
        Gets the metric of this MetricData.
        Name of the metric

        :return: The metric of this MetricData.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this MetricData.
        Name of the metric

        :param metric: The metric of this MetricData.
        :type: str
        """

        self._metric = metric

    @property
    def interval(self):
        """
        Gets the interval of this MetricData.

        :return: The interval of this MetricData.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this MetricData.

        :param interval: The interval of this MetricData.
        :type: int
        """

        self._interval = interval

    @property
    def timestamp(self):
        """
        Gets the timestamp of this MetricData.

        :return: The timestamp of this MetricData.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this MetricData.

        :param timestamp: The timestamp of this MetricData.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def unit(self):
        """
        Gets the unit of this MetricData.

        :return: The unit of this MetricData.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this MetricData.

        :param unit: The unit of this MetricData.
        :type: str
        """

        self._unit = unit

    @property
    def entity_type(self):
        """
        Gets the entity_type of this MetricData.

        :return: The entity_type of this MetricData.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this MetricData.

        :param entity_type: The entity_type of this MetricData.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def points(self):
        """
        Gets the points of this MetricData.

        :return: The points of this MetricData.
        :rtype: list[EntityMetricValue]
        """
        return self._points

    @points.setter
    def points(self, points):
        """
        Sets the points of this MetricData.

        :param points: The points of this MetricData.
        :type: list[EntityMetricValue]
        """

        self._points = points

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
        if not isinstance(other, MetricData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
