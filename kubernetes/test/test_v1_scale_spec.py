# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_scale_spec import V1ScaleSpec


class TestV1ScaleSpec(unittest.TestCase):
    """ V1ScaleSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ScaleSpec(self):
        """
        Test V1ScaleSpec
        """
        model = kubernetes.client.models.v1_scale_spec.V1ScaleSpec()


if __name__ == '__main__':
    unittest.main()
