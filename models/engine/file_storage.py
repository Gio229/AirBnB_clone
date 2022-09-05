#!/usr/bin/pyhton3
"""
This module define the class FileStorage
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
