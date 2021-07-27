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


class GroupsMembersRequest(object):
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
        'entity_ids': 'list[str]',
        'cursor': 'str'
    }

    attribute_map = {
        'entity_ids': 'entity_ids',
        'cursor': 'cursor'
    }

    def __init__(self, entity_ids=None, cursor=None):
        """
        GroupsMembersRequest - a model defined in Swagger
        """

        self._entity_ids = None
        self._cursor = None

        if entity_ids is not None:
          self.entity_ids = entity_ids
        if cursor is not None:
          self.cursor = cursor

    @property
    def entity_ids(self):
        """
        Gets the entity_ids of this GroupsMembersRequest.

        :return: The entity_ids of this GroupsMembersRequest.
        :rtype: list[str]
        """
        return self._entity_ids

    @entity_ids.setter
    def entity_ids(self, entity_ids):
        """
        Sets the entity_ids of this GroupsMembersRequest.

        :param entity_ids: The entity_ids of this GroupsMembersRequest.
        :type: list[str]
        """

        self._entity_ids = entity_ids

    @property
    def cursor(self):
        """
        Gets the cursor of this GroupsMembersRequest.

        :return: The cursor of this GroupsMembersRequest.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this GroupsMembersRequest.

        :param cursor: The cursor of this GroupsMembersRequest.
        :type: str
        """

        self._cursor = cursor

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
        if not isinstance(other, GroupsMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
