#!/usr/bin/python3
""" Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "Square class"
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """method must be implemented an area"""
        return self.__size ** 2

    def __str__(self):
        """Method that prints string"""
        return f"[Square] {self.__size}/{self.__size}"
