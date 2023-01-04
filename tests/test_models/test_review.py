#!/usr/bin/python3
"""
This module define the Place
"""
import unittest

from ...models.review import Review


class TestReview(unittest.TestCase):
    """
    This class define all tests for Review
    """

    def test_instantiation(self):
        self.assertEqual(Review, type(Review()))


if __name__ == "__main__":
    unittest.main()
