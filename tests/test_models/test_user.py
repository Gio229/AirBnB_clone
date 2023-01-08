#!/usr/bin/python3
"""
This module define the Place
"""
import unittest
from datetime import datetime

from models.user import User


class TestUser(unittest.TestCase):
    """
    This class define all tests for User
    """

    def test_instantiation(self):
        """Test if new instance have the right type
        """
        user = User()
        self.assertEqual(User, type(user))
        self.assertTrue(type(user.id) is str)
        self.assertTrue(type(user.created_at) is datetime)
        self.assertTrue(type(user.updated_at) is datetime)

    def test_email(self):
        """Test if email attribute is string
        """
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """Test if password attribute is string
        """
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        """Test if first_name attribute is string
        """
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        """Test if last_name attribute is string
        """
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()
