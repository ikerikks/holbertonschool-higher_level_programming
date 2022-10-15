#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """class rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes new rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width of ractangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of ractangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rectangle area"""
        return (self.__width * self.height)

    def perimeter(self):
        """rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """representation of the Rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += '#'
                if i != self.__height - 1:
                    string += '\n'
            return string

    def __repr__(self):
        """string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """object is being delete"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
