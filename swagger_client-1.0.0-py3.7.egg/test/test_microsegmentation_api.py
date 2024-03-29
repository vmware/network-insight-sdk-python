# coding: utf-8

"""
    VMware Aria Operations for Networks API Reference

    Operations for Networks API Reference

    OpenAPI spec version: 6.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.microsegmentation_api import MicrosegmentationApi


class TestMicrosegmentationApi(unittest.TestCase):
    """ MicrosegmentationApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.microsegmentation_api.MicrosegmentationApi()

    def tearDown(self):
        pass

    def test_export_nsx_recommended_rules(self):
        """
        Test case for export_nsx_recommended_rules

        Export recommended firewall rules for NSX-v
        """
        pass

    def test_get_connection_graph(self):
        """
        Test case for get_connection_graph

        Get communication graph for requested entity type
        """
        pass

    def test_get_entity_communication_summary(self):
        """
        Test case for get_entity_communication_summary

        Get communication summary for requested entity
        """
        pass

    def test_list_recommended_rules(self):
        """
        Test case for list_recommended_rules

        Get logical recommended firewall rules
        """
        pass


if __name__ == '__main__':
    unittest.main()
