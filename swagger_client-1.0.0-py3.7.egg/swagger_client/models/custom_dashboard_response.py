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


class CustomDashboardResponse(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'create_timestamp': 'str',
        'last_updated_timestamp': 'str',
        'owner': 'str',
        'users_read_access': 'list[str]',
        'users_write_access': 'list[str]',
        'pins': 'list[CustomPinObject]',
        'groups_write_access': 'list[str]',
        'groups_read_access': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'create_timestamp': 'create_timestamp',
        'last_updated_timestamp': 'last_updated_timestamp',
        'owner': 'owner',
        'users_read_access': 'users_read_access',
        'users_write_access': 'users_write_access',
        'pins': 'pins',
        'groups_write_access': 'groups_write_access',
        'groups_read_access': 'groups_read_access'
    }

    def __init__(self, id=None, name=None, description=None, create_timestamp=None, last_updated_timestamp=None, owner=None, users_read_access=None, users_write_access=None, pins=None, groups_write_access=None, groups_read_access=None):
        """
        CustomDashboardResponse - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._create_timestamp = None
        self._last_updated_timestamp = None
        self._owner = None
        self._users_read_access = None
        self._users_write_access = None
        self._pins = None
        self._groups_write_access = None
        self._groups_read_access = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if create_timestamp is not None:
          self.create_timestamp = create_timestamp
        if last_updated_timestamp is not None:
          self.last_updated_timestamp = last_updated_timestamp
        if owner is not None:
          self.owner = owner
        if users_read_access is not None:
          self.users_read_access = users_read_access
        if users_write_access is not None:
          self.users_write_access = users_write_access
        if pins is not None:
          self.pins = pins
        if groups_write_access is not None:
          self.groups_write_access = groups_write_access
        if groups_read_access is not None:
          self.groups_read_access = groups_read_access

    @property
    def id(self):
        """
        Gets the id of this CustomDashboardResponse.
        Entity Identifier for a custom dashboard

        :return: The id of this CustomDashboardResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomDashboardResponse.
        Entity Identifier for a custom dashboard

        :param id: The id of this CustomDashboardResponse.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CustomDashboardResponse.
        Descriptor or identifier for particular custom dashboard.

        :return: The name of this CustomDashboardResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CustomDashboardResponse.
        Descriptor or identifier for particular custom dashboard.

        :param name: The name of this CustomDashboardResponse.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CustomDashboardResponse.
        Description of the custom dashboard

        :return: The description of this CustomDashboardResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CustomDashboardResponse.
        Description of the custom dashboard

        :param description: The description of this CustomDashboardResponse.
        :type: str
        """

        self._description = description

    @property
    def create_timestamp(self):
        """
        Gets the create_timestamp of this CustomDashboardResponse.
        Create timestamp for custom dashboard

        :return: The create_timestamp of this CustomDashboardResponse.
        :rtype: str
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """
        Sets the create_timestamp of this CustomDashboardResponse.
        Create timestamp for custom dashboard

        :param create_timestamp: The create_timestamp of this CustomDashboardResponse.
        :type: str
        """

        self._create_timestamp = create_timestamp

    @property
    def last_updated_timestamp(self):
        """
        Gets the last_updated_timestamp of this CustomDashboardResponse.
        Last update timestamp for custom dashboard

        :return: The last_updated_timestamp of this CustomDashboardResponse.
        :rtype: str
        """
        return self._last_updated_timestamp

    @last_updated_timestamp.setter
    def last_updated_timestamp(self, last_updated_timestamp):
        """
        Sets the last_updated_timestamp of this CustomDashboardResponse.
        Last update timestamp for custom dashboard

        :param last_updated_timestamp: The last_updated_timestamp of this CustomDashboardResponse.
        :type: str
        """

        self._last_updated_timestamp = last_updated_timestamp

    @property
    def owner(self):
        """
        Gets the owner of this CustomDashboardResponse.
        User email of the custom dashboard owner

        :return: The owner of this CustomDashboardResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this CustomDashboardResponse.
        User email of the custom dashboard owner

        :param owner: The owner of this CustomDashboardResponse.
        :type: str
        """

        self._owner = owner

    @property
    def users_read_access(self):
        """
        Gets the users_read_access of this CustomDashboardResponse.
        List of users with read privilege for the custom dashboard

        :return: The users_read_access of this CustomDashboardResponse.
        :rtype: list[str]
        """
        return self._users_read_access

    @users_read_access.setter
    def users_read_access(self, users_read_access):
        """
        Sets the users_read_access of this CustomDashboardResponse.
        List of users with read privilege for the custom dashboard

        :param users_read_access: The users_read_access of this CustomDashboardResponse.
        :type: list[str]
        """

        self._users_read_access = users_read_access

    @property
    def users_write_access(self):
        """
        Gets the users_write_access of this CustomDashboardResponse.
        List of users with read and write privilege for the custom dashboard

        :return: The users_write_access of this CustomDashboardResponse.
        :rtype: list[str]
        """
        return self._users_write_access

    @users_write_access.setter
    def users_write_access(self, users_write_access):
        """
        Sets the users_write_access of this CustomDashboardResponse.
        List of users with read and write privilege for the custom dashboard

        :param users_write_access: The users_write_access of this CustomDashboardResponse.
        :type: list[str]
        """

        self._users_write_access = users_write_access

    @property
    def pins(self):
        """
        Gets the pins of this CustomDashboardResponse.
        Pins associated with custom dashboard

        :return: The pins of this CustomDashboardResponse.
        :rtype: list[CustomPinObject]
        """
        return self._pins

    @pins.setter
    def pins(self, pins):
        """
        Sets the pins of this CustomDashboardResponse.
        Pins associated with custom dashboard

        :param pins: The pins of this CustomDashboardResponse.
        :type: list[CustomPinObject]
        """

        self._pins = pins

    @property
    def groups_write_access(self):
        """
        Gets the groups_write_access of this CustomDashboardResponse.
        LDAP/VIDM groups with read and write privilege of the custom dashboard

        :return: The groups_write_access of this CustomDashboardResponse.
        :rtype: list[str]
        """
        return self._groups_write_access

    @groups_write_access.setter
    def groups_write_access(self, groups_write_access):
        """
        Sets the groups_write_access of this CustomDashboardResponse.
        LDAP/VIDM groups with read and write privilege of the custom dashboard

        :param groups_write_access: The groups_write_access of this CustomDashboardResponse.
        :type: list[str]
        """

        self._groups_write_access = groups_write_access

    @property
    def groups_read_access(self):
        """
        Gets the groups_read_access of this CustomDashboardResponse.
        LDAP/VIDM groups with read privilege of the custom dashboard

        :return: The groups_read_access of this CustomDashboardResponse.
        :rtype: list[str]
        """
        return self._groups_read_access

    @groups_read_access.setter
    def groups_read_access(self, groups_read_access):
        """
        Sets the groups_read_access of this CustomDashboardResponse.
        LDAP/VIDM groups with read privilege of the custom dashboard

        :param groups_read_access: The groups_read_access of this CustomDashboardResponse.
        :type: list[str]
        """

        self._groups_read_access = groups_read_access

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
        if not isinstance(other, CustomDashboardResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
