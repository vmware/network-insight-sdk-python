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


class BackupRestoreRequest(object):
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
        'config_filter': 'ConfigDataFilter',
        'backup_schedule': 'BackupSchedule',
        'backup_file_server_type': 'FileServerType',
        'local_file_server': 'LocalFileServer',
        'ssh_file_server': 'SshFileServer',
        'ftp_file_server': 'FtpFileServer',
        'schedule_now': 'bool'
    }

    attribute_map = {
        'config_filter': 'config_filter',
        'backup_schedule': 'backup_schedule',
        'backup_file_server_type': 'backup_file_server_type',
        'local_file_server': 'local_file_server',
        'ssh_file_server': 'ssh_file_server',
        'ftp_file_server': 'ftp_file_server',
        'schedule_now': 'schedule_now'
    }

    def __init__(self, config_filter=None, backup_schedule=None, backup_file_server_type=None, local_file_server=None, ssh_file_server=None, ftp_file_server=None, schedule_now=False):
        """
        BackupRestoreRequest - a model defined in Swagger
        """

        self._config_filter = None
        self._backup_schedule = None
        self._backup_file_server_type = None
        self._local_file_server = None
        self._ssh_file_server = None
        self._ftp_file_server = None
        self._schedule_now = None

        if config_filter is not None:
          self.config_filter = config_filter
        if backup_schedule is not None:
          self.backup_schedule = backup_schedule
        if backup_file_server_type is not None:
          self.backup_file_server_type = backup_file_server_type
        if local_file_server is not None:
          self.local_file_server = local_file_server
        if ssh_file_server is not None:
          self.ssh_file_server = ssh_file_server
        if ftp_file_server is not None:
          self.ftp_file_server = ftp_file_server
        if schedule_now is not None:
          self.schedule_now = schedule_now

    @property
    def config_filter(self):
        """
        Gets the config_filter of this BackupRestoreRequest.

        :return: The config_filter of this BackupRestoreRequest.
        :rtype: ConfigDataFilter
        """
        return self._config_filter

    @config_filter.setter
    def config_filter(self, config_filter):
        """
        Sets the config_filter of this BackupRestoreRequest.

        :param config_filter: The config_filter of this BackupRestoreRequest.
        :type: ConfigDataFilter
        """

        self._config_filter = config_filter

    @property
    def backup_schedule(self):
        """
        Gets the backup_schedule of this BackupRestoreRequest.

        :return: The backup_schedule of this BackupRestoreRequest.
        :rtype: BackupSchedule
        """
        return self._backup_schedule

    @backup_schedule.setter
    def backup_schedule(self, backup_schedule):
        """
        Sets the backup_schedule of this BackupRestoreRequest.

        :param backup_schedule: The backup_schedule of this BackupRestoreRequest.
        :type: BackupSchedule
        """

        self._backup_schedule = backup_schedule

    @property
    def backup_file_server_type(self):
        """
        Gets the backup_file_server_type of this BackupRestoreRequest.

        :return: The backup_file_server_type of this BackupRestoreRequest.
        :rtype: FileServerType
        """
        return self._backup_file_server_type

    @backup_file_server_type.setter
    def backup_file_server_type(self, backup_file_server_type):
        """
        Sets the backup_file_server_type of this BackupRestoreRequest.

        :param backup_file_server_type: The backup_file_server_type of this BackupRestoreRequest.
        :type: FileServerType
        """

        self._backup_file_server_type = backup_file_server_type

    @property
    def local_file_server(self):
        """
        Gets the local_file_server of this BackupRestoreRequest.

        :return: The local_file_server of this BackupRestoreRequest.
        :rtype: LocalFileServer
        """
        return self._local_file_server

    @local_file_server.setter
    def local_file_server(self, local_file_server):
        """
        Sets the local_file_server of this BackupRestoreRequest.

        :param local_file_server: The local_file_server of this BackupRestoreRequest.
        :type: LocalFileServer
        """

        self._local_file_server = local_file_server

    @property
    def ssh_file_server(self):
        """
        Gets the ssh_file_server of this BackupRestoreRequest.

        :return: The ssh_file_server of this BackupRestoreRequest.
        :rtype: SshFileServer
        """
        return self._ssh_file_server

    @ssh_file_server.setter
    def ssh_file_server(self, ssh_file_server):
        """
        Sets the ssh_file_server of this BackupRestoreRequest.

        :param ssh_file_server: The ssh_file_server of this BackupRestoreRequest.
        :type: SshFileServer
        """

        self._ssh_file_server = ssh_file_server

    @property
    def ftp_file_server(self):
        """
        Gets the ftp_file_server of this BackupRestoreRequest.

        :return: The ftp_file_server of this BackupRestoreRequest.
        :rtype: FtpFileServer
        """
        return self._ftp_file_server

    @ftp_file_server.setter
    def ftp_file_server(self, ftp_file_server):
        """
        Sets the ftp_file_server of this BackupRestoreRequest.

        :param ftp_file_server: The ftp_file_server of this BackupRestoreRequest.
        :type: FtpFileServer
        """

        self._ftp_file_server = ftp_file_server

    @property
    def schedule_now(self):
        """
        Gets the schedule_now of this BackupRestoreRequest.
        True, to run backup now (on demand)

        :return: The schedule_now of this BackupRestoreRequest.
        :rtype: bool
        """
        return self._schedule_now

    @schedule_now.setter
    def schedule_now(self, schedule_now):
        """
        Sets the schedule_now of this BackupRestoreRequest.
        True, to run backup now (on demand)

        :param schedule_now: The schedule_now of this BackupRestoreRequest.
        :type: bool
        """

        self._schedule_now = schedule_now

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
        if not isinstance(other, BackupRestoreRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
