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


class HCXApplianceStatus(object):
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
        'overall_status': 'str',
        'overall_transport_status': 'str',
        'service_pipeline_status': 'str',
        'overall_encryption_status': 'str',
        'wan_opt_status': 'str',
        'system_state': 'str'
    }

    attribute_map = {
        'overall_status': 'overall_status',
        'overall_transport_status': 'overall_transport_status',
        'service_pipeline_status': 'service_pipeline_status',
        'overall_encryption_status': 'overall_encryption_status',
        'wan_opt_status': 'wan_opt_status',
        'system_state': 'system_state'
    }

    def __init__(self, overall_status=None, overall_transport_status=None, service_pipeline_status=None, overall_encryption_status=None, wan_opt_status=None, system_state=None):
        """
        HCXApplianceStatus - a model defined in Swagger
        """

        self._overall_status = None
        self._overall_transport_status = None
        self._service_pipeline_status = None
        self._overall_encryption_status = None
        self._wan_opt_status = None
        self._system_state = None

        if overall_status is not None:
          self.overall_status = overall_status
        if overall_transport_status is not None:
          self.overall_transport_status = overall_transport_status
        if service_pipeline_status is not None:
          self.service_pipeline_status = service_pipeline_status
        if overall_encryption_status is not None:
          self.overall_encryption_status = overall_encryption_status
        if wan_opt_status is not None:
          self.wan_opt_status = wan_opt_status
        if system_state is not None:
          self.system_state = system_state

    @property
    def overall_status(self):
        """
        Gets the overall_status of this HCXApplianceStatus.

        :return: The overall_status of this HCXApplianceStatus.
        :rtype: str
        """
        return self._overall_status

    @overall_status.setter
    def overall_status(self, overall_status):
        """
        Sets the overall_status of this HCXApplianceStatus.

        :param overall_status: The overall_status of this HCXApplianceStatus.
        :type: str
        """

        self._overall_status = overall_status

    @property
    def overall_transport_status(self):
        """
        Gets the overall_transport_status of this HCXApplianceStatus.

        :return: The overall_transport_status of this HCXApplianceStatus.
        :rtype: str
        """
        return self._overall_transport_status

    @overall_transport_status.setter
    def overall_transport_status(self, overall_transport_status):
        """
        Sets the overall_transport_status of this HCXApplianceStatus.

        :param overall_transport_status: The overall_transport_status of this HCXApplianceStatus.
        :type: str
        """

        self._overall_transport_status = overall_transport_status

    @property
    def service_pipeline_status(self):
        """
        Gets the service_pipeline_status of this HCXApplianceStatus.

        :return: The service_pipeline_status of this HCXApplianceStatus.
        :rtype: str
        """
        return self._service_pipeline_status

    @service_pipeline_status.setter
    def service_pipeline_status(self, service_pipeline_status):
        """
        Sets the service_pipeline_status of this HCXApplianceStatus.

        :param service_pipeline_status: The service_pipeline_status of this HCXApplianceStatus.
        :type: str
        """

        self._service_pipeline_status = service_pipeline_status

    @property
    def overall_encryption_status(self):
        """
        Gets the overall_encryption_status of this HCXApplianceStatus.

        :return: The overall_encryption_status of this HCXApplianceStatus.
        :rtype: str
        """
        return self._overall_encryption_status

    @overall_encryption_status.setter
    def overall_encryption_status(self, overall_encryption_status):
        """
        Sets the overall_encryption_status of this HCXApplianceStatus.

        :param overall_encryption_status: The overall_encryption_status of this HCXApplianceStatus.
        :type: str
        """

        self._overall_encryption_status = overall_encryption_status

    @property
    def wan_opt_status(self):
        """
        Gets the wan_opt_status of this HCXApplianceStatus.

        :return: The wan_opt_status of this HCXApplianceStatus.
        :rtype: str
        """
        return self._wan_opt_status

    @wan_opt_status.setter
    def wan_opt_status(self, wan_opt_status):
        """
        Sets the wan_opt_status of this HCXApplianceStatus.

        :param wan_opt_status: The wan_opt_status of this HCXApplianceStatus.
        :type: str
        """

        self._wan_opt_status = wan_opt_status

    @property
    def system_state(self):
        """
        Gets the system_state of this HCXApplianceStatus.

        :return: The system_state of this HCXApplianceStatus.
        :rtype: str
        """
        return self._system_state

    @system_state.setter
    def system_state(self, system_state):
        """
        Sets the system_state of this HCXApplianceStatus.

        :param system_state: The system_state of this HCXApplianceStatus.
        :type: str
        """

        self._system_state = system_state

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
        if not isinstance(other, HCXApplianceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
