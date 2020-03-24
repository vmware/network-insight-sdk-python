# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VidmConfiguration(object):
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
        'vidm_appliance': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'sha_thumbprint': 'str',
        'enable': 'bool'
    }

    attribute_map = {
        'vidm_appliance': 'vidm_appliance',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'sha_thumbprint': 'sha_thumbprint',
        'enable': 'enable'
    }

    def __init__(self, vidm_appliance=None, client_id=None, client_secret=None, sha_thumbprint=None, enable=None):
        """
        VidmConfiguration - a model defined in Swagger
        """

        self._vidm_appliance = None
        self._client_id = None
        self._client_secret = None
        self._sha_thumbprint = None
        self._enable = None

        if vidm_appliance is not None:
          self.vidm_appliance = vidm_appliance
        if client_id is not None:
          self.client_id = client_id
        if client_secret is not None:
          self.client_secret = client_secret
        if sha_thumbprint is not None:
          self.sha_thumbprint = sha_thumbprint
        if enable is not None:
          self.enable = enable

    @property
    def vidm_appliance(self):
        """
        Gets the vidm_appliance of this VidmConfiguration.
        Provide fully quallified domain name of VMware Identity Manager

        :return: The vidm_appliance of this VidmConfiguration.
        :rtype: str
        """
        return self._vidm_appliance

    @vidm_appliance.setter
    def vidm_appliance(self, vidm_appliance):
        """
        Sets the vidm_appliance of this VidmConfiguration.
        Provide fully quallified domain name of VMware Identity Manager

        :param vidm_appliance: The vidm_appliance of this VidmConfiguration.
        :type: str
        """

        self._vidm_appliance = vidm_appliance

    @property
    def client_id(self):
        """
        Gets the client_id of this VidmConfiguration.
        Register VMware vRealize Network Insight as an OAuth client to VMware Identity Manager and provide client-id

        :return: The client_id of this VidmConfiguration.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this VidmConfiguration.
        Register VMware vRealize Network Insight as an OAuth client to VMware Identity Manager and provide client-id

        :param client_id: The client_id of this VidmConfiguration.
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """
        Gets the client_secret of this VidmConfiguration.
        Provide the registered OAuth client secret

        :return: The client_secret of this VidmConfiguration.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """
        Sets the client_secret of this VidmConfiguration.
        Provide the registered OAuth client secret

        :param client_secret: The client_secret of this VidmConfiguration.
        :type: str
        """

        self._client_secret = client_secret

    @property
    def sha_thumbprint(self):
        """
        Gets the sha_thumbprint of this VidmConfiguration.
        Optionally, provide SHA thumbprint to validate VMware Identity Manager appliance that is being configured

        :return: The sha_thumbprint of this VidmConfiguration.
        :rtype: str
        """
        return self._sha_thumbprint

    @sha_thumbprint.setter
    def sha_thumbprint(self, sha_thumbprint):
        """
        Sets the sha_thumbprint of this VidmConfiguration.
        Optionally, provide SHA thumbprint to validate VMware Identity Manager appliance that is being configured

        :param sha_thumbprint: The sha_thumbprint of this VidmConfiguration.
        :type: str
        """

        self._sha_thumbprint = sha_thumbprint

    @property
    def enable(self):
        """
        Gets the enable of this VidmConfiguration.
        True, to enable the VMware Identity Manager integration in vRealize Network Insight

        :return: The enable of this VidmConfiguration.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """
        Sets the enable of this VidmConfiguration.
        True, to enable the VMware Identity Manager integration in vRealize Network Insight

        :param enable: The enable of this VidmConfiguration.
        :type: bool
        """

        self._enable = enable

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
        if not isinstance(other, VidmConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
