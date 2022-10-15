#!/usr/bin/python3
"""save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """save object in json file
        Args:
            my_obj: Object
            filename: file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
