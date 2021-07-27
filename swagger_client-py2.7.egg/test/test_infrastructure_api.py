# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.infrastructure_api import InfrastructureApi


class TestInfrastructureApi(unittest.TestCase):
    """ InfrastructureApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.infrastructure_api.InfrastructureApi()

    def tearDown(self):
        pass

    def test_delete_vcf_watermark(self):
        """
        Test case for delete_vcf_watermark

        Delete VMware Cloud Foundation (VCF) watermark
        """
        pass

    def test_get_node(self):
        """
        Test case for get_node

        Show node details
        """
        pass

    def test_get_vcf_watermark(self):
        """
        Test case for get_vcf_watermark

        Get VCF Watermark details
        """
        pass

    def test_list_nodes(self):
        """
        Test case for list_nodes

        List nodes
        """
        pass

    def test_save_vcf_watermark(self):
        """
        Test case for save_vcf_watermark

        Configure VMware Cloud Foundation (VCF) watermark
        """
        pass

    def test_update_vcf_watermark(self):
        """
        Test case for update_vcf_watermark

        Update VMware Cloud Foundation (VCF) watermark
        """
        pass


if __name__ == '__main__':
    unittest.main()
