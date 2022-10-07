#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from unittest import mock
import io
from models.rectangle import Rectangle
import json
import os


class TestRectangle(unittest.TestCase):
    "Unit test suite for Rectangle class"

    def test_init(self):
        "Test of Rectangle for width/height and default initialization"
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_type(self):
        "Test of Rectangle for wrong attribute types"
        self.assertRaisesRegex(
            TypeError, "width must be an integer", Rectangle, "1", 2)
        self.assertRaisesRegex(
            TypeError, "height must be an integer", Rectangle, 1, "2")
        self.assertRaisesRegex(
            TypeError, "x must be an integer", Rectangle, 1, 2, "3")
        self.assertRaisesRegex(
            TypeError, "y must be an integer", Rectangle, 1, 2, 3, "4")

    def test_value(self):
        "Test of Rectangle for invalid values"
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Rectangle, -1, 2)
        self.assertRaisesRegex(
            ValueError, "height must be > 0", Rectangle, 1, -2)
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Rectangle, 0, 2)
        self.assertRaisesRegex(
            ValueError, "height must be > 0", Rectangle, 1, 0)
        self.assertRaisesRegex(
            ValueError, "x must be >= 0", Rectangle, 1, 2, -3)
        self.assertRaisesRegex(
            ValueError, "y must be >= 0", Rectangle, 1, 2, 3, -4)

    def test_area(self):
        "Tests if Rectangle's area() exists and returns the right value"
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        "Tests if Rectangle's display() exists and prints right value"
        # Test for no y
        r = Rectangle(3, 2, 1, 0)
        with mock.patch("sys.stdout", new=io.StringIO()) as mocked_stdout:
            r.display()

        assert mocked_stdout.getvalue() == " ###\n ###\n"

        # Test for neither x nor y
        r = Rectangle(3, 2, 0, 0)
        with mock.patch("sys.stdout", new=io.StringIO()) as mocked_stdout:
            r.display()

        assert mocked_stdout.getvalue() == "###\n###\n"

    def test_str(self):
        "Tests if Rectangle's str representation exists and has right format"
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_dictionary(self):
        "Tests to_dictionary() method"
        s1 = Rectangle(10, 2, 1, 9)
        s1_dict = s1.to_dictionary()
        self.assertEqual(s1_dict, {'x': 1, 'y': 9, 'id': 9,
                                   'height': 2, 'width': 10})

    def test_update(self):
        "Tests if Rectangle's update() exists and updates the right args"
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_create(self):
        """tests create"""
        to_test = Rectangle.create(**{'id': 89, 'width': 1,
                                      'height': 2, 'x': 3})
        answer = Rectangle(1, 2, 3, 0, 89)
        self.assertEqual(str(to_test), str(answer))

        to_test = Rectangle.create(**{'id': 89, 'width': 1,
                                      'height': 2, 'x': 3, 'y': 4})
        answer = Rectangle(1, 2, 3, 4, 89)
        self.assertEqual(str(to_test), str(answer))

        to_test = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        answer = Rectangle(1, 2, 3, 0, 89)
        self.assertEqual(str(to_test), str(answer))

        to_test = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        answer = Rectangle(1, 2, 0, 0, 89)
        self.assertEqual(str(to_test), str(answer))

        to_test = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(to_test.id, 89)
        self.assertEqual(to_test.width, 1)
        self.assertEqual(to_test.x, 0)
        self.assertEqual(to_test.y, 0)

        to_test = Rectangle.create(**{'id': 89})
        self.assertEqual(to_test.id, 89)
        self.assertEqual(to_test.x, 0)
        self.assertEqual(to_test.y, 0)

    def test_save_to_file_None(self):
        """Test of Rectangle.save_to_file(None) in Rectangle exists"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as file:
            self.assertEqual(json.loads(file.read()), json.loads('[]'))
        os.remove("Rectangle.json")

    def test_save_empty_list(self):
        """test  empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as fileempty:
            self.assertEqual("[]", fileempty.read())


if __name__ == "__main__":
    unittest.main()
