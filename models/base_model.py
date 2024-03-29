#!/usr/bin/python3
"""The BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args: Unused.
            **kwargs: attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)


    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the  instance.

        """
        r_dict = self.__dict__.copy()
        r_dict["created_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        r_dict["__class__"] = self.__class__.__name__
        return r_dict

    def __str__(self):
        """Return the print/str representation instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)