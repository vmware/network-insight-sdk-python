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


class BasicUpdateInfo(object):
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
        'name': 'str',
        'entity_id': 'str',
        'update_status': 'UpdateStatus'
    }

    attribute_map = {
        'name': 'name',
        'entity_id': 'entity_id',
        'update_status': 'update_status'
    }

    def __init__(self, name=None, entity_id=None, update_status=None):
        """
        BasicUpdateInfo - a model defined in Swagger
        """

        self._name = None
        self._entity_id = None
        self._update_status = None

        if name is not None:
          self.name = name
        if entity_id is not None:
          self.entity_id = entity_id
        if update_status is not None:
          self.update_status = update_status

    @property
    def name(self):
        """
        Gets the name of this BasicUpdateInfo.

        :return: The name of this BasicUpdateInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BasicUpdateInfo.

        :param name: The name of this BasicUpdateInfo.
        :type: str
        """

        self._name = name

    @property
    def entity_id(self):
        """
        Gets the entity_id of this BasicUpdateInfo.

        :return: The entity_id of this BasicUpdateInfo.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this BasicUpdateInfo.

        :param entity_id: The entity_id of this BasicUpdateInfo.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def update_status(self):
        """
        Gets the update_status of this BasicUpdateInfo.

        :return: The update_status of this BasicUpdateInfo.
        :rtype: UpdateStatus
        """
        return self._update_status

    @update_status.setter
    def update_status(self, update_status):
        """
        Sets the update_status of this BasicUpdateInfo.

        :param update_status: The update_status of this BasicUpdateInfo.
        :type: UpdateStatus
        """

        self._update_status = update_status

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
        if not isinstance(other, BasicUpdateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
