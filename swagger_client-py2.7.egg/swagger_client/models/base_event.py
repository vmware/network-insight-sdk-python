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


class BaseEvent(object):
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
        'name': 'str',
        'entity_type': 'EntityType',
        'anchor_entities': 'list[Reference]',
        'related_entities': 'list[Reference]',
        'message': 'str',
        'event_tags': 'list[str]',
        'admin_state': 'str',
        'archived': 'bool',
        'event_time_epoch_ms': 'int',
        'event_type': 'str',
        'recommendations': 'list[str]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'anchor_entities': 'anchor_entities',
        'related_entities': 'related_entities',
        'message': 'message',
        'event_tags': 'event_tags',
        'admin_state': 'admin_state',
        'archived': 'archived',
        'event_time_epoch_ms': 'event_time_epoch_ms',
        'event_type': 'event_type',
        'recommendations': 'recommendations'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, anchor_entities=None, related_entities=None, message=None, event_tags=None, admin_state=None, archived=None, event_time_epoch_ms=None, event_type=None, recommendations=None):
        """
        BaseEvent - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._anchor_entities = None
        self._related_entities = None
        self._message = None
        self._event_tags = None
        self._admin_state = None
        self._archived = None
        self._event_time_epoch_ms = None
        self._event_type = None
        self._recommendations = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if anchor_entities is not None:
          self.anchor_entities = anchor_entities
        if related_entities is not None:
          self.related_entities = related_entities
        if message is not None:
          self.message = message
        if event_tags is not None:
          self.event_tags = event_tags
        if admin_state is not None:
          self.admin_state = admin_state
        if archived is not None:
          self.archived = archived
        if event_time_epoch_ms is not None:
          self.event_time_epoch_ms = event_time_epoch_ms
        if event_type is not None:
          self.event_type = event_type
        if recommendations is not None:
          self.recommendations = recommendations

    @property
    def entity_id(self):
        """
        Gets the entity_id of this BaseEvent.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this BaseEvent.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this BaseEvent.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this BaseEvent.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this BaseEvent.
        Name of the object

        :return: The name of this BaseEvent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BaseEvent.
        Name of the object

        :param name: The name of this BaseEvent.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this BaseEvent.

        :return: The entity_type of this BaseEvent.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this BaseEvent.

        :param entity_type: The entity_type of this BaseEvent.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def anchor_entities(self):
        """
        Gets the anchor_entities of this BaseEvent.

        :return: The anchor_entities of this BaseEvent.
        :rtype: list[Reference]
        """
        return self._anchor_entities

    @anchor_entities.setter
    def anchor_entities(self, anchor_entities):
        """
        Sets the anchor_entities of this BaseEvent.

        :param anchor_entities: The anchor_entities of this BaseEvent.
        :type: list[Reference]
        """

        self._anchor_entities = anchor_entities

    @property
    def related_entities(self):
        """
        Gets the related_entities of this BaseEvent.
        The entity IDs of all related objects

        :return: The related_entities of this BaseEvent.
        :rtype: list[Reference]
        """
        return self._related_entities

    @related_entities.setter
    def related_entities(self, related_entities):
        """
        Sets the related_entities of this BaseEvent.
        The entity IDs of all related objects

        :param related_entities: The related_entities of this BaseEvent.
        :type: list[Reference]
        """

        self._related_entities = related_entities

    @property
    def message(self):
        """
        Gets the message of this BaseEvent.
        Event message

        :return: The message of this BaseEvent.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this BaseEvent.
        Event message

        :param message: The message of this BaseEvent.
        :type: str
        """

        self._message = message

    @property
    def event_tags(self):
        """
        Gets the event_tags of this BaseEvent.
        Event tags

        :return: The event_tags of this BaseEvent.
        :rtype: list[str]
        """
        return self._event_tags

    @event_tags.setter
    def event_tags(self, event_tags):
        """
        Sets the event_tags of this BaseEvent.
        Event tags

        :param event_tags: The event_tags of this BaseEvent.
        :type: list[str]
        """

        self._event_tags = event_tags

    @property
    def admin_state(self):
        """
        Gets the admin_state of this BaseEvent.
        Administrative state of the event

        :return: The admin_state of this BaseEvent.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """
        Sets the admin_state of this BaseEvent.
        Administrative state of the event

        :param admin_state: The admin_state of this BaseEvent.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if admin_state not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_state` ({0}), must be one of {1}"
                .format(admin_state, allowed_values)
            )

        self._admin_state = admin_state

    @property
    def archived(self):
        """
        Gets the archived of this BaseEvent.
        Whether of not the event is archived

        :return: The archived of this BaseEvent.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """
        Sets the archived of this BaseEvent.
        Whether of not the event is archived

        :param archived: The archived of this BaseEvent.
        :type: bool
        """

        self._archived = archived

    @property
    def event_time_epoch_ms(self):
        """
        Gets the event_time_epoch_ms of this BaseEvent.
        Epoc timestamp of when the event was triggered

        :return: The event_time_epoch_ms of this BaseEvent.
        :rtype: int
        """
        return self._event_time_epoch_ms

    @event_time_epoch_ms.setter
    def event_time_epoch_ms(self, event_time_epoch_ms):
        """
        Sets the event_time_epoch_ms of this BaseEvent.
        Epoc timestamp of when the event was triggered

        :param event_time_epoch_ms: The event_time_epoch_ms of this BaseEvent.
        :type: int
        """

        self._event_time_epoch_ms = event_time_epoch_ms

    @property
    def event_type(self):
        """
        Gets the event_type of this BaseEvent.
        The type of event

        :return: The event_type of this BaseEvent.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this BaseEvent.
        The type of event

        :param event_type: The event_type of this BaseEvent.
        :type: str
        """

        self._event_type = event_type

    @property
    def recommendations(self):
        """
        Gets the recommendations of this BaseEvent.
        A list of recommended remedies

        :return: The recommendations of this BaseEvent.
        :rtype: list[str]
        """
        return self._recommendations

    @recommendations.setter
    def recommendations(self, recommendations):
        """
        Sets the recommendations of this BaseEvent.
        A list of recommended remedies

        :param recommendations: The recommendations of this BaseEvent.
        :type: list[str]
        """

        self._recommendations = recommendations

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
        if not isinstance(other, BaseEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
