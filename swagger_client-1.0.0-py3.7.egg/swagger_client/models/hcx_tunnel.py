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


class HCXTunnel(object):
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
        'manager': 'Reference',
        'local_address': 'IpAddress',
        'remote_address': 'IpAddress',
        'local_port': 'int',
        'remote_port': 'int',
        'source_appliance': 'Reference',
        'remote_appliance': 'Reference',
        'tunnel_type': 'str',
        'tunnel_state': 'str',
        'local_site': 'Reference',
        'remote_site': 'Reference',
        'l2_extensions': 'list[Reference]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'vendor_id': 'vendor_id',
        'manager': 'manager',
        'local_address': 'local_address',
        'remote_address': 'remote_address',
        'local_port': 'local_port',
        'remote_port': 'remote_port',
        'source_appliance': 'source_appliance',
        'remote_appliance': 'remote_appliance',
        'tunnel_type': 'tunnel_type',
        'tunnel_state': 'tunnel_state',
        'local_site': 'local_site',
        'remote_site': 'remote_site',
        'l2_extensions': 'l2_extensions'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, vendor_id=None, manager=None, local_address=None, remote_address=None, local_port=None, remote_port=None, source_appliance=None, remote_appliance=None, tunnel_type=None, tunnel_state=None, local_site=None, remote_site=None, l2_extensions=None):
        """
        HCXTunnel - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._vendor_id = None
        self._manager = None
        self._local_address = None
        self._remote_address = None
        self._local_port = None
        self._remote_port = None
        self._source_appliance = None
        self._remote_appliance = None
        self._tunnel_type = None
        self._tunnel_state = None
        self._local_site = None
        self._remote_site = None
        self._l2_extensions = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if manager is not None:
          self.manager = manager
        if local_address is not None:
          self.local_address = local_address
        if remote_address is not None:
          self.remote_address = remote_address
        if local_port is not None:
          self.local_port = local_port
        if remote_port is not None:
          self.remote_port = remote_port
        if source_appliance is not None:
          self.source_appliance = source_appliance
        if remote_appliance is not None:
          self.remote_appliance = remote_appliance
        if tunnel_type is not None:
          self.tunnel_type = tunnel_type
        if tunnel_state is not None:
          self.tunnel_state = tunnel_state
        if local_site is not None:
          self.local_site = local_site
        if remote_site is not None:
          self.remote_site = remote_site
        if l2_extensions is not None:
          self.l2_extensions = l2_extensions

    @property
    def entity_id(self):
        """
        Gets the entity_id of this HCXTunnel.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this HCXTunnel.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this HCXTunnel.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this HCXTunnel.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this HCXTunnel.
        Name of the object

        :return: The name of this HCXTunnel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HCXTunnel.
        Name of the object

        :param name: The name of this HCXTunnel.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this HCXTunnel.

        :return: The entity_type of this HCXTunnel.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this HCXTunnel.

        :param entity_type: The entity_type of this HCXTunnel.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this HCXTunnel.

        :return: The vendor_id of this HCXTunnel.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this HCXTunnel.

        :param vendor_id: The vendor_id of this HCXTunnel.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def manager(self):
        """
        Gets the manager of this HCXTunnel.

        :return: The manager of this HCXTunnel.
        :rtype: Reference
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this HCXTunnel.

        :param manager: The manager of this HCXTunnel.
        :type: Reference
        """

        self._manager = manager

    @property
    def local_address(self):
        """
        Gets the local_address of this HCXTunnel.

        :return: The local_address of this HCXTunnel.
        :rtype: IpAddress
        """
        return self._local_address

    @local_address.setter
    def local_address(self, local_address):
        """
        Sets the local_address of this HCXTunnel.

        :param local_address: The local_address of this HCXTunnel.
        :type: IpAddress
        """

        self._local_address = local_address

    @property
    def remote_address(self):
        """
        Gets the remote_address of this HCXTunnel.

        :return: The remote_address of this HCXTunnel.
        :rtype: IpAddress
        """
        return self._remote_address

    @remote_address.setter
    def remote_address(self, remote_address):
        """
        Sets the remote_address of this HCXTunnel.

        :param remote_address: The remote_address of this HCXTunnel.
        :type: IpAddress
        """

        self._remote_address = remote_address

    @property
    def local_port(self):
        """
        Gets the local_port of this HCXTunnel.

        :return: The local_port of this HCXTunnel.
        :rtype: int
        """
        return self._local_port

    @local_port.setter
    def local_port(self, local_port):
        """
        Sets the local_port of this HCXTunnel.

        :param local_port: The local_port of this HCXTunnel.
        :type: int
        """

        self._local_port = local_port

    @property
    def remote_port(self):
        """
        Gets the remote_port of this HCXTunnel.

        :return: The remote_port of this HCXTunnel.
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        """
        Sets the remote_port of this HCXTunnel.

        :param remote_port: The remote_port of this HCXTunnel.
        :type: int
        """

        self._remote_port = remote_port

    @property
    def source_appliance(self):
        """
        Gets the source_appliance of this HCXTunnel.

        :return: The source_appliance of this HCXTunnel.
        :rtype: Reference
        """
        return self._source_appliance

    @source_appliance.setter
    def source_appliance(self, source_appliance):
        """
        Sets the source_appliance of this HCXTunnel.

        :param source_appliance: The source_appliance of this HCXTunnel.
        :type: Reference
        """

        self._source_appliance = source_appliance

    @property
    def remote_appliance(self):
        """
        Gets the remote_appliance of this HCXTunnel.

        :return: The remote_appliance of this HCXTunnel.
        :rtype: Reference
        """
        return self._remote_appliance

    @remote_appliance.setter
    def remote_appliance(self, remote_appliance):
        """
        Sets the remote_appliance of this HCXTunnel.

        :param remote_appliance: The remote_appliance of this HCXTunnel.
        :type: Reference
        """

        self._remote_appliance = remote_appliance

    @property
    def tunnel_type(self):
        """
        Gets the tunnel_type of this HCXTunnel.

        :return: The tunnel_type of this HCXTunnel.
        :rtype: str
        """
        return self._tunnel_type

    @tunnel_type.setter
    def tunnel_type(self, tunnel_type):
        """
        Sets the tunnel_type of this HCXTunnel.

        :param tunnel_type: The tunnel_type of this HCXTunnel.
        :type: str
        """

        self._tunnel_type = tunnel_type

    @property
    def tunnel_state(self):
        """
        Gets the tunnel_state of this HCXTunnel.

        :return: The tunnel_state of this HCXTunnel.
        :rtype: str
        """
        return self._tunnel_state

    @tunnel_state.setter
    def tunnel_state(self, tunnel_state):
        """
        Sets the tunnel_state of this HCXTunnel.

        :param tunnel_state: The tunnel_state of this HCXTunnel.
        :type: str
        """

        self._tunnel_state = tunnel_state

    @property
    def local_site(self):
        """
        Gets the local_site of this HCXTunnel.

        :return: The local_site of this HCXTunnel.
        :rtype: Reference
        """
        return self._local_site

    @local_site.setter
    def local_site(self, local_site):
        """
        Sets the local_site of this HCXTunnel.

        :param local_site: The local_site of this HCXTunnel.
        :type: Reference
        """

        self._local_site = local_site

    @property
    def remote_site(self):
        """
        Gets the remote_site of this HCXTunnel.

        :return: The remote_site of this HCXTunnel.
        :rtype: Reference
        """
        return self._remote_site

    @remote_site.setter
    def remote_site(self, remote_site):
        """
        Sets the remote_site of this HCXTunnel.

        :param remote_site: The remote_site of this HCXTunnel.
        :type: Reference
        """

        self._remote_site = remote_site

    @property
    def l2_extensions(self):
        """
        Gets the l2_extensions of this HCXTunnel.

        :return: The l2_extensions of this HCXTunnel.
        :rtype: list[Reference]
        """
        return self._l2_extensions

    @l2_extensions.setter
    def l2_extensions(self, l2_extensions):
        """
        Sets the l2_extensions of this HCXTunnel.

        :param l2_extensions: The l2_extensions of this HCXTunnel.
        :type: list[Reference]
        """

        self._l2_extensions = l2_extensions

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
        if not isinstance(other, HCXTunnel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
