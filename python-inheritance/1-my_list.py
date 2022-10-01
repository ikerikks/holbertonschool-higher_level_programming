#!/usr/bin/python3


class MyList(list):
    """class inheriting from list"""
    def print_sorted(self):
        """prints a list"""
        print(sorted(self))
