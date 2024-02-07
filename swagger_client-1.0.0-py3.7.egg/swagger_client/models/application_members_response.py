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


class ApplicationMembersResponse(object):
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
        'entity_type': 'str',
        'name': 'str',
        'created_by': 'str',
        'creation_time': 'int',
        'last_modified_by': 'str',
        'last_modified_by_service': 'str',
        'last_modified_time': 'int',
        'source': 'DiscoveryType',
        'tiers': 'list[TierMembersResponse]',
        'discovery_info': 'DiscoveryInfo',
        'curated_groups': 'list[str]',
        'confidence': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'name': 'name',
        'created_by': 'created_by',
        'creation_time': 'creation_time',
        'last_modified_by': 'last_modified_by',
        'last_modified_by_service': 'last_modified_by_service',
        'last_modified_time': 'last_modified_time',
        'source': 'source',
        'tiers': 'tiers',
        'discovery_info': 'discovery_info',
        'curated_groups': 'curated_groups',
        'confidence': 'confidence'
    }

    def __init__(self, entity_id=None, entity_type=None, name=None, created_by=None, creation_time=None, last_modified_by=None, last_modified_by_service=None, last_modified_time=None, source=None, tiers=None, discovery_info=None, curated_groups=None, confidence=None):
        """
        ApplicationMembersResponse - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
        self._name = None
        self._created_by = None
        self._creation_time = None
        self._last_modified_by = None
        self._last_modified_by_service = None
        self._last_modified_time = None
        self._source = None
        self._tiers = None
        self._discovery_info = None
        self._curated_groups = None
        self._confidence = None

        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if name is not None:
          self.name = name
        if created_by is not None:
          self.created_by = created_by
        if creation_time is not None:
          self.creation_time = creation_time
        if last_modified_by is not None:
          self.last_modified_by = last_modified_by
        if last_modified_by_service is not None:
          self.last_modified_by_service = last_modified_by_service
        if last_modified_time is not None:
          self.last_modified_time = last_modified_time
        if source is not None:
          self.source = source
        if tiers is not None:
          self.tiers = tiers
        if discovery_info is not None:
          self.discovery_info = discovery_info
        if curated_groups is not None:
          self.curated_groups = curated_groups
        if confidence is not None:
          self.confidence = confidence

    @property
    def entity_id(self):
        """
        Gets the entity_id of this ApplicationMembersResponse.

        :return: The entity_id of this ApplicationMembersResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this ApplicationMembersResponse.

        :param entity_id: The entity_id of this ApplicationMembersResponse.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this ApplicationMembersResponse.

        :return: The entity_type of this ApplicationMembersResponse.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this ApplicationMembersResponse.

        :param entity_type: The entity_type of this ApplicationMembersResponse.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """
        Gets the name of this ApplicationMembersResponse.

        :return: The name of this ApplicationMembersResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApplicationMembersResponse.

        :param name: The name of this ApplicationMembersResponse.
        :type: str
        """

        self._name = name

    @property
    def created_by(self):
        """
        Gets the created_by of this ApplicationMembersResponse.

        :return: The created_by of this ApplicationMembersResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this ApplicationMembersResponse.

        :param created_by: The created_by of this ApplicationMembersResponse.
        :type: str
        """

        self._created_by = created_by

    @property
    def creation_time(self):
        """
        Gets the creation_time of this ApplicationMembersResponse.

        :return: The creation_time of this ApplicationMembersResponse.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this ApplicationMembersResponse.

        :param creation_time: The creation_time of this ApplicationMembersResponse.
        :type: int
        """

        self._creation_time = creation_time

    @property
    def last_modified_by(self):
        """
        Gets the last_modified_by of this ApplicationMembersResponse.

        :return: The last_modified_by of this ApplicationMembersResponse.
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """
        Sets the last_modified_by of this ApplicationMembersResponse.

        :param last_modified_by: The last_modified_by of this ApplicationMembersResponse.
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_by_service(self):
        """
        Gets the last_modified_by_service of this ApplicationMembersResponse.

        :return: The last_modified_by_service of this ApplicationMembersResponse.
        :rtype: str
        """
        return self._last_modified_by_service

    @last_modified_by_service.setter
    def last_modified_by_service(self, last_modified_by_service):
        """
        Sets the last_modified_by_service of this ApplicationMembersResponse.

        :param last_modified_by_service: The last_modified_by_service of this ApplicationMembersResponse.
        :type: str
        """

        self._last_modified_by_service = last_modified_by_service

    @property
    def last_modified_time(self):
        """
        Gets the last_modified_time of this ApplicationMembersResponse.

        :return: The last_modified_time of this ApplicationMembersResponse.
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """
        Sets the last_modified_time of this ApplicationMembersResponse.

        :param last_modified_time: The last_modified_time of this ApplicationMembersResponse.
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def source(self):
        """
        Gets the source of this ApplicationMembersResponse.
        This field is deprecated. Please use discovery_info.

        :return: The source of this ApplicationMembersResponse.
        :rtype: DiscoveryType
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ApplicationMembersResponse.
        This field is deprecated. Please use discovery_info.

        :param source: The source of this ApplicationMembersResponse.
        :type: DiscoveryType
        """

        self._source = source

    @property
    def tiers(self):
        """
        Gets the tiers of this ApplicationMembersResponse.

        :return: The tiers of this ApplicationMembersResponse.
        :rtype: list[TierMembersResponse]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """
        Sets the tiers of this ApplicationMembersResponse.

        :param tiers: The tiers of this ApplicationMembersResponse.
        :type: list[TierMembersResponse]
        """

        self._tiers = tiers

    @property
    def discovery_info(self):
        """
        Gets the discovery_info of this ApplicationMembersResponse.

        :return: The discovery_info of this ApplicationMembersResponse.
        :rtype: DiscoveryInfo
        """
        return self._discovery_info

    @discovery_info.setter
    def discovery_info(self, discovery_info):
        """
        Sets the discovery_info of this ApplicationMembersResponse.

        :param discovery_info: The discovery_info of this ApplicationMembersResponse.
        :type: DiscoveryInfo
        """

        self._discovery_info = discovery_info

    @property
    def curated_groups(self):
        """
        Gets the curated_groups of this ApplicationMembersResponse.

        :return: The curated_groups of this ApplicationMembersResponse.
        :rtype: list[str]
        """
        return self._curated_groups

    @curated_groups.setter
    def curated_groups(self, curated_groups):
        """
        Sets the curated_groups of this ApplicationMembersResponse.

        :param curated_groups: The curated_groups of this ApplicationMembersResponse.
        :type: list[str]
        """

        self._curated_groups = curated_groups

    @property
    def confidence(self):
        """
        Gets the confidence of this ApplicationMembersResponse.

        :return: The confidence of this ApplicationMembersResponse.
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this ApplicationMembersResponse.

        :param confidence: The confidence of this ApplicationMembersResponse.
        :type: str
        """

        self._confidence = confidence

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
        if not isinstance(other, ApplicationMembersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other