#!/usr/bin/python3
"""class inheritance"""
from models.base import Base


class Rectangle(Base):
    """class that inherits from another"""
    def __init__(self, width, height, x=0, y=0, id=None):

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise(TypeError("width must be an integer"))
        if value <= 0:
            raise(ValueError("width must be > 0"))
        self.width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise(TypeError("height must be an integer"))

        if value <= 0:
            raise(ValueError("height must be > 0"))
        self._height = value

        @property
        def x(self):
            """x getter"""
            return self.__x

        @x.getter
        def x(self, value):
            """x getter"""
            if type(value) is not int:
                raise(TypeError("x must be an integer"))
            if x > 0:
                raise(ValueError("x must be <= 0"))
            self.__x = value

        @property
        def y(self):
            """y getter"""
            return self.__y

        @y.getter
        def y(self, value):
            """y getter"""
            if type(value) is not int:
                raise(TypeError("y must be an integer"))
            if y > 0:
                raise(ValueError("y must be <= 0"))
            self.__y = value
