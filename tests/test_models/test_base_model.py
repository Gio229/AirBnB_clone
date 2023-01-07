#!/usr/bin/python3
"""
This module define the TestBaseModel
"""
import unittest
import json

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    This class define all tests for BaseModel
    """

    def test_instantiation(self):
        """Test if instance have the right type
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_constructor(self):
        """Test if constructor work well
        """
        obj1 = BaseModel()
        dict_obj1 = obj1.to_dict()
        obj2 = BaseModel(**dict_obj1)
        self.assertEqual(obj1.id, obj2.id)
        self.assertEqual(obj1.created_at, obj2.created_at)
        self.assertEqual(obj1.updated_at, obj2.updated_at)

    def test_save(self):
        """Test if instance is correctly saved
        """
        baseModel = BaseModel()
        old_updated_at = baseModel.updated_at
        baseModel.save()
        new_updated_at = baseModel.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

        with open("file.json", "r") as f:
            recovered_objects_json = json.load(f)
            self.assertIn("BaseModel." + baseModel.id, recovered_objects_json)



if __name__ == "__main__":
    unittest.main()
