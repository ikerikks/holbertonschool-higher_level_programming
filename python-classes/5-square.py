#!/usr/bin/python3
"""class that defines a square."""


class Square:
    """Square class. """

    def __init__(self, size=0):
        """defines a square.
        Args:
            size : size of square
        """
        if not isinstance(size, int):
            raise(TypeError("size must be an integer"))
        elif size < 0:
            raise(ValueError("size must be >= 0"))
        else:
            self.__size = int(size)

    def area(self):
        """ defines the area of the square.

        Returns:
            area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """gets the size of the square
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if not isinstance(value, int):
            raise(TypeError("size must be an integer"))
        elif value < 0:
            raise(ValueError("size must be >= 0"))
        else:
            self.__size = int(value)

    def my_print(self):
        if self.__size == 0:
            print("")

        for i in range(self.__size):
            for i in range(1, self.__size):
                print("#", end="")
            print("#")
