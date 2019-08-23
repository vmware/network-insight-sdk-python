# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class KubernetesService(object):
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
        'kubernetes_cluster': 'Reference',
        'manager': 'Reference',
        'annotations': 'list[str]',
        'labels': 'list[str]',
        'creation_timestamp': 'str',
        'namespace': 'Reference',
        'cluster_ip': 'IpV4Address',
        'loadbalancer_ip': 'IpV4Address',
        'type': 'str',
        'external_ips': 'list[IpV4Address]',
        'selectors': 'list[str]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'vendor_id': 'vendor_id',
        'kubernetes_cluster': 'kubernetes_cluster',
        'manager': 'manager',
        'annotations': 'annotations',
        'labels': 'labels',
        'creation_timestamp': 'creation_timestamp',
        'namespace': 'namespace',
        'cluster_ip': 'cluster_ip',
        'loadbalancer_ip': 'loadbalancer_ip',
        'type': 'type',
        'external_ips': 'external_ips',
        'selectors': 'selectors'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, vendor_id=None, kubernetes_cluster=None, manager=None, annotations=None, labels=None, creation_timestamp=None, namespace=None, cluster_ip=None, loadbalancer_ip=None, type=None, external_ips=None, selectors=None):
        """
        KubernetesService - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._vendor_id = None
        self._kubernetes_cluster = None
        self._manager = None
        self._annotations = None
        self._labels = None
        self._creation_timestamp = None
        self._namespace = None
        self._cluster_ip = None
        self._loadbalancer_ip = None
        self._type = None
        self._external_ips = None
        self._selectors = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if kubernetes_cluster is not None:
          self.kubernetes_cluster = kubernetes_cluster
        if manager is not None:
          self.manager = manager
        if annotations is not None:
          self.annotations = annotations
        if labels is not None:
          self.labels = labels
        if creation_timestamp is not None:
          self.creation_timestamp = creation_timestamp
        if namespace is not None:
          self.namespace = namespace
        if cluster_ip is not None:
          self.cluster_ip = cluster_ip
        if loadbalancer_ip is not None:
          self.loadbalancer_ip = loadbalancer_ip
        if type is not None:
          self.type = type
        if external_ips is not None:
          self.external_ips = external_ips
        if selectors is not None:
          self.selectors = selectors

    @property
    def entity_id(self):
        """
        Gets the entity_id of this KubernetesService.

        :return: The entity_id of this KubernetesService.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this KubernetesService.

        :param entity_id: The entity_id of this KubernetesService.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this KubernetesService.

        :return: The name of this KubernetesService.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this KubernetesService.

        :param name: The name of this KubernetesService.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this KubernetesService.

        :return: The entity_type of this KubernetesService.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this KubernetesService.

        :param entity_type: The entity_type of this KubernetesService.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this KubernetesService.

        :return: The vendor_id of this KubernetesService.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this KubernetesService.

        :param vendor_id: The vendor_id of this KubernetesService.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def kubernetes_cluster(self):
        """
        Gets the kubernetes_cluster of this KubernetesService.

        :return: The kubernetes_cluster of this KubernetesService.
        :rtype: Reference
        """
        return self._kubernetes_cluster

    @kubernetes_cluster.setter
    def kubernetes_cluster(self, kubernetes_cluster):
        """
        Sets the kubernetes_cluster of this KubernetesService.

        :param kubernetes_cluster: The kubernetes_cluster of this KubernetesService.
        :type: Reference
        """

        self._kubernetes_cluster = kubernetes_cluster

    @property
    def manager(self):
        """
        Gets the manager of this KubernetesService.

        :return: The manager of this KubernetesService.
        :rtype: Reference
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this KubernetesService.

        :param manager: The manager of this KubernetesService.
        :type: Reference
        """

        self._manager = manager

    @property
    def annotations(self):
        """
        Gets the annotations of this KubernetesService.

        :return: The annotations of this KubernetesService.
        :rtype: list[str]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """
        Sets the annotations of this KubernetesService.

        :param annotations: The annotations of this KubernetesService.
        :type: list[str]
        """

        self._annotations = annotations

    @property
    def labels(self):
        """
        Gets the labels of this KubernetesService.

        :return: The labels of this KubernetesService.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this KubernetesService.

        :param labels: The labels of this KubernetesService.
        :type: list[str]
        """

        self._labels = labels

    @property
    def creation_timestamp(self):
        """
        Gets the creation_timestamp of this KubernetesService.

        :return: The creation_timestamp of this KubernetesService.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """
        Sets the creation_timestamp of this KubernetesService.

        :param creation_timestamp: The creation_timestamp of this KubernetesService.
        :type: str
        """

        self._creation_timestamp = creation_timestamp

    @property
    def namespace(self):
        """
        Gets the namespace of this KubernetesService.

        :return: The namespace of this KubernetesService.
        :rtype: Reference
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this KubernetesService.

        :param namespace: The namespace of this KubernetesService.
        :type: Reference
        """

        self._namespace = namespace

    @property
    def cluster_ip(self):
        """
        Gets the cluster_ip of this KubernetesService.

        :return: The cluster_ip of this KubernetesService.
        :rtype: IpV4Address
        """
        return self._cluster_ip

    @cluster_ip.setter
    def cluster_ip(self, cluster_ip):
        """
        Sets the cluster_ip of this KubernetesService.

        :param cluster_ip: The cluster_ip of this KubernetesService.
        :type: IpV4Address
        """

        self._cluster_ip = cluster_ip

    @property
    def loadbalancer_ip(self):
        """
        Gets the loadbalancer_ip of this KubernetesService.

        :return: The loadbalancer_ip of this KubernetesService.
        :rtype: IpV4Address
        """
        return self._loadbalancer_ip

    @loadbalancer_ip.setter
    def loadbalancer_ip(self, loadbalancer_ip):
        """
        Sets the loadbalancer_ip of this KubernetesService.

        :param loadbalancer_ip: The loadbalancer_ip of this KubernetesService.
        :type: IpV4Address
        """

        self._loadbalancer_ip = loadbalancer_ip

    @property
    def type(self):
        """
        Gets the type of this KubernetesService.

        :return: The type of this KubernetesService.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this KubernetesService.

        :param type: The type of this KubernetesService.
        :type: str
        """

        self._type = type

    @property
    def external_ips(self):
        """
        Gets the external_ips of this KubernetesService.

        :return: The external_ips of this KubernetesService.
        :rtype: list[IpV4Address]
        """
        return self._external_ips

    @external_ips.setter
    def external_ips(self, external_ips):
        """
        Sets the external_ips of this KubernetesService.

        :param external_ips: The external_ips of this KubernetesService.
        :type: list[IpV4Address]
        """

        self._external_ips = external_ips

    @property
    def selectors(self):
        """
        Gets the selectors of this KubernetesService.

        :return: The selectors of this KubernetesService.
        :rtype: list[str]
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """
        Sets the selectors of this KubernetesService.

        :param selectors: The selectors of this KubernetesService.
        :type: list[str]
        """

        self._selectors = selectors

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
        if not isinstance(other, KubernetesService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
