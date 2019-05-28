# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.settings_api import SettingsApi


class TestSettingsApi(unittest.TestCase):
    """ SettingsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.settings_api.SettingsApi()

    def tearDown(self):
        pass

    def test_add_ip_tag(self):
        """
        Test case for add_ip_tag

        Tag ip addresses with tag-id
        """
        pass

    def test_add_vidm_user(self):
        """
        Test case for add_vidm_user

        Add a VMware Identity manager user to vRealize Network Insight
        """
        pass

    def test_add_vidm_user_group(self):
        """
        Test case for add_vidm_user_group

        Add a VMware Identity Manager user-group to vRealize Network Insight
        """
        pass

    def test_create_subnet_mapping(self):
        """
        Test case for create_subnet_mapping

        Create subnet mapping
        """
        pass

    def test_delete_subnet_mapping(self):
        """
        Test case for delete_subnet_mapping

        Delete subnet mapping
        """
        pass

    def test_delete_user(self):
        """
        Test case for delete_user

        Delete an existing user.
        """
        pass

    def test_delete_user_group(self):
        """
        Test case for delete_user_group

        Delete an existing user-group
        """
        pass

    def test_delete_vidm_configuration(self):
        """
        Test case for delete_vidm_configuration

        Delete VMware Identity Manager configuration
        """
        pass

    def test_disable_vidm(self):
        """
        Test case for disable_vidm

        Disable VMware Identity Manager integration
        """
        pass

    def test_enable_vidm(self):
        """
        Test case for enable_vidm

        Enable VMware Identity Manager integration
        """
        pass

    def test_get_ip_tag(self):
        """
        Test case for get_ip_tag

        Show ip tag details
        """
        pass

    def test_get_ip_tag_ids(self):
        """
        Test case for get_ip_tag_ids

        Show ip tag ids
        """
        pass

    def test_get_subnet_mappings(self):
        """
        Test case for get_subnet_mappings

        Get all subnet mappings
        """
        pass

    def test_get_user(self):
        """
        Test case for get_user

        Get details of a user
        """
        pass

    def test_get_user_group(self):
        """
        Test case for get_user_group

        Get details of a user-group
        """
        pass

    def test_get_user_groups(self):
        """
        Test case for get_user_groups

        List user-groups
        """
        pass

    def test_get_users(self):
        """
        Test case for get_users

        List the users
        """
        pass

    def test_get_vidm_configuration(self):
        """
        Test case for get_vidm_configuration

        Get configuration details of VMware Identity Manager
        """
        pass

    def test_remove_ip_tag(self):
        """
        Test case for remove_ip_tag

        Remove tag from ip addresses
        """
        pass

    def test_save_vidm_configuration(self):
        """
        Test case for save_vidm_configuration

        Configure VMware Identity Manager
        """
        pass

    def test_update_subnet_mapping(self):
        """
        Test case for update_subnet_mapping

        Update subnet mapping
        """
        pass

    def test_update_vidm_configuration(self):
        """
        Test case for update_vidm_configuration

        Update VMware Identity Manager configuration
        """
        pass

    def test_update_vidm_user_group_role(self):
        """
        Test case for update_vidm_user_group_role

        Update role for user-group mapped through VMware Identity Manager
        """
        pass

    def test_update_vidm_user_role(self):
        """
        Test case for update_vidm_user_role

        Update role for user mapped through VMware Identity Manager
        """
        pass


if __name__ == '__main__':
    unittest.main()