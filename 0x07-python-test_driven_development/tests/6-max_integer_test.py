#!/bin/usr/python3
"""Unittest for max_integer([..])
pass
pass
pass
"""

import unittest

max_integer = __import__("6-max-integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_maxInt(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEquals(max_integer([1, 3, 4, 2]), 4)
