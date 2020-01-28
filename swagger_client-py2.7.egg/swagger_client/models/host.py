# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Host(object):
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
        'vmknics': 'list[Reference]',
        'cluster': 'Reference',
        'vcenter_manager': 'Reference',
        'vm_count': 'int',
        'datastores': 'list[Reference]',
        'service_tag': 'str',
        'vendor_id': 'str',
        'nsx_manager': 'Reference',
        'maintenance_mode': 'str',
        'connection_state': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'vmknics': 'vmknics',
        'cluster': 'cluster',
        'vcenter_manager': 'vcenter_manager',
        'vm_count': 'vm_count',
        'datastores': 'datastores',
        'service_tag': 'service_tag',
        'vendor_id': 'vendor_id',
        'nsx_manager': 'nsx_manager',
        'maintenance_mode': 'maintenance_mode',
        'connection_state': 'connection_state'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, vmknics=None, cluster=None, vcenter_manager=None, vm_count=None, datastores=None, service_tag=None, vendor_id=None, nsx_manager=None, maintenance_mode=None, connection_state=None):
        """
        Host - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._vmknics = None
        self._cluster = None
        self._vcenter_manager = None
        self._vm_count = None
        self._datastores = None
        self._service_tag = None
        self._vendor_id = None
        self._nsx_manager = None
        self._maintenance_mode = None
        self._connection_state = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if vmknics is not None:
          self.vmknics = vmknics
        if cluster is not None:
          self.cluster = cluster
        if vcenter_manager is not None:
          self.vcenter_manager = vcenter_manager
        if vm_count is not None:
          self.vm_count = vm_count
        if datastores is not None:
          self.datastores = datastores
        if service_tag is not None:
          self.service_tag = service_tag
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if nsx_manager is not None:
          self.nsx_manager = nsx_manager
        if maintenance_mode is not None:
          self.maintenance_mode = maintenance_mode
        if connection_state is not None:
          self.connection_state = connection_state

    @property
    def entity_id(self):
        """
        Gets the entity_id of this Host.

        :return: The entity_id of this Host.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this Host.

        :param entity_id: The entity_id of this Host.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this Host.

        :return: The name of this Host.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Host.

        :param name: The name of this Host.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this Host.

        :return: The entity_type of this Host.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this Host.

        :param entity_type: The entity_type of this Host.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def vmknics(self):
        """
        Gets the vmknics of this Host.

        :return: The vmknics of this Host.
        :rtype: list[Reference]
        """
        return self._vmknics

    @vmknics.setter
    def vmknics(self, vmknics):
        """
        Sets the vmknics of this Host.

        :param vmknics: The vmknics of this Host.
        :type: list[Reference]
        """

        self._vmknics = vmknics

    @property
    def cluster(self):
        """
        Gets the cluster of this Host.

        :return: The cluster of this Host.
        :rtype: Reference
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """
        Sets the cluster of this Host.

        :param cluster: The cluster of this Host.
        :type: Reference
        """

        self._cluster = cluster

    @property
    def vcenter_manager(self):
        """
        Gets the vcenter_manager of this Host.

        :return: The vcenter_manager of this Host.
        :rtype: Reference
        """
        return self._vcenter_manager

    @vcenter_manager.setter
    def vcenter_manager(self, vcenter_manager):
        """
        Sets the vcenter_manager of this Host.

        :param vcenter_manager: The vcenter_manager of this Host.
        :type: Reference
        """

        self._vcenter_manager = vcenter_manager

    @property
    def vm_count(self):
        """
        Gets the vm_count of this Host.

        :return: The vm_count of this Host.
        :rtype: int
        """
        return self._vm_count

    @vm_count.setter
    def vm_count(self, vm_count):
        """
        Sets the vm_count of this Host.

        :param vm_count: The vm_count of this Host.
        :type: int
        """

        self._vm_count = vm_count

    @property
    def datastores(self):
        """
        Gets the datastores of this Host.

        :return: The datastores of this Host.
        :rtype: list[Reference]
        """
        return self._datastores

    @datastores.setter
    def datastores(self, datastores):
        """
        Sets the datastores of this Host.

        :param datastores: The datastores of this Host.
        :type: list[Reference]
        """

        self._datastores = datastores

    @property
    def service_tag(self):
        """
        Gets the service_tag of this Host.

        :return: The service_tag of this Host.
        :rtype: str
        """
        return self._service_tag

    @service_tag.setter
    def service_tag(self, service_tag):
        """
        Sets the service_tag of this Host.

        :param service_tag: The service_tag of this Host.
        :type: str
        """

        self._service_tag = service_tag

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this Host.

        :return: The vendor_id of this Host.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this Host.

        :param vendor_id: The vendor_id of this Host.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def nsx_manager(self):
        """
        Gets the nsx_manager of this Host.

        :return: The nsx_manager of this Host.
        :rtype: Reference
        """
        return self._nsx_manager

    @nsx_manager.setter
    def nsx_manager(self, nsx_manager):
        """
        Sets the nsx_manager of this Host.

        :param nsx_manager: The nsx_manager of this Host.
        :type: Reference
        """

        self._nsx_manager = nsx_manager

    @property
    def maintenance_mode(self):
        """
        Gets the maintenance_mode of this Host.

        :return: The maintenance_mode of this Host.
        :rtype: str
        """
        return self._maintenance_mode

    @maintenance_mode.setter
    def maintenance_mode(self, maintenance_mode):
        """
        Sets the maintenance_mode of this Host.

        :param maintenance_mode: The maintenance_mode of this Host.
        :type: str
        """

        self._maintenance_mode = maintenance_mode

    @property
    def connection_state(self):
        """
        Gets the connection_state of this Host.

        :return: The connection_state of this Host.
        :rtype: str
        """
        return self._connection_state

    @connection_state.setter
    def connection_state(self, connection_state):
        """
        Sets the connection_state of this Host.

        :param connection_state: The connection_state of this Host.
        :type: str
        """

        self._connection_state = connection_state

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
        if not isinstance(other, Host):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
