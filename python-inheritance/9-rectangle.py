#!/usr/bin/python3
""" Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "BaseGeometry class"
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Method print string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
