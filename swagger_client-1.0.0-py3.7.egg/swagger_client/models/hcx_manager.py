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


class HCXManager(object):
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
        'vendor_id': 'str',
        'local_site': 'Reference',
        'sddc_type': 'str',
        'cloud_provider_type': 'str',
        'endpoint_id': 'str',
        'ip_address': 'IpAddress',
        'compute_managers': 'list[Reference]',
        'sddc': 'Reference',
        'version': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'vendor_id': 'vendor_id',
        'local_site': 'local_site',
        'sddc_type': 'sddc_type',
        'cloud_provider_type': 'cloud_provider_type',
        'endpoint_id': 'endpoint_id',
        'ip_address': 'ip_address',
        'compute_managers': 'compute_managers',
        'sddc': 'sddc',
        'version': 'version'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, vendor_id=None, local_site=None, sddc_type=None, cloud_provider_type=None, endpoint_id=None, ip_address=None, compute_managers=None, sddc=None, version=None):
        """
        HCXManager - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._vendor_id = None
        self._local_site = None
        self._sddc_type = None
        self._cloud_provider_type = None
        self._endpoint_id = None
        self._ip_address = None
        self._compute_managers = None
        self._sddc = None
        self._version = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if local_site is not None:
          self.local_site = local_site
        if sddc_type is not None:
          self.sddc_type = sddc_type
        if cloud_provider_type is not None:
          self.cloud_provider_type = cloud_provider_type
        if endpoint_id is not None:
          self.endpoint_id = endpoint_id
        if ip_address is not None:
          self.ip_address = ip_address
        if compute_managers is not None:
          self.compute_managers = compute_managers
        if sddc is not None:
          self.sddc = sddc
        if version is not None:
          self.version = version

    @property
    def entity_id(self):
        """
        Gets the entity_id of this HCXManager.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this HCXManager.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this HCXManager.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this HCXManager.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this HCXManager.
        Name of the object

        :return: The name of this HCXManager.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HCXManager.
        Name of the object

        :param name: The name of this HCXManager.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this HCXManager.

        :return: The entity_type of this HCXManager.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this HCXManager.

        :param entity_type: The entity_type of this HCXManager.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this HCXManager.

        :return: The vendor_id of this HCXManager.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this HCXManager.

        :param vendor_id: The vendor_id of this HCXManager.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def local_site(self):
        """
        Gets the local_site of this HCXManager.

        :return: The local_site of this HCXManager.
        :rtype: Reference
        """
        return self._local_site

    @local_site.setter
    def local_site(self, local_site):
        """
        Sets the local_site of this HCXManager.

        :param local_site: The local_site of this HCXManager.
        :type: Reference
        """

        self._local_site = local_site

    @property
    def sddc_type(self):
        """
        Gets the sddc_type of this HCXManager.

        :return: The sddc_type of this HCXManager.
        :rtype: str
        """
        return self._sddc_type

    @sddc_type.setter
    def sddc_type(self, sddc_type):
        """
        Sets the sddc_type of this HCXManager.

        :param sddc_type: The sddc_type of this HCXManager.
        :type: str
        """

        self._sddc_type = sddc_type

    @property
    def cloud_provider_type(self):
        """
        Gets the cloud_provider_type of this HCXManager.

        :return: The cloud_provider_type of this HCXManager.
        :rtype: str
        """
        return self._cloud_provider_type

    @cloud_provider_type.setter
    def cloud_provider_type(self, cloud_provider_type):
        """
        Sets the cloud_provider_type of this HCXManager.

        :param cloud_provider_type: The cloud_provider_type of this HCXManager.
        :type: str
        """

        self._cloud_provider_type = cloud_provider_type

    @property
    def endpoint_id(self):
        """
        Gets the endpoint_id of this HCXManager.

        :return: The endpoint_id of this HCXManager.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """
        Sets the endpoint_id of this HCXManager.

        :param endpoint_id: The endpoint_id of this HCXManager.
        :type: str
        """

        self._endpoint_id = endpoint_id

    @property
    def ip_address(self):
        """
        Gets the ip_address of this HCXManager.

        :return: The ip_address of this HCXManager.
        :rtype: IpAddress
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this HCXManager.

        :param ip_address: The ip_address of this HCXManager.
        :type: IpAddress
        """

        self._ip_address = ip_address

    @property
    def compute_managers(self):
        """
        Gets the compute_managers of this HCXManager.

        :return: The compute_managers of this HCXManager.
        :rtype: list[Reference]
        """
        return self._compute_managers

    @compute_managers.setter
    def compute_managers(self, compute_managers):
        """
        Sets the compute_managers of this HCXManager.

        :param compute_managers: The compute_managers of this HCXManager.
        :type: list[Reference]
        """

        self._compute_managers = compute_managers

    @property
    def sddc(self):
        """
        Gets the sddc of this HCXManager.

        :return: The sddc of this HCXManager.
        :rtype: Reference
        """
        return self._sddc

    @sddc.setter
    def sddc(self, sddc):
        """
        Sets the sddc of this HCXManager.

        :param sddc: The sddc of this HCXManager.
        :type: Reference
        """

        self._sddc = sddc

    @property
    def version(self):
        """
        Gets the version of this HCXManager.

        :return: The version of this HCXManager.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this HCXManager.

        :param version: The version of this HCXManager.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, HCXManager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
