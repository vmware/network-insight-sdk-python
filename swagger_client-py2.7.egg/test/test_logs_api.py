# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""




import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.logs_api import LogsApi


class TestLogsApi(unittest.TestCase):
    """ LogsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.logs_api.LogsApi()

    def tearDown(self):
        pass

    def test_get_audit_logs(self):
        """
        Test case for get_audit_logs

        Get Audit logs
        """
        pass


if __name__ == '__main__':
    unittest.main()
