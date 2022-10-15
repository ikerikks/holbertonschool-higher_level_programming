#!/usr/bin/python3
"""student class"""


class Student:
    """student Class"""

    def __init__(self, first_name, last_name, age):
        """student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """student class to JSON"""
        return self.__dict__
