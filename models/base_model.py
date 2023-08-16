#!/usr/bin/python3
"""
    class BaseModel that defines all
    common attributes/methods for other
    classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
       class
    """
    def __init__(self, *args, **kwargs):
        """
           initiallizing an object
           args:
                id: string - assign with an uuid
                    when an instance is created.

                created_at: datetime - assign with the current
                datetime when an instance is created

                updated_at: datetime - assign with the current
                datetime when an instance is created and it will
                be updated every time you change your object

        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at':
                        date_format = '%Y-%m-%dT%H:%M:%S.%f'
                        self.created_at = datetime.strptime(value, date_format)
                    elif key == 'updated_at':
                        date_format = '%Y-%m-%dT%H:%M:%S.%f'
                        self.updated_at = datetime.strptime(value, date_format)
                    else:
                        setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """
            __str__: should print: [<class name>] (<self.id>)
            <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
             updates the public instance attribute updated_at
             with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
           returns a dictionary containing all
           keys/values of __dict__ of the instance:
        """
        my_dictonary = {}
        my_dictonary.update(self.__dict__)
        my_dictonary.update({'__class__': self.__class__.__name__})
        my_dictonary['created_at'] = self.created_at.isoformat()
        my_dictonary['updated_at'] = self.updated_at.isoformat()
        return my_dictonary
