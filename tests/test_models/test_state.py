#!/usr/bin/python3
"""
This module define the State tests
"""
from datetime import datetime
import unittest

from models.state import State


class TestState(unittest.TestCase):
    """
    This class define all tests for State
    """

    def test_instantiation(self):
        state = State()
        self.assertEqual(State, type(state))
        self.assertTrue(type(state.id) is str)
        self.assertTrue(type(state.created_at) is datetime)
        self.assertTrue(type(state.updated_at) is datetime)

    def test_name(self):
        """Test if name attribute is string
        """
        self.assertEqual(str, type(State.name))

if __name__ == "__main__":
    unittest.main()
