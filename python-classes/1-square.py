#!/usr/bin/python3
"""empty class that defines a square."""


from ctypes import sizeof


class Square:
    """Square class. """

    def __init__(self, size):
        """defines a square.
        Args:
            size : size of square
        Returns:
            None
        """
        self.__size = size
