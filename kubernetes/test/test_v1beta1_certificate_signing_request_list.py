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
from kubernetes.client.models.v1beta1_certificate_signing_request_list import V1beta1CertificateSigningRequestList


class TestV1beta1CertificateSigningRequestList(unittest.TestCase):
    """ V1beta1CertificateSigningRequestList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1CertificateSigningRequestList(self):
        """
        Test V1beta1CertificateSigningRequestList
        """
        model = kubernetes.client.models.v1beta1_certificate_signing_request_list.V1beta1CertificateSigningRequestList()


if __name__ == '__main__':
    unittest.main()
