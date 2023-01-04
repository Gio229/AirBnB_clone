#!/usr/bin/python3
"""
This module define the class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    This class defines all common
    attributes/methods for other classes
    """
    date_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self):
        """Constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Give the string representation of the object
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save the instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the instance as dictionary
        """
        dict_repr = self.__dict__
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = dict_repr["created_at"].strftime(
            self.date_format)
        dict_repr["updated_at"] = dict_repr["updated_at"].strftime(
            self.date_format)

        return dict_repr


if __name__ == "__main__":
    bb = BaseModel()
    print(bb)
    print(bb.to_dict())
