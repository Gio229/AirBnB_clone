

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
        self.assertEqual(FileStorage, type(FileStorage()))


if __name__ == "__main__":
    unittest.main()
