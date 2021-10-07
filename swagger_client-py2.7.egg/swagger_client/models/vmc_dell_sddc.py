# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 6.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VMCDellSDDC(object):
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
        'nsx_manager': 'Reference',
        'vcenter_manager': 'Reference',
        'sddc_id': 'str',
        'org_id': 'str',
        'org_name': 'str',
        'vc_private_ip': 'IpV4Address',
        'vc_public_ip': 'IpV4Address',
        'vc_fqdn': 'str',
        'nsx_private_ip': 'IpV4Address',
        'nsx_public_ip': 'IpV4Address',
        'nsx_fqdn': 'str',
        'cloud_provider_type': 'CloudProviderTypeEnum'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'nsx_manager': 'nsx_manager',
        'vcenter_manager': 'vcenter_manager',
        'sddc_id': 'sddc_id',
        'org_id': 'org_id',
        'org_name': 'org_name',
        'vc_private_ip': 'vc_private_ip',
        'vc_public_ip': 'vc_public_ip',
        'vc_fqdn': 'vc_fqdn',
        'nsx_private_ip': 'nsx_private_ip',
        'nsx_public_ip': 'nsx_public_ip',
        'nsx_fqdn': 'nsx_fqdn',
        'cloud_provider_type': 'cloud_provider_type'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, nsx_manager=None, vcenter_manager=None, sddc_id=None, org_id=None, org_name=None, vc_private_ip=None, vc_public_ip=None, vc_fqdn=None, nsx_private_ip=None, nsx_public_ip=None, nsx_fqdn=None, cloud_provider_type=None):
        """
        VMCDellSDDC - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._nsx_manager = None
        self._vcenter_manager = None
        self._sddc_id = None
        self._org_id = None
        self._org_name = None
        self._vc_private_ip = None
        self._vc_public_ip = None
        self._vc_fqdn = None
        self._nsx_private_ip = None
        self._nsx_public_ip = None
        self._nsx_fqdn = None
        self._cloud_provider_type = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if nsx_manager is not None:
          self.nsx_manager = nsx_manager
        if vcenter_manager is not None:
          self.vcenter_manager = vcenter_manager
        if sddc_id is not None:
          self.sddc_id = sddc_id
        if org_id is not None:
          self.org_id = org_id
        if org_name is not None:
          self.org_name = org_name
        if vc_private_ip is not None:
          self.vc_private_ip = vc_private_ip
        if vc_public_ip is not None:
          self.vc_public_ip = vc_public_ip
        if vc_fqdn is not None:
          self.vc_fqdn = vc_fqdn
        if nsx_private_ip is not None:
          self.nsx_private_ip = nsx_private_ip
        if nsx_public_ip is not None:
          self.nsx_public_ip = nsx_public_ip
        if nsx_fqdn is not None:
          self.nsx_fqdn = nsx_fqdn
        if cloud_provider_type is not None:
          self.cloud_provider_type = cloud_provider_type

    @property
    def entity_id(self):
        """
        Gets the entity_id of this VMCDellSDDC.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this VMCDellSDDC.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this VMCDellSDDC.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this VMCDellSDDC.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this VMCDellSDDC.
        Name of the object

        :return: The name of this VMCDellSDDC.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VMCDellSDDC.
        Name of the object

        :param name: The name of this VMCDellSDDC.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this VMCDellSDDC.

        :return: The entity_type of this VMCDellSDDC.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this VMCDellSDDC.

        :param entity_type: The entity_type of this VMCDellSDDC.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def nsx_manager(self):
        """
        Gets the nsx_manager of this VMCDellSDDC.

        :return: The nsx_manager of this VMCDellSDDC.
        :rtype: Reference
        """
        return self._nsx_manager

    @nsx_manager.setter
    def nsx_manager(self, nsx_manager):
        """
        Sets the nsx_manager of this VMCDellSDDC.

        :param nsx_manager: The nsx_manager of this VMCDellSDDC.
        :type: Reference
        """

        self._nsx_manager = nsx_manager

    @property
    def vcenter_manager(self):
        """
        Gets the vcenter_manager of this VMCDellSDDC.

        :return: The vcenter_manager of this VMCDellSDDC.
        :rtype: Reference
        """
        return self._vcenter_manager

    @vcenter_manager.setter
    def vcenter_manager(self, vcenter_manager):
        """
        Sets the vcenter_manager of this VMCDellSDDC.

        :param vcenter_manager: The vcenter_manager of this VMCDellSDDC.
        :type: Reference
        """

        self._vcenter_manager = vcenter_manager

    @property
    def sddc_id(self):
        """
        Gets the sddc_id of this VMCDellSDDC.

        :return: The sddc_id of this VMCDellSDDC.
        :rtype: str
        """
        return self._sddc_id

    @sddc_id.setter
    def sddc_id(self, sddc_id):
        """
        Sets the sddc_id of this VMCDellSDDC.

        :param sddc_id: The sddc_id of this VMCDellSDDC.
        :type: str
        """

        self._sddc_id = sddc_id

    @property
    def org_id(self):
        """
        Gets the org_id of this VMCDellSDDC.

        :return: The org_id of this VMCDellSDDC.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """
        Sets the org_id of this VMCDellSDDC.

        :param org_id: The org_id of this VMCDellSDDC.
        :type: str
        """

        self._org_id = org_id

    @property
    def org_name(self):
        """
        Gets the org_name of this VMCDellSDDC.

        :return: The org_name of this VMCDellSDDC.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """
        Sets the org_name of this VMCDellSDDC.

        :param org_name: The org_name of this VMCDellSDDC.
        :type: str
        """

        self._org_name = org_name

    @property
    def vc_private_ip(self):
        """
        Gets the vc_private_ip of this VMCDellSDDC.

        :return: The vc_private_ip of this VMCDellSDDC.
        :rtype: IpV4Address
        """
        return self._vc_private_ip

    @vc_private_ip.setter
    def vc_private_ip(self, vc_private_ip):
        """
        Sets the vc_private_ip of this VMCDellSDDC.

        :param vc_private_ip: The vc_private_ip of this VMCDellSDDC.
        :type: IpV4Address
        """

        self._vc_private_ip = vc_private_ip

    @property
    def vc_public_ip(self):
        """
        Gets the vc_public_ip of this VMCDellSDDC.

        :return: The vc_public_ip of this VMCDellSDDC.
        :rtype: IpV4Address
        """
        return self._vc_public_ip

    @vc_public_ip.setter
    def vc_public_ip(self, vc_public_ip):
        """
        Sets the vc_public_ip of this VMCDellSDDC.

        :param vc_public_ip: The vc_public_ip of this VMCDellSDDC.
        :type: IpV4Address
        """

        self._vc_public_ip = vc_public_ip

    @property
    def vc_fqdn(self):
        """
        Gets the vc_fqdn of this VMCDellSDDC.

        :return: The vc_fqdn of this VMCDellSDDC.
        :rtype: str
        """
        return self._vc_fqdn

    @vc_fqdn.setter
    def vc_fqdn(self, vc_fqdn):
        """
        Sets the vc_fqdn of this VMCDellSDDC.

        :param vc_fqdn: The vc_fqdn of this VMCDellSDDC.
        :type: str
        """

        self._vc_fqdn = vc_fqdn

    @property
    def nsx_private_ip(self):
        """
        Gets the nsx_private_ip of this VMCDellSDDC.

        :return: The nsx_private_ip of this VMCDellSDDC.
        :rtype: IpV4Address
        """
        return self._nsx_private_ip

    @nsx_private_ip.setter
    def nsx_private_ip(self, nsx_private_ip):
        """
        Sets the nsx_private_ip of this VMCDellSDDC.

        :param nsx_private_ip: The nsx_private_ip of this VMCDellSDDC.
        :type: IpV4Address
        """

        self._nsx_private_ip = nsx_private_ip

    @property
    def nsx_public_ip(self):
        """
        Gets the nsx_public_ip of this VMCDellSDDC.

        :return: The nsx_public_ip of this VMCDellSDDC.
        :rtype: IpV4Address
        """
        return self._nsx_public_ip

    @nsx_public_ip.setter
    def nsx_public_ip(self, nsx_public_ip):
        """
        Sets the nsx_public_ip of this VMCDellSDDC.

        :param nsx_public_ip: The nsx_public_ip of this VMCDellSDDC.
        :type: IpV4Address
        """

        self._nsx_public_ip = nsx_public_ip

    @property
    def nsx_fqdn(self):
        """
        Gets the nsx_fqdn of this VMCDellSDDC.

        :return: The nsx_fqdn of this VMCDellSDDC.
        :rtype: str
        """
        return self._nsx_fqdn

    @nsx_fqdn.setter
    def nsx_fqdn(self, nsx_fqdn):
        """
        Sets the nsx_fqdn of this VMCDellSDDC.

        :param nsx_fqdn: The nsx_fqdn of this VMCDellSDDC.
        :type: str
        """

        self._nsx_fqdn = nsx_fqdn

    @property
    def cloud_provider_type(self):
        """
        Gets the cloud_provider_type of this VMCDellSDDC.

        :return: The cloud_provider_type of this VMCDellSDDC.
        :rtype: CloudProviderTypeEnum
        """
        return self._cloud_provider_type

    @cloud_provider_type.setter
    def cloud_provider_type(self, cloud_provider_type):
        """
        Sets the cloud_provider_type of this VMCDellSDDC.

        :param cloud_provider_type: The cloud_provider_type of this VMCDellSDDC.
        :type: CloudProviderTypeEnum
        """

        self._cloud_provider_type = cloud_provider_type

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
        if not isinstance(other, VMCDellSDDC):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
