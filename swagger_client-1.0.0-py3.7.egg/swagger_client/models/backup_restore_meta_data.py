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


class BackupRestoreMetaData(object):
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
        'component_name': 'str',
        'total_count': 'int',
        'success_count': 'int',
        'failed_entities': 'list[FailedBackupRestoreEntity]'
    }

    attribute_map = {
        'component_name': 'componentName',
        'total_count': 'totalCount',
        'success_count': 'successCount',
        'failed_entities': 'failedEntities'
    }

    def __init__(self, component_name=None, total_count=None, success_count=None, failed_entities=None):
        """
        BackupRestoreMetaData - a model defined in Swagger
        """

        self._component_name = None
        self._total_count = None
        self._success_count = None
        self._failed_entities = None

        if component_name is not None:
          self.component_name = component_name
        if total_count is not None:
          self.total_count = total_count
        if success_count is not None:
          self.success_count = success_count
        if failed_entities is not None:
          self.failed_entities = failed_entities

    @property
    def component_name(self):
        """
        Gets the component_name of this BackupRestoreMetaData.
        Name of the component

        :return: The component_name of this BackupRestoreMetaData.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """
        Sets the component_name of this BackupRestoreMetaData.
        Name of the component

        :param component_name: The component_name of this BackupRestoreMetaData.
        :type: str
        """

        self._component_name = component_name

    @property
    def total_count(self):
        """
        Gets the total_count of this BackupRestoreMetaData.
        Number of entities present in this component

        :return: The total_count of this BackupRestoreMetaData.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this BackupRestoreMetaData.
        Number of entities present in this component

        :param total_count: The total_count of this BackupRestoreMetaData.
        :type: int
        """

        self._total_count = total_count

    @property
    def success_count(self):
        """
        Gets the success_count of this BackupRestoreMetaData.
        Number of entities present in this component which are successfully backed up or restored

        :return: The success_count of this BackupRestoreMetaData.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """
        Sets the success_count of this BackupRestoreMetaData.
        Number of entities present in this component which are successfully backed up or restored

        :param success_count: The success_count of this BackupRestoreMetaData.
        :type: int
        """

        self._success_count = success_count

    @property
    def failed_entities(self):
        """
        Gets the failed_entities of this BackupRestoreMetaData.
        List of the entities for which backup/restore failed

        :return: The failed_entities of this BackupRestoreMetaData.
        :rtype: list[FailedBackupRestoreEntity]
        """
        return self._failed_entities

    @failed_entities.setter
    def failed_entities(self, failed_entities):
        """
        Sets the failed_entities of this BackupRestoreMetaData.
        List of the entities for which backup/restore failed

        :param failed_entities: The failed_entities of this BackupRestoreMetaData.
        :type: list[FailedBackupRestoreEntity]
        """

        self._failed_entities = failed_entities

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
        if not isinstance(other, BackupRestoreMetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other