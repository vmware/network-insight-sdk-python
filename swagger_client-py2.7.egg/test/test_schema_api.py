# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.schema_api import SchemaApi


class TestSchemaApi(unittest.TestCase):
    """ SchemaApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.schema_api.SchemaApi()

    def tearDown(self):
        pass

    def test_bulk_fetch_event_meta_info(self):
        """
        Test case for bulk_fetch_event_meta_info

        Get Event meta Information
        """
        pass

    def test_get_metrics_schema(self):
        """
        Test case for get_metrics_schema

        Get metrics schema for an entity type
        """
        pass


if __name__ == '__main__':
    unittest.main()
