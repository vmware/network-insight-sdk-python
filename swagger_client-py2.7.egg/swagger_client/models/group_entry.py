# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GroupEntry(object):
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
        'group_id': 'str',
        'entity_id': 'str',
        'entity_type': 'str',
        'flow_summary': 'FlowSummary'
    }

    attribute_map = {
        'group_id': 'group_id',
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'flow_summary': 'flow_summary'
    }

    def __init__(self, group_id=None, entity_id=None, entity_type=None, flow_summary=None):
        """
        GroupEntry - a model defined in Swagger
        """

        self._group_id = None
        self._entity_id = None
        self._entity_type = None
        self._flow_summary = None

        if group_id is not None:
          self.group_id = group_id
        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if flow_summary is not None:
          self.flow_summary = flow_summary

    @property
    def group_id(self):
        """
        Gets the group_id of this GroupEntry.

        :return: The group_id of this GroupEntry.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this GroupEntry.

        :param group_id: The group_id of this GroupEntry.
        :type: str
        """

        self._group_id = group_id

    @property
    def entity_id(self):
        """
        Gets the entity_id of this GroupEntry.

        :return: The entity_id of this GroupEntry.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this GroupEntry.

        :param entity_id: The entity_id of this GroupEntry.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this GroupEntry.

        :return: The entity_type of this GroupEntry.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this GroupEntry.

        :param entity_type: The entity_type of this GroupEntry.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def flow_summary(self):
        """
        Gets the flow_summary of this GroupEntry.

        :return: The flow_summary of this GroupEntry.
        :rtype: FlowSummary
        """
        return self._flow_summary

    @flow_summary.setter
    def flow_summary(self, flow_summary):
        """
        Sets the flow_summary of this GroupEntry.

        :param flow_summary: The flow_summary of this GroupEntry.
        :type: FlowSummary
        """

        self._flow_summary = flow_summary

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
        if not isinstance(other, GroupEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
