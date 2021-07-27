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


class NSXControllerDataCollection(object):
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
        'enabled': 'bool',
        'controller_password': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'controller_password': 'controller_password'
    }

    def __init__(self, enabled=False, controller_password=None):
        """
        NSXControllerDataCollection - a model defined in Swagger
        """

        self._enabled = None
        self._controller_password = None

        if enabled is not None:
          self.enabled = enabled
        if controller_password is not None:
          self.controller_password = controller_password

    @property
    def enabled(self):
        """
        Gets the enabled of this NSXControllerDataCollection.
        Whether or not to collect data from the NSX-v Controller Cluster

        :return: The enabled of this NSXControllerDataCollection.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this NSXControllerDataCollection.
        Whether or not to collect data from the NSX-v Controller Cluster

        :param enabled: The enabled of this NSXControllerDataCollection.
        :type: bool
        """

        self._enabled = enabled

    @property
    def controller_password(self):
        """
        Gets the controller_password of this NSXControllerDataCollection.
        Controller Password

        :return: The controller_password of this NSXControllerDataCollection.
        :rtype: str
        """
        return self._controller_password

    @controller_password.setter
    def controller_password(self, controller_password):
        """
        Sets the controller_password of this NSXControllerDataCollection.
        Controller Password

        :param controller_password: The controller_password of this NSXControllerDataCollection.
        :type: str
        """

        self._controller_password = controller_password

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
        if not isinstance(other, NSXControllerDataCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
