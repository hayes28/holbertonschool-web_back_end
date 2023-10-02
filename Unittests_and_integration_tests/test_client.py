#!/usr/bin/env python3
"""Test fixtures
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient Class"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test that GithubOrgClient.org returns the correct value """
        mock_get_json.return_value = True
        test_class = GithubOrgClient(org_name)
        self.assertEqual(test_class.org, True)
        mock_get_json.assert_called_once()

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json):
        """ Test that the result of _public_repos_url is the expected one """
        mock_get_json.return_value = {'repos_url': 'test/repos_url'}
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class._public_repos_url,
                         "test/repos_url")
        mock_get_json.assert_called_once()
