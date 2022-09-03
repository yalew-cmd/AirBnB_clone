#!/usr/bin/python3
"""Module defines City class."""
from models import storage
from datetime import datetime
from models.base_model import BaseModel


class City(BaseModel):
    """User class to create user instances."""

    state_id = ""
    name = ""
    def __init__(self, *_, **kwargs):
        """Initialize User instances.

        Args:
            self (object): <class '__main__.User'> type object.

        Returns:
            None
        """
        if not kwargs:
            super().__init__(self)
        else:
            super().__init__(self, **kwargs)
        return None

    def save(self):
        """Override `BaseModel` save method.

        Args:
            self (object): <class '__main__.User'> type object.

        Returns:
            None
        """
        self.updated_at = datetime.now()
        self.__dict__["__class__"] = self.__class__.__name__
        storage.new(self)
        storage.save()
    pass
