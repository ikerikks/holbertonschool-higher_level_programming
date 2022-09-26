#!/usr/bin/python3


import re


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except:
        return False
    else:
        return True
