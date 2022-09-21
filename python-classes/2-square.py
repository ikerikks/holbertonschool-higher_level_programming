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
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
