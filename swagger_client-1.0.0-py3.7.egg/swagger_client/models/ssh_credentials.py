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


class SSHCredentials(object):
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
        'username': 'str',
        'password': 'str',
        'name': 'str',
        'entity_id': 'str',
        'account_type': 'AccountType'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'name': 'name',
        'entity_id': 'entityId',
        'account_type': 'account_type'
    }

    def __init__(self, username=None, password=None, name=None, entity_id=None, account_type=None):
        """
        SSHCredentials - a model defined in Swagger
        """

        self._username = None
        self._password = None
        self._name = None
        self._entity_id = None
        self._account_type = None

        self.username = username
        if password is not None:
          self.password = password
        if name is not None:
          self.name = name
        if entity_id is not None:
          self.entity_id = entity_id
        if account_type is not None:
          self.account_type = account_type

    @property
    def username(self):
        """
        Gets the username of this SSHCredentials.
        Username to authenticate with

        :return: The username of this SSHCredentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this SSHCredentials.
        Username to authenticate with

        :param username: The username of this SSHCredentials.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this SSHCredentials.
        Password to authenticate with

        :return: The password of this SSHCredentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this SSHCredentials.
        Password to authenticate with

        :param password: The password of this SSHCredentials.
        :type: str
        """

        self._password = password

    @property
    def name(self):
        """
        Gets the name of this SSHCredentials.
        Unique Name

        :return: The name of this SSHCredentials.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SSHCredentials.
        Unique Name

        :param name: The name of this SSHCredentials.
        :type: str
        """

        self._name = name

    @property
    def entity_id(self):
        """
        Gets the entity_id of this SSHCredentials.
        entityId

        :return: The entity_id of this SSHCredentials.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this SSHCredentials.
        entityId

        :param entity_id: The entity_id of this SSHCredentials.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def account_type(self):
        """
        Gets the account_type of this SSHCredentials.

        :return: The account_type of this SSHCredentials.
        :rtype: AccountType
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this SSHCredentials.

        :param account_type: The account_type of this SSHCredentials.
        :type: AccountType
        """

        self._account_type = account_type

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
        if not isinstance(other, SSHCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
