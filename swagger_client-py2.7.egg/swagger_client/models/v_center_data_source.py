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


class VCenterDataSource(object):
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
        'entity_type': 'DataSourceType',
        'ip': 'str',
        'fqdn': 'str',
        'proxy_id': 'str',
        'nickname': 'str',
        'enabled': 'bool',
        'notes': 'str',
        'certificate': 'str',
        'sha_thumbprint': 'str',
        'new_certificate': 'str',
        'new_sha_thumbprint': 'str',
        'credentials': 'PasswordCredentials',
        'ipfix_request': 'DvsIpfixRequest',
        'ipfix_response': 'DvsIpfixResponse',
        'is_vmc': 'bool'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'ip': 'ip',
        'fqdn': 'fqdn',
        'proxy_id': 'proxy_id',
        'nickname': 'nickname',
        'enabled': 'enabled',
        'notes': 'notes',
        'certificate': 'certificate',
        'sha_thumbprint': 'sha_thumbprint',
        'new_certificate': 'new_certificate',
        'new_sha_thumbprint': 'new_sha_thumbprint',
        'credentials': 'credentials',
        'ipfix_request': 'ipfix_request',
        'ipfix_response': 'ipfix_response',
        'is_vmc': 'is_vmc'
    }

    def __init__(self, entity_id=None, entity_type=None, ip=None, fqdn=None, proxy_id=None, nickname=None, enabled=True, notes=None, certificate=None, sha_thumbprint=None, new_certificate=None, new_sha_thumbprint=None, credentials=None, ipfix_request=None, ipfix_response=None, is_vmc=False):
        """
        VCenterDataSource - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
        self._ip = None
        self._fqdn = None
        self._proxy_id = None
        self._nickname = None
        self._enabled = None
        self._notes = None
        self._certificate = None
        self._sha_thumbprint = None
        self._new_certificate = None
        self._new_sha_thumbprint = None
        self._credentials = None
        self._ipfix_request = None
        self._ipfix_response = None
        self._is_vmc = None

        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if ip is not None:
          self.ip = ip
        if fqdn is not None:
          self.fqdn = fqdn
        if proxy_id is not None:
          self.proxy_id = proxy_id
        if nickname is not None:
          self.nickname = nickname
        if enabled is not None:
          self.enabled = enabled
        if notes is not None:
          self.notes = notes
        if certificate is not None:
          self.certificate = certificate
        if sha_thumbprint is not None:
          self.sha_thumbprint = sha_thumbprint
        if new_certificate is not None:
          self.new_certificate = new_certificate
        if new_sha_thumbprint is not None:
          self.new_sha_thumbprint = new_sha_thumbprint
        if credentials is not None:
          self.credentials = credentials
        if ipfix_request is not None:
          self.ipfix_request = ipfix_request
        if ipfix_response is not None:
          self.ipfix_response = ipfix_response
        if is_vmc is not None:
          self.is_vmc = is_vmc

    @property
    def entity_id(self):
        """
        Gets the entity_id of this VCenterDataSource.
        Internal ID of data source, to be used in subsequent API calls

        :return: The entity_id of this VCenterDataSource.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this VCenterDataSource.
        Internal ID of data source, to be used in subsequent API calls

        :param entity_id: The entity_id of this VCenterDataSource.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this VCenterDataSource.

        :return: The entity_type of this VCenterDataSource.
        :rtype: DataSourceType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this VCenterDataSource.

        :param entity_type: The entity_type of this VCenterDataSource.
        :type: DataSourceType
        """

        self._entity_type = entity_type

    @property
    def ip(self):
        """
        Gets the ip of this VCenterDataSource.
        IP address of data source (use either IP or FQDN, not both)

        :return: The ip of this VCenterDataSource.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this VCenterDataSource.
        IP address of data source (use either IP or FQDN, not both)

        :param ip: The ip of this VCenterDataSource.
        :type: str
        """

        self._ip = ip

    @property
    def fqdn(self):
        """
        Gets the fqdn of this VCenterDataSource.
        Hostname of data source (use either IP or FQDN, not both)

        :return: The fqdn of this VCenterDataSource.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this VCenterDataSource.
        Hostname of data source (use either IP or FQDN, not both)

        :param fqdn: The fqdn of this VCenterDataSource.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def proxy_id(self):
        """
        Gets the proxy_id of this VCenterDataSource.
        ID of Collector VM which should register this vcenter

        :return: The proxy_id of this VCenterDataSource.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """
        Sets the proxy_id of this VCenterDataSource.
        ID of Collector VM which should register this vcenter

        :param proxy_id: The proxy_id of this VCenterDataSource.
        :type: str
        """

        self._proxy_id = proxy_id

    @property
    def nickname(self):
        """
        Gets the nickname of this VCenterDataSource.
        A friendly nickname for the data source

        :return: The nickname of this VCenterDataSource.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this VCenterDataSource.
        A friendly nickname for the data source

        :param nickname: The nickname of this VCenterDataSource.
        :type: str
        """

        self._nickname = nickname

    @property
    def enabled(self):
        """
        Gets the enabled of this VCenterDataSource.
        Whether or not data collection is enabled

        :return: The enabled of this VCenterDataSource.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this VCenterDataSource.
        Whether or not data collection is enabled

        :param enabled: The enabled of this VCenterDataSource.
        :type: bool
        """

        self._enabled = enabled

    @property
    def notes(self):
        """
        Gets the notes of this VCenterDataSource.
        Room for notes or comments about the data source

        :return: The notes of this VCenterDataSource.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this VCenterDataSource.
        Room for notes or comments about the data source

        :param notes: The notes of this VCenterDataSource.
        :type: str
        """

        self._notes = notes

    @property
    def certificate(self):
        """
        Gets the certificate of this VCenterDataSource.
        Certificate of data source

        :return: The certificate of this VCenterDataSource.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this VCenterDataSource.
        Certificate of data source

        :param certificate: The certificate of this VCenterDataSource.
        :type: str
        """

        self._certificate = certificate

    @property
    def sha_thumbprint(self):
        """
        Gets the sha_thumbprint of this VCenterDataSource.
        SHA thumbprint of data source

        :return: The sha_thumbprint of this VCenterDataSource.
        :rtype: str
        """
        return self._sha_thumbprint

    @sha_thumbprint.setter
    def sha_thumbprint(self, sha_thumbprint):
        """
        Sets the sha_thumbprint of this VCenterDataSource.
        SHA thumbprint of data source

        :param sha_thumbprint: The sha_thumbprint of this VCenterDataSource.
        :type: str
        """

        self._sha_thumbprint = sha_thumbprint

    @property
    def new_certificate(self):
        """
        Gets the new_certificate of this VCenterDataSource.
        New certificate of data source

        :return: The new_certificate of this VCenterDataSource.
        :rtype: str
        """
        return self._new_certificate

    @new_certificate.setter
    def new_certificate(self, new_certificate):
        """
        Sets the new_certificate of this VCenterDataSource.
        New certificate of data source

        :param new_certificate: The new_certificate of this VCenterDataSource.
        :type: str
        """

        self._new_certificate = new_certificate

    @property
    def new_sha_thumbprint(self):
        """
        Gets the new_sha_thumbprint of this VCenterDataSource.
        New SHA thumbprint of data source

        :return: The new_sha_thumbprint of this VCenterDataSource.
        :rtype: str
        """
        return self._new_sha_thumbprint

    @new_sha_thumbprint.setter
    def new_sha_thumbprint(self, new_sha_thumbprint):
        """
        Sets the new_sha_thumbprint of this VCenterDataSource.
        New SHA thumbprint of data source

        :param new_sha_thumbprint: The new_sha_thumbprint of this VCenterDataSource.
        :type: str
        """

        self._new_sha_thumbprint = new_sha_thumbprint

    @property
    def credentials(self):
        """
        Gets the credentials of this VCenterDataSource.

        :return: The credentials of this VCenterDataSource.
        :rtype: PasswordCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this VCenterDataSource.

        :param credentials: The credentials of this VCenterDataSource.
        :type: PasswordCredentials
        """

        self._credentials = credentials

    @property
    def ipfix_request(self):
        """
        Gets the ipfix_request of this VCenterDataSource.

        :return: The ipfix_request of this VCenterDataSource.
        :rtype: DvsIpfixRequest
        """
        return self._ipfix_request

    @ipfix_request.setter
    def ipfix_request(self, ipfix_request):
        """
        Sets the ipfix_request of this VCenterDataSource.

        :param ipfix_request: The ipfix_request of this VCenterDataSource.
        :type: DvsIpfixRequest
        """

        self._ipfix_request = ipfix_request

    @property
    def ipfix_response(self):
        """
        Gets the ipfix_response of this VCenterDataSource.

        :return: The ipfix_response of this VCenterDataSource.
        :rtype: DvsIpfixResponse
        """
        return self._ipfix_response

    @ipfix_response.setter
    def ipfix_response(self, ipfix_response):
        """
        Sets the ipfix_response of this VCenterDataSource.

        :param ipfix_response: The ipfix_response of this VCenterDataSource.
        :type: DvsIpfixResponse
        """

        self._ipfix_response = ipfix_response

    @property
    def is_vmc(self):
        """
        Gets the is_vmc of this VCenterDataSource.
        Whether vCenter is a VMware Cloud operated vCenter (true or false).

        :return: The is_vmc of this VCenterDataSource.
        :rtype: bool
        """
        return self._is_vmc

    @is_vmc.setter
    def is_vmc(self, is_vmc):
        """
        Sets the is_vmc of this VCenterDataSource.
        Whether vCenter is a VMware Cloud operated vCenter (true or false).

        :param is_vmc: The is_vmc of this VCenterDataSource.
        :type: bool
        """

        self._is_vmc = is_vmc

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
        if not isinstance(other, VCenterDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
