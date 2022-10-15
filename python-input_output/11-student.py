#!/usr/bin/python3
"""student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """student class to JSON"""
        if attrs is None:
            return self.__dict__
        dictio = {}
        for i in attrs:
            if i in self.__dict__:
                dictio[i] = self.__dict__[i]
        return dictio

    def reload_from_json(self, json):
        """replaces all attributes"""
        for attrs in json:
            self.__dict__[attrs] = json[attrs]
