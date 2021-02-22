# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WebProxyRequest(object):
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
        'nick_name': 'str',
        'target_ip': 'str',
        'target_port': 'int',
        'proxy_type': 'str',
        'auth_type': 'str',
        'use_credentials': 'bool',
        'user_name': 'str',
        'password': 'str'
    }

    attribute_map = {
        'nick_name': 'nick_name',
        'target_ip': 'target_ip',
        'target_port': 'target_port',
        'proxy_type': 'proxy_type',
        'auth_type': 'auth_type',
        'use_credentials': 'use_credentials',
        'user_name': 'user_name',
        'password': 'password'
    }

    def __init__(self, nick_name=None, target_ip=None, target_port=None, proxy_type=None, auth_type=None, use_credentials=None, user_name=None, password=None):
        """
        WebProxyRequest - a model defined in Swagger
        """

        self._nick_name = None
        self._target_ip = None
        self._target_port = None
        self._proxy_type = None
        self._auth_type = None
        self._use_credentials = None
        self._user_name = None
        self._password = None

        if nick_name is not None:
          self.nick_name = nick_name
        if target_ip is not None:
          self.target_ip = target_ip
        if target_port is not None:
          self.target_port = target_port
        if proxy_type is not None:
          self.proxy_type = proxy_type
        if auth_type is not None:
          self.auth_type = auth_type
        if use_credentials is not None:
          self.use_credentials = use_credentials
        if user_name is not None:
          self.user_name = user_name
        if password is not None:
          self.password = password

    @property
    def nick_name(self):
        """
        Gets the nick_name of this WebProxyRequest.
        Descriptor or identifier for particular web proxy. It should be unique

        :return: The nick_name of this WebProxyRequest.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """
        Sets the nick_name of this WebProxyRequest.
        Descriptor or identifier for particular web proxy. It should be unique

        :param nick_name: The nick_name of this WebProxyRequest.
        :type: str
        """

        self._nick_name = nick_name

    @property
    def target_ip(self):
        """
        Gets the target_ip of this WebProxyRequest.
        IP address of web Proxy server

        :return: The target_ip of this WebProxyRequest.
        :rtype: str
        """
        return self._target_ip

    @target_ip.setter
    def target_ip(self, target_ip):
        """
        Sets the target_ip of this WebProxyRequest.
        IP address of web Proxy server

        :param target_ip: The target_ip of this WebProxyRequest.
        :type: str
        """

        self._target_ip = target_ip

    @property
    def target_port(self):
        """
        Gets the target_port of this WebProxyRequest.
        Port number of web Proxy server

        :return: The target_port of this WebProxyRequest.
        :rtype: int
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        """
        Sets the target_port of this WebProxyRequest.
        Port number of web Proxy server

        :param target_port: The target_port of this WebProxyRequest.
        :type: int
        """

        self._target_port = target_port

    @property
    def proxy_type(self):
        """
        Gets the proxy_type of this WebProxyRequest.
        Type of web Proxy being configured. [Permitted Values - HTTP/HTTPS]

        :return: The proxy_type of this WebProxyRequest.
        :rtype: str
        """
        return self._proxy_type

    @proxy_type.setter
    def proxy_type(self, proxy_type):
        """
        Sets the proxy_type of this WebProxyRequest.
        Type of web Proxy being configured. [Permitted Values - HTTP/HTTPS]

        :param proxy_type: The proxy_type of this WebProxyRequest.
        :type: str
        """

        self._proxy_type = proxy_type

    @property
    def auth_type(self):
        """
        Gets the auth_type of this WebProxyRequest.
        Type of authentication. [Permitted Values - Basic/NTLM]

        :return: The auth_type of this WebProxyRequest.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """
        Sets the auth_type of this WebProxyRequest.
        Type of authentication. [Permitted Values - Basic/NTLM]

        :param auth_type: The auth_type of this WebProxyRequest.
        :type: str
        """

        self._auth_type = auth_type

    @property
    def use_credentials(self):
        """
        Gets the use_credentials of this WebProxyRequest.
        Credentials required for this web proxy

        :return: The use_credentials of this WebProxyRequest.
        :rtype: bool
        """
        return self._use_credentials

    @use_credentials.setter
    def use_credentials(self, use_credentials):
        """
        Sets the use_credentials of this WebProxyRequest.
        Credentials required for this web proxy

        :param use_credentials: The use_credentials of this WebProxyRequest.
        :type: bool
        """

        self._use_credentials = use_credentials

    @property
    def user_name(self):
        """
        Gets the user_name of this WebProxyRequest.
        Username for web proxy authentication

        :return: The user_name of this WebProxyRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this WebProxyRequest.
        Username for web proxy authentication

        :param user_name: The user_name of this WebProxyRequest.
        :type: str
        """

        self._user_name = user_name

    @property
    def password(self):
        """
        Gets the password of this WebProxyRequest.
        Password for web proxy authentication

        :return: The password of this WebProxyRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this WebProxyRequest.
        Password for web proxy authentication

        :param password: The password of this WebProxyRequest.
        :type: str
        """

        self._password = password

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
        if not isinstance(other, WebProxyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
