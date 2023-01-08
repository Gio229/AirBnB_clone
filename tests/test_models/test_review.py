#!/usr/bin/python3
"""
This module define the Place
"""
from datetime import datetime
import unittest

from models.review import Review


class TestReview(unittest.TestCase):
    """
    This class define all tests for Review
    """

    def test_instantiation(self):
        review = Review()
        self.assertEqual(Review, type(review))
        self.assertTrue(type(review.id) is str)
        self.assertTrue(type(review.created_at) is datetime)
        self.assertTrue(type(review.updated_at) is datetime)

    def test_place_id(self):
        """Test if place_id attribute is string
        """
        self.assertEqual(str, type(Review.place_id))
    
    def test_user_id(self):
        """Test if user_id attribute is string
        """
        self.assertEqual(str, type(Review.user_id))
    
    def test_text(self):
        """Test if text attribute is string
        """
        self.assertEqual(str, type(Review.text))

if __name__ == "__main__":
    unittest.main()
