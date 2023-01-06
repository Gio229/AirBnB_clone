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

    # path to the JSON file storage
    __file_path = "file.json"
    # dictionary which will contains all created objects
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Add to __objects a new object
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Save objects to json file storage
        """
        try:
            objects_to_store = {}
            for key, value in self.__objects.items():
                objects_to_store[key] = value.to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(objects_to_store, f)
        except:
            return

    def reload(self):
        """Recovered all objects from json file storage
        """
        try:
            with open(self.__file_path, 'r') as f:
                recovered_objects = json.load(f)
                for object in recovered_objects.values():
                    del object["__class__"]
                self.__objects = recovered_objects
        except:
            return
    
    def some(self):
        print ("me void=")
