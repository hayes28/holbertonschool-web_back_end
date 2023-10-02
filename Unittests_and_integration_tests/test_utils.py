#!/usr/bin/env python3
""" Unittests and Integration Tests project """

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap Class """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access nested map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test access nested map exception """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """ TestGetJson Class """

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test get json """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.return_value.json.assert_called_once()

class TestMemoize(unittest.TestCase):
    """ TestMemoize Class """

    def test_memoize(self):
        """ Test memoize """
        class TestClass:
            """ TestClass Class """
            def a_method(self):
                """ a_method method """
                return 42

            @memoize
            def a_property(self):
                """ a_property method """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test = TestClass()
            test.a_property
            test.a_property
            mock_method.assert_called_once()
