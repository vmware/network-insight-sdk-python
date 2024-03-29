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


class GraphEdge(object):
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
        'src_id': 'str',
        'dst_id': 'str'
    }

    attribute_map = {
        'src_id': 'srcId',
        'dst_id': 'dstId'
    }

    def __init__(self, src_id=None, dst_id=None):
        """
        GraphEdge - a model defined in Swagger
        """

        self._src_id = None
        self._dst_id = None

        if src_id is not None:
          self.src_id = src_id
        if dst_id is not None:
          self.dst_id = dst_id

    @property
    def src_id(self):
        """
        Gets the src_id of this GraphEdge.

        :return: The src_id of this GraphEdge.
        :rtype: str
        """
        return self._src_id

    @src_id.setter
    def src_id(self, src_id):
        """
        Sets the src_id of this GraphEdge.

        :param src_id: The src_id of this GraphEdge.
        :type: str
        """

        self._src_id = src_id

    @property
    def dst_id(self):
        """
        Gets the dst_id of this GraphEdge.

        :return: The dst_id of this GraphEdge.
        :rtype: str
        """
        return self._dst_id

    @dst_id.setter
    def dst_id(self, dst_id):
        """
        Sets the dst_id of this GraphEdge.

        :param dst_id: The dst_id of this GraphEdge.
        :type: str
        """

        self._dst_id = dst_id

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
        if not isinstance(other, GraphEdge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
