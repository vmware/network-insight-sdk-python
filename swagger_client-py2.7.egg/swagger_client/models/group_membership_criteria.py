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


class GroupMembershipCriteria(object):
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
        'membership_type': 'str',
        'ip_address_membership_criteria': 'IpAddressMembershipCriteria',
        'search_membership_criteria': 'SearchMembershipCriteria'
    }

    attribute_map = {
        'membership_type': 'membership_type',
        'ip_address_membership_criteria': 'ip_address_membership_criteria',
        'search_membership_criteria': 'search_membership_criteria'
    }

    def __init__(self, membership_type=None, ip_address_membership_criteria=None, search_membership_criteria=None):
        """
        GroupMembershipCriteria - a model defined in Swagger
        """

        self._membership_type = None
        self._ip_address_membership_criteria = None
        self._search_membership_criteria = None

        if membership_type is not None:
          self.membership_type = membership_type
        if ip_address_membership_criteria is not None:
          self.ip_address_membership_criteria = ip_address_membership_criteria
        if search_membership_criteria is not None:
          self.search_membership_criteria = search_membership_criteria

    @property
    def membership_type(self):
        """
        Gets the membership_type of this GroupMembershipCriteria.

        :return: The membership_type of this GroupMembershipCriteria.
        :rtype: str
        """
        return self._membership_type

    @membership_type.setter
    def membership_type(self, membership_type):
        """
        Sets the membership_type of this GroupMembershipCriteria.

        :param membership_type: The membership_type of this GroupMembershipCriteria.
        :type: str
        """
        allowed_values = ["SearchMembershipCriteria", "IPAddressMembershipCriteria"]
        if membership_type not in allowed_values:
            raise ValueError(
                "Invalid value for `membership_type` ({0}), must be one of {1}"
                .format(membership_type, allowed_values)
            )

        self._membership_type = membership_type

    @property
    def ip_address_membership_criteria(self):
        """
        Gets the ip_address_membership_criteria of this GroupMembershipCriteria.

        :return: The ip_address_membership_criteria of this GroupMembershipCriteria.
        :rtype: IpAddressMembershipCriteria
        """
        return self._ip_address_membership_criteria

    @ip_address_membership_criteria.setter
    def ip_address_membership_criteria(self, ip_address_membership_criteria):
        """
        Sets the ip_address_membership_criteria of this GroupMembershipCriteria.

        :param ip_address_membership_criteria: The ip_address_membership_criteria of this GroupMembershipCriteria.
        :type: IpAddressMembershipCriteria
        """

        self._ip_address_membership_criteria = ip_address_membership_criteria

    @property
    def search_membership_criteria(self):
        """
        Gets the search_membership_criteria of this GroupMembershipCriteria.

        :return: The search_membership_criteria of this GroupMembershipCriteria.
        :rtype: SearchMembershipCriteria
        """
        return self._search_membership_criteria

    @search_membership_criteria.setter
    def search_membership_criteria(self, search_membership_criteria):
        """
        Sets the search_membership_criteria of this GroupMembershipCriteria.

        :param search_membership_criteria: The search_membership_criteria of this GroupMembershipCriteria.
        :type: SearchMembershipCriteria
        """

        self._search_membership_criteria = search_membership_criteria

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
        if not isinstance(other, GroupMembershipCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
