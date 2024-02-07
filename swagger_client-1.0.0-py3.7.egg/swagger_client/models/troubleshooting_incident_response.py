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


class TroubleshootingIncidentResponse(object):
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
        'entity_id': 'str',
        'start_entity_id': 'str',
        'name': 'str',
        'status': 'str',
        'created_time': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'last_modified_time': 'int',
        'created_by': 'str',
        'last_modified_by': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'start_entity_id': 'start_entity_id',
        'name': 'name',
        'status': 'status',
        'created_time': 'created_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'last_modified_time': 'last_modified_time',
        'created_by': 'created_by',
        'last_modified_by': 'last_modified_by'
    }

    def __init__(self, entity_id=None, start_entity_id=None, name=None, status=None, created_time=None, start_time=None, end_time=None, last_modified_time=None, created_by=None, last_modified_by=None):
        """
        TroubleshootingIncidentResponse - a model defined in Swagger
        """

        self._entity_id = None
        self._start_entity_id = None
        self._name = None
        self._status = None
        self._created_time = None
        self._start_time = None
        self._end_time = None
        self._last_modified_time = None
        self._created_by = None
        self._last_modified_by = None

        if entity_id is not None:
          self.entity_id = entity_id
        if start_entity_id is not None:
          self.start_entity_id = start_entity_id
        if name is not None:
          self.name = name
        if status is not None:
          self.status = status
        if created_time is not None:
          self.created_time = created_time
        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time
        if last_modified_time is not None:
          self.last_modified_time = last_modified_time
        if created_by is not None:
          self.created_by = created_by
        if last_modified_by is not None:
          self.last_modified_by = last_modified_by

    @property
    def entity_id(self):
        """
        Gets the entity_id of this TroubleshootingIncidentResponse.

        :return: The entity_id of this TroubleshootingIncidentResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this TroubleshootingIncidentResponse.

        :param entity_id: The entity_id of this TroubleshootingIncidentResponse.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def start_entity_id(self):
        """
        Gets the start_entity_id of this TroubleshootingIncidentResponse.

        :return: The start_entity_id of this TroubleshootingIncidentResponse.
        :rtype: str
        """
        return self._start_entity_id

    @start_entity_id.setter
    def start_entity_id(self, start_entity_id):
        """
        Sets the start_entity_id of this TroubleshootingIncidentResponse.

        :param start_entity_id: The start_entity_id of this TroubleshootingIncidentResponse.
        :type: str
        """

        self._start_entity_id = start_entity_id

    @property
    def name(self):
        """
        Gets the name of this TroubleshootingIncidentResponse.

        :return: The name of this TroubleshootingIncidentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TroubleshootingIncidentResponse.

        :param name: The name of this TroubleshootingIncidentResponse.
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """
        Gets the status of this TroubleshootingIncidentResponse.

        :return: The status of this TroubleshootingIncidentResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TroubleshootingIncidentResponse.

        :param status: The status of this TroubleshootingIncidentResponse.
        :type: str
        """

        self._status = status

    @property
    def created_time(self):
        """
        Gets the created_time of this TroubleshootingIncidentResponse.

        :return: The created_time of this TroubleshootingIncidentResponse.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """
        Sets the created_time of this TroubleshootingIncidentResponse.

        :param created_time: The created_time of this TroubleshootingIncidentResponse.
        :type: int
        """

        self._created_time = created_time

    @property
    def start_time(self):
        """
        Gets the start_time of this TroubleshootingIncidentResponse.

        :return: The start_time of this TroubleshootingIncidentResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this TroubleshootingIncidentResponse.

        :param start_time: The start_time of this TroubleshootingIncidentResponse.
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this TroubleshootingIncidentResponse.

        :return: The end_time of this TroubleshootingIncidentResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this TroubleshootingIncidentResponse.

        :param end_time: The end_time of this TroubleshootingIncidentResponse.
        :type: int
        """

        self._end_time = end_time

    @property
    def last_modified_time(self):
        """
        Gets the last_modified_time of this TroubleshootingIncidentResponse.

        :return: The last_modified_time of this TroubleshootingIncidentResponse.
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """
        Sets the last_modified_time of this TroubleshootingIncidentResponse.

        :param last_modified_time: The last_modified_time of this TroubleshootingIncidentResponse.
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def created_by(self):
        """
        Gets the created_by of this TroubleshootingIncidentResponse.

        :return: The created_by of this TroubleshootingIncidentResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this TroubleshootingIncidentResponse.

        :param created_by: The created_by of this TroubleshootingIncidentResponse.
        :type: str
        """

        self._created_by = created_by

    @property
    def last_modified_by(self):
        """
        Gets the last_modified_by of this TroubleshootingIncidentResponse.

        :return: The last_modified_by of this TroubleshootingIncidentResponse.
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """
        Sets the last_modified_by of this TroubleshootingIncidentResponse.

        :param last_modified_by: The last_modified_by of this TroubleshootingIncidentResponse.
        :type: str
        """

        self._last_modified_by = last_modified_by

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
        if not isinstance(other, TroubleshootingIncidentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other