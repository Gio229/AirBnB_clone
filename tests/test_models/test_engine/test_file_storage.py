

#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""
import unittest

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
        objects_from_storage = storage.all()
        self.assertEqual(type(objects_from_storage), dict)

if __name__ == "__main__":
    unittest.main()
