#!/usr/bin/python3
"""
This module define the TestBaseModel
"""
import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    This class define all tests for BaseModel
    """

    def test_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))


if __name__ == "__main__":
    unittest.main()
