# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 6.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VidmCertificate(object):
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
        'vidm_root_certificate': 'str'
    }

    attribute_map = {
        'vidm_root_certificate': 'vidm_root_certificate'
    }

    def __init__(self, vidm_root_certificate=None):
        """
        VidmCertificate - a model defined in Swagger
        """

        self._vidm_root_certificate = None

        if vidm_root_certificate is not None:
          self.vidm_root_certificate = vidm_root_certificate

    @property
    def vidm_root_certificate(self):
        """
        Gets the vidm_root_certificate of this VidmCertificate.
        Root certificate of the VIDM server

        :return: The vidm_root_certificate of this VidmCertificate.
        :rtype: str
        """
        return self._vidm_root_certificate

    @vidm_root_certificate.setter
    def vidm_root_certificate(self, vidm_root_certificate):
        """
        Sets the vidm_root_certificate of this VidmCertificate.
        Root certificate of the VIDM server

        :param vidm_root_certificate: The vidm_root_certificate of this VidmCertificate.
        :type: str
        """

        self._vidm_root_certificate = vidm_root_certificate

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
        if not isinstance(other, VidmCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
