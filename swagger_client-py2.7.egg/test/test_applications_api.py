# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.applications_api import ApplicationsApi


class TestApplicationsApi(unittest.TestCase):
    """ ApplicationsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.applications_api.ApplicationsApi()

    def tearDown(self):
        pass

    def test_add_application(self):
        """
        Test case for add_application

        Create an application
        """
        pass

    def test_add_tier(self):
        """
        Test case for add_tier

        Create tier in application
        """
        pass

    def test_delete_application(self):
        """
        Test case for delete_application

        Delete an application
        """
        pass

    def test_delete_tier(self):
        """
        Test case for delete_tier

        Delete tier
        """
        pass

    def test_get_application(self):
        """
        Test case for get_application

        Show application details
        """
        pass

    def test_get_application_members(self):
        """
        Test case for get_application_members

        Show application members
        """
        pass

    def test_get_application_tier(self):
        """
        Test case for get_application_tier

        Show tier details
        """
        pass

    def test_get_tier(self):
        """
        Test case for get_tier

        Show tier details
        """
        pass

    def test_list_application_tiers(self):
        """
        Test case for list_application_tiers

        List tiers of an application
        """
        pass

    def test_list_applications(self):
        """
        Test case for list_applications

        List applications
        """
        pass

    def test_list_applications_details(self):
        """
        Test case for list_applications_details

        Get application details bulk
        """
        pass


if __name__ == '__main__':
    unittest.main()
