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
from swagger_client.apis.migration_api import MigrationApi


class TestMigrationApi(unittest.TestCase):
    """ MigrationApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.migration_api.MigrationApi()

    def tearDown(self):
        pass

    def test_disable_migration_wave(self):
        """
        Test case for disable_migration_wave

        Disable migration wave computation.
        """
        pass

    def test_enable_migration_wave(self):
        """
        Test case for enable_migration_wave

        Enable migration wave computation.
        """
        pass

    def test_get_migration_wave(self):
        """
        Test case for get_migration_wave

        Get migration waves.
        """
        pass


if __name__ == '__main__':
    unittest.main()