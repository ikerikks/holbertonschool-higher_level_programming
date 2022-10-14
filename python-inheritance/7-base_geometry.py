#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """empty class"""
    def area(self):
        raise(Exception("area() is not implemented"))

    def integer_validator(self, name, value):
        if type(name) is not value:
            raise(TypeError("{} must be an integer".format(name)))
        if value <= 0:
            raise(ValueError("{} must be greater than 0".format(name)))
