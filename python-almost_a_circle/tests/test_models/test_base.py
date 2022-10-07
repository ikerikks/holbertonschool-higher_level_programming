#!/usr/bin/python3
"Unit tests for Base class"
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    "Unit tests suite for Base class"

    def test_constantId(self):
        "Test of Base for correctly initializing an id"
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_autoId(self):
        "Test of Base for automatically assigning and incrementing an id"
        b = Base()
        self.assertEqual(b.id, 1)

    def test_string(self):
        """Test of Base for case input is string"""
        b = Base("string")
        self.assertEqual(b.id, "string")

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

    def test_from_json_string(self):
        """ Test from_json_string - check json string return to list """
        string = '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]'
        json_str = Base.from_json_string(string)
        self.assertTrue(isinstance(string, str))
        self.assertTrue(isinstance(json_str, list))
        self.assertCountEqual(
            json_str, [{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}])
        json_s_1 = Base.from_json_string(None)
        self.assertEqual(json_s_1, [])
        err = ("from_json_string() missing 1 required positional argument: " +
               "'json_string'")
        with self.assertRaises(TypeError) as i:
            Base.from_json_string()
        self.assertEqual(err, str(i.exception))
        err = "from_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as i:
            Base.from_json_string('[1]', '[2]')
        self.assertEqual(err, str(i.exception))


if __name__ == "__main__":
    unittest.main()
