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


class CustomPinResponse(object):
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
        'pin_model_key': 'str',
        'pin_name': 'str',
        'custom_dashboard_id': 'str',
        'query': 'str',
        'created_timestamp': 'str',
        'last_updated_timestamp': 'str',
        'pinned_timestamp': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'pin_model_key': 'pin_model_key',
        'pin_name': 'pin_name',
        'custom_dashboard_id': 'custom_dashboard_id',
        'query': 'query',
        'created_timestamp': 'created_timestamp',
        'last_updated_timestamp': 'last_updated_timestamp',
        'pinned_timestamp': 'pinned_timestamp',
        'owner': 'owner'
    }

    def __init__(self, pin_model_key=None, pin_name=None, custom_dashboard_id=None, query=None, created_timestamp=None, last_updated_timestamp=None, pinned_timestamp=None, owner=None):
        """
        CustomPinResponse - a model defined in Swagger
        """

        self._pin_model_key = None
        self._pin_name = None
        self._custom_dashboard_id = None
        self._query = None
        self._created_timestamp = None
        self._last_updated_timestamp = None
        self._pinned_timestamp = None
        self._owner = None

        if pin_model_key is not None:
          self.pin_model_key = pin_model_key
        if pin_name is not None:
          self.pin_name = pin_name
        if custom_dashboard_id is not None:
          self.custom_dashboard_id = custom_dashboard_id
        if query is not None:
          self.query = query
        if created_timestamp is not None:
          self.created_timestamp = created_timestamp
        if last_updated_timestamp is not None:
          self.last_updated_timestamp = last_updated_timestamp
        if pinned_timestamp is not None:
          self.pinned_timestamp = pinned_timestamp
        if owner is not None:
          self.owner = owner

    @property
    def pin_model_key(self):
        """
        Gets the pin_model_key of this CustomPinResponse.
        Pin model key

        :return: The pin_model_key of this CustomPinResponse.
        :rtype: str
        """
        return self._pin_model_key

    @pin_model_key.setter
    def pin_model_key(self, pin_model_key):
        """
        Sets the pin_model_key of this CustomPinResponse.
        Pin model key

        :param pin_model_key: The pin_model_key of this CustomPinResponse.
        :type: str
        """

        self._pin_model_key = pin_model_key

    @property
    def pin_name(self):
        """
        Gets the pin_name of this CustomPinResponse.
        Name of the pin

        :return: The pin_name of this CustomPinResponse.
        :rtype: str
        """
        return self._pin_name

    @pin_name.setter
    def pin_name(self, pin_name):
        """
        Sets the pin_name of this CustomPinResponse.
        Name of the pin

        :param pin_name: The pin_name of this CustomPinResponse.
        :type: str
        """

        self._pin_name = pin_name

    @property
    def custom_dashboard_id(self):
        """
        Gets the custom_dashboard_id of this CustomPinResponse.
        Model key of the custom dashboard of which the pin is part of

        :return: The custom_dashboard_id of this CustomPinResponse.
        :rtype: str
        """
        return self._custom_dashboard_id

    @custom_dashboard_id.setter
    def custom_dashboard_id(self, custom_dashboard_id):
        """
        Sets the custom_dashboard_id of this CustomPinResponse.
        Model key of the custom dashboard of which the pin is part of

        :param custom_dashboard_id: The custom_dashboard_id of this CustomPinResponse.
        :type: str
        """

        self._custom_dashboard_id = custom_dashboard_id

    @property
    def query(self):
        """
        Gets the query of this CustomPinResponse.
        Search query behind the pin

        :return: The query of this CustomPinResponse.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this CustomPinResponse.
        Search query behind the pin

        :param query: The query of this CustomPinResponse.
        :type: str
        """

        self._query = query

    @property
    def created_timestamp(self):
        """
        Gets the created_timestamp of this CustomPinResponse.
        Create timestamp of the pin

        :return: The created_timestamp of this CustomPinResponse.
        :rtype: str
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """
        Sets the created_timestamp of this CustomPinResponse.
        Create timestamp of the pin

        :param created_timestamp: The created_timestamp of this CustomPinResponse.
        :type: str
        """

        self._created_timestamp = created_timestamp

    @property
    def last_updated_timestamp(self):
        """
        Gets the last_updated_timestamp of this CustomPinResponse.
        Last update timestamp of the pin

        :return: The last_updated_timestamp of this CustomPinResponse.
        :rtype: str
        """
        return self._last_updated_timestamp

    @last_updated_timestamp.setter
    def last_updated_timestamp(self, last_updated_timestamp):
        """
        Sets the last_updated_timestamp of this CustomPinResponse.
        Last update timestamp of the pin

        :param last_updated_timestamp: The last_updated_timestamp of this CustomPinResponse.
        :type: str
        """

        self._last_updated_timestamp = last_updated_timestamp

    @property
    def pinned_timestamp(self):
        """
        Gets the pinned_timestamp of this CustomPinResponse.
        Timestamp when the pin was pinned

        :return: The pinned_timestamp of this CustomPinResponse.
        :rtype: str
        """
        return self._pinned_timestamp

    @pinned_timestamp.setter
    def pinned_timestamp(self, pinned_timestamp):
        """
        Sets the pinned_timestamp of this CustomPinResponse.
        Timestamp when the pin was pinned

        :param pinned_timestamp: The pinned_timestamp of this CustomPinResponse.
        :type: str
        """

        self._pinned_timestamp = pinned_timestamp

    @property
    def owner(self):
        """
        Gets the owner of this CustomPinResponse.
        Owner of the pin

        :return: The owner of this CustomPinResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this CustomPinResponse.
        Owner of the pin

        :param owner: The owner of this CustomPinResponse.
        :type: str
        """

        self._owner = owner

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
        if not isinstance(other, CustomPinResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other