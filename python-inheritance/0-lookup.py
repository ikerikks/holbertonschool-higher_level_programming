#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """gets list of available attributes and methods
    Args:
        obj: object
    Returns:
        list
    """
    return dir(obj)
