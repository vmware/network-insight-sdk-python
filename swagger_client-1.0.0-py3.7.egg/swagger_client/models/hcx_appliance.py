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


class HCXAppliance(object):
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
        'appliance_type': 'str',
        'service_mesh': 'Reference',
        'site': 'Reference',
        'compute_profile': 'Reference',
        'peer_appliances': 'list[Reference]',
        'tunnels': 'list[Reference]',
        'compute_manager': 'Reference',
        'state': 'str',
        'appliance_version': 'str',
        'appliance_status': 'HCXApplianceStatus',
        'manager': 'Reference',
        'device': 'Reference'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'vendor_id': 'vendor_id',
        'appliance_type': 'appliance_type',
        'service_mesh': 'service_mesh',
        'site': 'site',
        'compute_profile': 'compute_profile',
        'peer_appliances': 'peer_appliances',
        'tunnels': 'tunnels',
        'compute_manager': 'compute_manager',
        'state': 'state',
        'appliance_version': 'appliance_version',
        'appliance_status': 'appliance_status',
        'manager': 'manager',
        'device': 'device'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, vendor_id=None, appliance_type=None, service_mesh=None, site=None, compute_profile=None, peer_appliances=None, tunnels=None, compute_manager=None, state=None, appliance_version=None, appliance_status=None, manager=None, device=None):
        """
        HCXAppliance - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._vendor_id = None
        self._appliance_type = None
        self._service_mesh = None
        self._site = None
        self._compute_profile = None
        self._peer_appliances = None
        self._tunnels = None
        self._compute_manager = None
        self._state = None
        self._appliance_version = None
        self._appliance_status = None
        self._manager = None
        self._device = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if appliance_type is not None:
          self.appliance_type = appliance_type
        if service_mesh is not None:
          self.service_mesh = service_mesh
        if site is not None:
          self.site = site
        if compute_profile is not None:
          self.compute_profile = compute_profile
        if peer_appliances is not None:
          self.peer_appliances = peer_appliances
        if tunnels is not None:
          self.tunnels = tunnels
        if compute_manager is not None:
          self.compute_manager = compute_manager
        if state is not None:
          self.state = state
        if appliance_version is not None:
          self.appliance_version = appliance_version
        if appliance_status is not None:
          self.appliance_status = appliance_status
        if manager is not None:
          self.manager = manager
        if device is not None:
          self.device = device

    @property
    def entity_id(self):
        """
        Gets the entity_id of this HCXAppliance.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this HCXAppliance.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this HCXAppliance.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this HCXAppliance.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this HCXAppliance.
        Name of the object

        :return: The name of this HCXAppliance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HCXAppliance.
        Name of the object

        :param name: The name of this HCXAppliance.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this HCXAppliance.

        :return: The entity_type of this HCXAppliance.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this HCXAppliance.

        :param entity_type: The entity_type of this HCXAppliance.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this HCXAppliance.

        :return: The vendor_id of this HCXAppliance.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this HCXAppliance.

        :param vendor_id: The vendor_id of this HCXAppliance.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def appliance_type(self):
        """
        Gets the appliance_type of this HCXAppliance.

        :return: The appliance_type of this HCXAppliance.
        :rtype: str
        """
        return self._appliance_type

    @appliance_type.setter
    def appliance_type(self, appliance_type):
        """
        Sets the appliance_type of this HCXAppliance.

        :param appliance_type: The appliance_type of this HCXAppliance.
        :type: str
        """

        self._appliance_type = appliance_type

    @property
    def service_mesh(self):
        """
        Gets the service_mesh of this HCXAppliance.

        :return: The service_mesh of this HCXAppliance.
        :rtype: Reference
        """
        return self._service_mesh

    @service_mesh.setter
    def service_mesh(self, service_mesh):
        """
        Sets the service_mesh of this HCXAppliance.

        :param service_mesh: The service_mesh of this HCXAppliance.
        :type: Reference
        """

        self._service_mesh = service_mesh

    @property
    def site(self):
        """
        Gets the site of this HCXAppliance.

        :return: The site of this HCXAppliance.
        :rtype: Reference
        """
        return self._site

    @site.setter
    def site(self, site):
        """
        Sets the site of this HCXAppliance.

        :param site: The site of this HCXAppliance.
        :type: Reference
        """

        self._site = site

    @property
    def compute_profile(self):
        """
        Gets the compute_profile of this HCXAppliance.

        :return: The compute_profile of this HCXAppliance.
        :rtype: Reference
        """
        return self._compute_profile

    @compute_profile.setter
    def compute_profile(self, compute_profile):
        """
        Sets the compute_profile of this HCXAppliance.

        :param compute_profile: The compute_profile of this HCXAppliance.
        :type: Reference
        """

        self._compute_profile = compute_profile

    @property
    def peer_appliances(self):
        """
        Gets the peer_appliances of this HCXAppliance.

        :return: The peer_appliances of this HCXAppliance.
        :rtype: list[Reference]
        """
        return self._peer_appliances

    @peer_appliances.setter
    def peer_appliances(self, peer_appliances):
        """
        Sets the peer_appliances of this HCXAppliance.

        :param peer_appliances: The peer_appliances of this HCXAppliance.
        :type: list[Reference]
        """

        self._peer_appliances = peer_appliances

    @property
    def tunnels(self):
        """
        Gets the tunnels of this HCXAppliance.

        :return: The tunnels of this HCXAppliance.
        :rtype: list[Reference]
        """
        return self._tunnels

    @tunnels.setter
    def tunnels(self, tunnels):
        """
        Sets the tunnels of this HCXAppliance.

        :param tunnels: The tunnels of this HCXAppliance.
        :type: list[Reference]
        """

        self._tunnels = tunnels

    @property
    def compute_manager(self):
        """
        Gets the compute_manager of this HCXAppliance.

        :return: The compute_manager of this HCXAppliance.
        :rtype: Reference
        """
        return self._compute_manager

    @compute_manager.setter
    def compute_manager(self, compute_manager):
        """
        Sets the compute_manager of this HCXAppliance.

        :param compute_manager: The compute_manager of this HCXAppliance.
        :type: Reference
        """

        self._compute_manager = compute_manager

    @property
    def state(self):
        """
        Gets the state of this HCXAppliance.

        :return: The state of this HCXAppliance.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this HCXAppliance.

        :param state: The state of this HCXAppliance.
        :type: str
        """

        self._state = state

    @property
    def appliance_version(self):
        """
        Gets the appliance_version of this HCXAppliance.

        :return: The appliance_version of this HCXAppliance.
        :rtype: str
        """
        return self._appliance_version

    @appliance_version.setter
    def appliance_version(self, appliance_version):
        """
        Sets the appliance_version of this HCXAppliance.

        :param appliance_version: The appliance_version of this HCXAppliance.
        :type: str
        """

        self._appliance_version = appliance_version

    @property
    def appliance_status(self):
        """
        Gets the appliance_status of this HCXAppliance.

        :return: The appliance_status of this HCXAppliance.
        :rtype: HCXApplianceStatus
        """
        return self._appliance_status

    @appliance_status.setter
    def appliance_status(self, appliance_status):
        """
        Sets the appliance_status of this HCXAppliance.

        :param appliance_status: The appliance_status of this HCXAppliance.
        :type: HCXApplianceStatus
        """

        self._appliance_status = appliance_status

    @property
    def manager(self):
        """
        Gets the manager of this HCXAppliance.

        :return: The manager of this HCXAppliance.
        :rtype: Reference
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this HCXAppliance.

        :param manager: The manager of this HCXAppliance.
        :type: Reference
        """

        self._manager = manager

    @property
    def device(self):
        """
        Gets the device of this HCXAppliance.

        :return: The device of this HCXAppliance.
        :rtype: Reference
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this HCXAppliance.

        :param device: The device of this HCXAppliance.
        :type: Reference
        """

        self._device = device

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
        if not isinstance(other, HCXAppliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
