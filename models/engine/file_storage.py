#!/usr/bin/python3
""" File Storage to serialize instances to JSON file
and deserialize JSON file to instances
"""
import json
import os.path
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review


class FileStorage:
    """ FileStorage class to serializes and deserialize
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ Sets object with key and value
        """
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """ Serializes __objects to the JSON file
        """
        dic1 = {}
        new_dic = {}
        for k, v in self.__objects.items():
            new_dic[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            string = json.dumps(new_dic)
            f.write(string)

    def reload(self):
        """ Deserializes the JSON to __objects.
        """
        class_dict = {'BaseModel': BaseModel, 'User': User, 'State': State,
                      'Amenity': Amenity, 'Place': Place, 'City': City,
                      'Review': Review}
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                string = f.read()
                if string != "":
                    dic = (json.loads(string))
                    for key, value in dic.items():
                        self.__objects[key] =\
                            class_dict[value['__class__']](**value)
