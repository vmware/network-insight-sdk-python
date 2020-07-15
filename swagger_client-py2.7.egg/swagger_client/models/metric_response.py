# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MetricResponse(object):
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
        'display_name': 'str',
        'interval': 'int',
        'unit': 'str',
        'pointlist': 'list[list[float]]',
        'start': 'int',
        'end': 'int'
    }

    attribute_map = {
        'metric': 'metric',
        'display_name': 'display_name',
        'interval': 'interval',
        'unit': 'unit',
        'pointlist': 'pointlist',
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, metric=None, display_name=None, interval=None, unit=None, pointlist=None, start=None, end=None):
        """
        MetricResponse - a model defined in Swagger
        """

        self._metric = None
        self._display_name = None
        self._interval = None
        self._unit = None
        self._pointlist = None
        self._start = None
        self._end = None

        if metric is not None:
          self.metric = metric
        if display_name is not None:
          self.display_name = display_name
        if interval is not None:
          self.interval = interval
        if unit is not None:
          self.unit = unit
        if pointlist is not None:
          self.pointlist = pointlist
        if start is not None:
          self.start = start
        if end is not None:
          self.end = end

    @property
    def metric(self):
        """
        Gets the metric of this MetricResponse.

        :return: The metric of this MetricResponse.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this MetricResponse.

        :param metric: The metric of this MetricResponse.
        :type: str
        """

        self._metric = metric

    @property
    def display_name(self):
        """
        Gets the display_name of this MetricResponse.

        :return: The display_name of this MetricResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MetricResponse.

        :param display_name: The display_name of this MetricResponse.
        :type: str
        """

        self._display_name = display_name

    @property
    def interval(self):
        """
        Gets the interval of this MetricResponse.

        :return: The interval of this MetricResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this MetricResponse.

        :param interval: The interval of this MetricResponse.
        :type: int
        """

        self._interval = interval

    @property
    def unit(self):
        """
        Gets the unit of this MetricResponse.

        :return: The unit of this MetricResponse.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this MetricResponse.

        :param unit: The unit of this MetricResponse.
        :type: str
        """

        self._unit = unit

    @property
    def pointlist(self):
        """
        Gets the pointlist of this MetricResponse.

        :return: The pointlist of this MetricResponse.
        :rtype: list[list[float]]
        """
        return self._pointlist

    @pointlist.setter
    def pointlist(self, pointlist):
        """
        Sets the pointlist of this MetricResponse.

        :param pointlist: The pointlist of this MetricResponse.
        :type: list[list[float]]
        """

        self._pointlist = pointlist

    @property
    def start(self):
        """
        Gets the start of this MetricResponse.

        :return: The start of this MetricResponse.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this MetricResponse.

        :param start: The start of this MetricResponse.
        :type: int
        """

        self._start = start

    @property
    def end(self):
        """
        Gets the end of this MetricResponse.

        :return: The end of this MetricResponse.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this MetricResponse.

        :param end: The end of this MetricResponse.
        :type: int
        """

        self._end = end

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
        if not isinstance(other, MetricResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
