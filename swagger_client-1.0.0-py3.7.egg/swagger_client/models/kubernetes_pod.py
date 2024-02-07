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


class KubernetesPod(object):
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
        'manager': 'Reference',
        'kubernetes_cluster': 'Reference',
        'kubernetes_namespace': 'Reference',
        'kubernetes_service': 'list[Reference]',
        'kubernetes_node': 'Reference',
        'ip_address': 'IpAddress',
        'vm': 'Reference',
        'host': 'Reference',
        'logical_port': 'Reference',
        'labels': 'list[str]',
        'vendor_id': 'str',
        'creation_timestamp': 'str',
        'annotations': 'list[str]',
        'ready_status': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'manager': 'manager',
        'kubernetes_cluster': 'kubernetes_cluster',
        'kubernetes_namespace': 'kubernetes_namespace',
        'kubernetes_service': 'kubernetes_service',
        'kubernetes_node': 'kubernetes_node',
        'ip_address': 'ip_address',
        'vm': 'vm',
        'host': 'host',
        'logical_port': 'logical_port',
        'labels': 'labels',
        'vendor_id': 'vendor_id',
        'creation_timestamp': 'creation_timestamp',
        'annotations': 'annotations',
        'ready_status': 'ready_status'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, manager=None, kubernetes_cluster=None, kubernetes_namespace=None, kubernetes_service=None, kubernetes_node=None, ip_address=None, vm=None, host=None, logical_port=None, labels=None, vendor_id=None, creation_timestamp=None, annotations=None, ready_status=None):
        """
        KubernetesPod - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._manager = None
        self._kubernetes_cluster = None
        self._kubernetes_namespace = None
        self._kubernetes_service = None
        self._kubernetes_node = None
        self._ip_address = None
        self._vm = None
        self._host = None
        self._logical_port = None
        self._labels = None
        self._vendor_id = None
        self._creation_timestamp = None
        self._annotations = None
        self._ready_status = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if manager is not None:
          self.manager = manager
        if kubernetes_cluster is not None:
          self.kubernetes_cluster = kubernetes_cluster
        if kubernetes_namespace is not None:
          self.kubernetes_namespace = kubernetes_namespace
        if kubernetes_service is not None:
          self.kubernetes_service = kubernetes_service
        if kubernetes_node is not None:
          self.kubernetes_node = kubernetes_node
        if ip_address is not None:
          self.ip_address = ip_address
        if vm is not None:
          self.vm = vm
        if host is not None:
          self.host = host
        if logical_port is not None:
          self.logical_port = logical_port
        if labels is not None:
          self.labels = labels
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if creation_timestamp is not None:
          self.creation_timestamp = creation_timestamp
        if annotations is not None:
          self.annotations = annotations
        if ready_status is not None:
          self.ready_status = ready_status

    @property
    def entity_id(self):
        """
        Gets the entity_id of this KubernetesPod.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this KubernetesPod.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this KubernetesPod.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this KubernetesPod.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this KubernetesPod.
        Name of the object

        :return: The name of this KubernetesPod.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this KubernetesPod.
        Name of the object

        :param name: The name of this KubernetesPod.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this KubernetesPod.

        :return: The entity_type of this KubernetesPod.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this KubernetesPod.

        :param entity_type: The entity_type of this KubernetesPod.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def manager(self):
        """
        Gets the manager of this KubernetesPod.

        :return: The manager of this KubernetesPod.
        :rtype: Reference
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this KubernetesPod.

        :param manager: The manager of this KubernetesPod.
        :type: Reference
        """

        self._manager = manager

    @property
    def kubernetes_cluster(self):
        """
        Gets the kubernetes_cluster of this KubernetesPod.

        :return: The kubernetes_cluster of this KubernetesPod.
        :rtype: Reference
        """
        return self._kubernetes_cluster

    @kubernetes_cluster.setter
    def kubernetes_cluster(self, kubernetes_cluster):
        """
        Sets the kubernetes_cluster of this KubernetesPod.

        :param kubernetes_cluster: The kubernetes_cluster of this KubernetesPod.
        :type: Reference
        """

        self._kubernetes_cluster = kubernetes_cluster

    @property
    def kubernetes_namespace(self):
        """
        Gets the kubernetes_namespace of this KubernetesPod.

        :return: The kubernetes_namespace of this KubernetesPod.
        :rtype: Reference
        """
        return self._kubernetes_namespace

    @kubernetes_namespace.setter
    def kubernetes_namespace(self, kubernetes_namespace):
        """
        Sets the kubernetes_namespace of this KubernetesPod.

        :param kubernetes_namespace: The kubernetes_namespace of this KubernetesPod.
        :type: Reference
        """

        self._kubernetes_namespace = kubernetes_namespace

    @property
    def kubernetes_service(self):
        """
        Gets the kubernetes_service of this KubernetesPod.

        :return: The kubernetes_service of this KubernetesPod.
        :rtype: list[Reference]
        """
        return self._kubernetes_service

    @kubernetes_service.setter
    def kubernetes_service(self, kubernetes_service):
        """
        Sets the kubernetes_service of this KubernetesPod.

        :param kubernetes_service: The kubernetes_service of this KubernetesPod.
        :type: list[Reference]
        """

        self._kubernetes_service = kubernetes_service

    @property
    def kubernetes_node(self):
        """
        Gets the kubernetes_node of this KubernetesPod.

        :return: The kubernetes_node of this KubernetesPod.
        :rtype: Reference
        """
        return self._kubernetes_node

    @kubernetes_node.setter
    def kubernetes_node(self, kubernetes_node):
        """
        Sets the kubernetes_node of this KubernetesPod.

        :param kubernetes_node: The kubernetes_node of this KubernetesPod.
        :type: Reference
        """

        self._kubernetes_node = kubernetes_node

    @property
    def ip_address(self):
        """
        Gets the ip_address of this KubernetesPod.

        :return: The ip_address of this KubernetesPod.
        :rtype: IpAddress
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this KubernetesPod.

        :param ip_address: The ip_address of this KubernetesPod.
        :type: IpAddress
        """

        self._ip_address = ip_address

    @property
    def vm(self):
        """
        Gets the vm of this KubernetesPod.

        :return: The vm of this KubernetesPod.
        :rtype: Reference
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """
        Sets the vm of this KubernetesPod.

        :param vm: The vm of this KubernetesPod.
        :type: Reference
        """

        self._vm = vm

    @property
    def host(self):
        """
        Gets the host of this KubernetesPod.

        :return: The host of this KubernetesPod.
        :rtype: Reference
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this KubernetesPod.

        :param host: The host of this KubernetesPod.
        :type: Reference
        """

        self._host = host

    @property
    def logical_port(self):
        """
        Gets the logical_port of this KubernetesPod.

        :return: The logical_port of this KubernetesPod.
        :rtype: Reference
        """
        return self._logical_port

    @logical_port.setter
    def logical_port(self, logical_port):
        """
        Sets the logical_port of this KubernetesPod.

        :param logical_port: The logical_port of this KubernetesPod.
        :type: Reference
        """

        self._logical_port = logical_port

    @property
    def labels(self):
        """
        Gets the labels of this KubernetesPod.

        :return: The labels of this KubernetesPod.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this KubernetesPod.

        :param labels: The labels of this KubernetesPod.
        :type: list[str]
        """

        self._labels = labels

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this KubernetesPod.

        :return: The vendor_id of this KubernetesPod.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this KubernetesPod.

        :param vendor_id: The vendor_id of this KubernetesPod.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def creation_timestamp(self):
        """
        Gets the creation_timestamp of this KubernetesPod.

        :return: The creation_timestamp of this KubernetesPod.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """
        Sets the creation_timestamp of this KubernetesPod.

        :param creation_timestamp: The creation_timestamp of this KubernetesPod.
        :type: str
        """

        self._creation_timestamp = creation_timestamp

    @property
    def annotations(self):
        """
        Gets the annotations of this KubernetesPod.

        :return: The annotations of this KubernetesPod.
        :rtype: list[str]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """
        Sets the annotations of this KubernetesPod.

        :param annotations: The annotations of this KubernetesPod.
        :type: list[str]
        """

        self._annotations = annotations

    @property
    def ready_status(self):
        """
        Gets the ready_status of this KubernetesPod.

        :return: The ready_status of this KubernetesPod.
        :rtype: str
        """
        return self._ready_status

    @ready_status.setter
    def ready_status(self, ready_status):
        """
        Sets the ready_status of this KubernetesPod.

        :param ready_status: The ready_status of this KubernetesPod.
        :type: str
        """

        self._ready_status = ready_status

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
        if not isinstance(other, KubernetesPod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
