#!/usr/bin/python3
"""read_file dunction"""


def read_file(filename=""):
    """reads a text file"""
    with open(filename) as file:
        print(file.read(), end='')
