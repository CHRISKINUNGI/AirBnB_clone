#!/usr/bin/python3
"""
   class FileStorage
   serializes instances to a JSON file and deserializes
   JSON file to instances
"""
import json
import os
classes = {}


class FileStorage:
    """
       class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            adds a new object to __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
           serializes __objects to the JSON file.
        """
        serialized_data = {key: obj.to_dict() for key,
                           obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_data, file)

    def reload(self):
        """
            deserializes the JSON file and populates __objects
            with instances
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    module_name = "models.base_model"
                    module = __import__(module_name, fromlist=[class_name])
                    obj_cls = getattr(module, class_name)
                    instance = obj_cls(**value)
                    self.__objects[key] = instance
