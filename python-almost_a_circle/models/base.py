#!/usr/bin/python3
"""Base class"""
import unittest
from models.rectangle import Rectangle

class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):

        """class constructor
            Args:
                id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    
    def test_to_json_string(self):
        """ Test to_json_string """
        dic = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        json_dic = Base.to_json_string([dic])
        self.assertTrue(isinstance(dic, dict))
        self.assertTrue(isinstance(json_dic, str))
        self.assertCountEqual(
            json_dic, '{["id": 1, "x": 2, "y": 3, "width": 4, "height": 5]}')
        json_d_1 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")
        err = ("to_json_string() missing 1 required positional argument: " +
               "'list_dictionaries'")
        with self.assertRaises(TypeError) as i:
            Base.to_json_string()
        self.assertEqual(err, str(i.exception))
        err = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as i:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(err, str(i.exception))
