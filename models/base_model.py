#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        """
        self.id = str(uuid.uuid4())  # Generate a unique ID
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
```

Explanation:
- The `BaseModel` class initializes an instance with a unique ID, creation timestamp (`created_at`), and update timestamp (`updated_at`).
- The `__str__` method provides a formatted string representation.
- The `save` method updates the `updated_at` attribute.
- The `to_dict` method returns a dictionary representation of the instance, including class name and ISO-formatted timestamps.

Feel free to extend this base class for other specific models! 🚀
