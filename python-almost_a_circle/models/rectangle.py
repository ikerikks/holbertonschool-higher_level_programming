#!/usr/bin/python3
"""class inheritance"""
import Base


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
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise(TypeError("width must be an integer"))
        if value <= 0:
            raise(ValueError("width must be > 0"))
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise(TypeError("height must be an integer"))

        if value <= 0:
            raise(ValueError("height must be > 0"))
        self.__height = value

        @property
        def x(self):
            """getter of x"""
            return self.__x

        @x.setter
        def x(self, value):
            """setter of x"""
            if type(value) is not int:
                raise(TypeError("x must be an integer"))
            if value < 0:
                raise(ValueError("x must be <= 0"))
            self.__x = value

        @property
        def y(self):
            """getter of y"""
            return self.__y

        @y.setter
        def y(self, value):
            """setter of y"""
            if type(value) is not int:
                raise(TypeError("y must be an integer"))
            if value < 0:
                raise(ValueError("y must be <= 0"))
            self.__y = value
