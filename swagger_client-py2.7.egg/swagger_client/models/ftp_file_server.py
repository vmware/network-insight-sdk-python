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


class FtpFileServer(object):
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
        'server_address': 'str',
        'port': 'int',
        'username': 'str',
        'password': 'str',
        'backup_directory': 'str',
        'backup_file_name': 'str'
    }

    attribute_map = {
        'server_address': 'server_address',
        'port': 'port',
        'username': 'username',
        'password': 'password',
        'backup_directory': 'backup_directory',
        'backup_file_name': 'backup_file_name'
    }

    def __init__(self, server_address=None, port=None, username=None, password=None, backup_directory=None, backup_file_name=None):
        """
        FtpFileServer - a model defined in Swagger
        """

        self._server_address = None
        self._port = None
        self._username = None
        self._password = None
        self._backup_directory = None
        self._backup_file_name = None

        if server_address is not None:
          self.server_address = server_address
        if port is not None:
          self.port = port
        if username is not None:
          self.username = username
        if password is not None:
          self.password = password
        if backup_directory is not None:
          self.backup_directory = backup_directory
        if backup_file_name is not None:
          self.backup_file_name = backup_file_name

    @property
    def server_address(self):
        """
        Gets the server_address of this FtpFileServer.
        IP address or hostname of destination FTP file server

        :return: The server_address of this FtpFileServer.
        :rtype: str
        """
        return self._server_address

    @server_address.setter
    def server_address(self, server_address):
        """
        Sets the server_address of this FtpFileServer.
        IP address or hostname of destination FTP file server

        :param server_address: The server_address of this FtpFileServer.
        :type: str
        """

        self._server_address = server_address

    @property
    def port(self):
        """
        Gets the port of this FtpFileServer.
        File transfer port

        :return: The port of this FtpFileServer.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this FtpFileServer.
        File transfer port

        :param port: The port of this FtpFileServer.
        :type: int
        """

        self._port = port

    @property
    def username(self):
        """
        Gets the username of this FtpFileServer.
        username to login FTP server

        :return: The username of this FtpFileServer.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this FtpFileServer.
        username to login FTP server

        :param username: The username of this FtpFileServer.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this FtpFileServer.
        password for the user to login FTP server

        :return: The password of this FtpFileServer.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this FtpFileServer.
        password for the user to login FTP server

        :param password: The password of this FtpFileServer.
        :type: str
        """

        self._password = password

    @property
    def backup_directory(self):
        """
        Gets the backup_directory of this FtpFileServer.
        directory on file server to store/fetch backups

        :return: The backup_directory of this FtpFileServer.
        :rtype: str
        """
        return self._backup_directory

    @backup_directory.setter
    def backup_directory(self, backup_directory):
        """
        Sets the backup_directory of this FtpFileServer.
        directory on file server to store/fetch backups

        :param backup_directory: The backup_directory of this FtpFileServer.
        :type: str
        """

        self._backup_directory = backup_directory

    @property
    def backup_file_name(self):
        """
        Gets the backup_file_name of this FtpFileServer.
        filename of the backup to be restored (used during restore only)

        :return: The backup_file_name of this FtpFileServer.
        :rtype: str
        """
        return self._backup_file_name

    @backup_file_name.setter
    def backup_file_name(self, backup_file_name):
        """
        Sets the backup_file_name of this FtpFileServer.
        filename of the backup to be restored (used during restore only)

        :param backup_file_name: The backup_file_name of this FtpFileServer.
        :type: str
        """

        self._backup_file_name = backup_file_name

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
        if not isinstance(other, FtpFileServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other