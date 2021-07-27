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


class BackupRestoreStatusResponse(object):
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
        'status': 'str',
        'backup_file_name': 'str',
        'status_updated_timestamp': 'str',
        'failed_components': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'backup_file_name': 'backup_file_name',
        'status_updated_timestamp': 'status_updated_timestamp',
        'failed_components': 'failed_components'
    }

    def __init__(self, status=None, backup_file_name=None, status_updated_timestamp=None, failed_components=None):
        """
        BackupRestoreStatusResponse - a model defined in Swagger
        """

        self._status = None
        self._backup_file_name = None
        self._status_updated_timestamp = None
        self._failed_components = None

        if status is not None:
          self.status = status
        if backup_file_name is not None:
          self.backup_file_name = backup_file_name
        if status_updated_timestamp is not None:
          self.status_updated_timestamp = status_updated_timestamp
        if failed_components is not None:
          self.failed_components = failed_components

    @property
    def status(self):
        """
        Gets the status of this BackupRestoreStatusResponse.
        Status of currently executing or last backup-restore job

        :return: The status of this BackupRestoreStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BackupRestoreStatusResponse.
        Status of currently executing or last backup-restore job

        :param status: The status of this BackupRestoreStatusResponse.
        :type: str
        """

        self._status = status

    @property
    def backup_file_name(self):
        """
        Gets the backup_file_name of this BackupRestoreStatusResponse.
        File name of backup tar file

        :return: The backup_file_name of this BackupRestoreStatusResponse.
        :rtype: str
        """
        return self._backup_file_name

    @backup_file_name.setter
    def backup_file_name(self, backup_file_name):
        """
        Sets the backup_file_name of this BackupRestoreStatusResponse.
        File name of backup tar file

        :param backup_file_name: The backup_file_name of this BackupRestoreStatusResponse.
        :type: str
        """

        self._backup_file_name = backup_file_name

    @property
    def status_updated_timestamp(self):
        """
        Gets the status_updated_timestamp of this BackupRestoreStatusResponse.
        TimeStamp of the last status update

        :return: The status_updated_timestamp of this BackupRestoreStatusResponse.
        :rtype: str
        """
        return self._status_updated_timestamp

    @status_updated_timestamp.setter
    def status_updated_timestamp(self, status_updated_timestamp):
        """
        Sets the status_updated_timestamp of this BackupRestoreStatusResponse.
        TimeStamp of the last status update

        :param status_updated_timestamp: The status_updated_timestamp of this BackupRestoreStatusResponse.
        :type: str
        """

        self._status_updated_timestamp = status_updated_timestamp

    @property
    def failed_components(self):
        """
        Gets the failed_components of this BackupRestoreStatusResponse.
        List of components failed to backup or restore

        :return: The failed_components of this BackupRestoreStatusResponse.
        :rtype: list[str]
        """
        return self._failed_components

    @failed_components.setter
    def failed_components(self, failed_components):
        """
        Sets the failed_components of this BackupRestoreStatusResponse.
        List of components failed to backup or restore

        :param failed_components: The failed_components of this BackupRestoreStatusResponse.
        :type: list[str]
        """

        self._failed_components = failed_components

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
        if not isinstance(other, BackupRestoreStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
