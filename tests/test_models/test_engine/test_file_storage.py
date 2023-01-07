

#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""
import unittest
import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorageDocs(unittest.TestCase):
    """
    This class define all tests for FileStorage
    """

    def test_instantiation(self):
        """Test if new instance have the good type
        """
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_all(self):
        """Test if all method work well"""
        storage = FileStorage()
        objects = storage.all()
        self.assertEqual(type(objects), dict)

    def test_reload(self):
        storage = FileStorage()
        baseModel = BaseModel()
        storage.new(baseModel)
        storage.save()
        storage.reload()
        self.assertIn("BaseModel." + baseModel.id,
                      storage.all())
    
    def test_new(self):
        storage = FileStorage()
        baseModel = BaseModel()
        storage.new(baseModel)
        self.assertIn("BaseModel." + baseModel.id,
                      storage.all())

    def test_save(self):
        storage = FileStorage()
        baseModel = BaseModel()
        storage.new(baseModel)
        storage.save()
        with open("file.json", "r") as f:
            recovered_objects = json.load(f)
            self.assertIn("BaseModel." + baseModel.id, recovered_objects)


if __name__ == "__main__":
    unittest.main()
