#!/usr/bin/python3
"""class that defines a square."""


class Square:
    """Square class. """

    def __init__(self, size=0, position=(0, 0)):
        """defines a square.
        Args:
            size : size of square
        """
        self.__size = int(size)
        self.__position = position

        if not isinstance(size, int):
            raise(TypeError("size must be an integer"))
        elif size < 0:
            raise(ValueError("size must be >= 0"))

        if type(position) is not tuple or len(position) != 2 or \
            type(position[0]) is not int or position[0] < 0 or \
                type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ defines the area of the square.

        Returns:
            area of the square
        """
        return self.__size ** 2

    """PRIVATE INSTANCE SIZE"""
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

    """PRIVATE INSTANCE POSITION"""
    @property
    def position(self):
        """sets position value od square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2\
            or not isinstance(value[0], int) or not isinstance(value[1], int)\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print("")

        for i in range(self.position[1]):
            print("")
        for j in range(1, self.__size):
            for k in range(self.position[0]):
                print(" ", end="")
            for l in range(1, self.__size):
                print("#", end="")
            print("")
