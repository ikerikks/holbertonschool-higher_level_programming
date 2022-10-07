#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from unittest import mock
import io
from models.square import Square
from models.base import Base
import os
import json


class TestSquare(unittest.TestCase):
    """Testing Square"""

    def test_instance(self):
        """test input size correct standard """

        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

        with self.assertRaises(TypeError):
            Square(5, "1")

        with self.assertRaises(TypeError):
            Square()

        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(ValueError):
            Square(-5, 3, 4)

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_case_normal(self):
        """Test of Square(1, 2, 3, 4) exists"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        """testing area"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

        s = Square(1, 2)
        self.assertEqual(s.area(), 1)

    def test_display(self):
        """test display()"""
        s = Square(5)
        with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            s.display()

        assert mock_stdout.getvalue() == "#####\n#####\n#####\n#####\n#####\n"

        s = Square(1, 2)
        with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            s.display()

        assert mock_stdout.getvalue() == "  #\n"

    def test_string(self):
        """Test str"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.__str__(), '[Square] (4) 2/3 - 1')

    def test_update(self):
        """test update()"""
        s1 = Square(2)
        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(size=1, id=89, x=2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.x, 2)

    def test_created(self):
        """Test of Square.create(**{ 'id': 89 }) in Square exists"""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        """
        Test of to_dictionary() in Square exists
        """
        dict = {'id': 7, 'size': 10, 'x': 9, 'y': 8}
        s = Square(10, 9, 8, 7)
        self.assertEqual(dict, s.to_dictionary())

    def test_save_to_file_none(self):
        """Test that `save_to_file()` instance used to directly
        serialize and write to file and delete the file
        """
        Base._Base__nb_object = 0
        s1 = Square(9, 2, 7)
        s2 = Square(2)
        Square.save_to_file(None)
        self.assertIs(os.path.exists("Square.json"), True)
        with open("Square.json", 'r') as file:
            self.assertEqual(json.loads(file.read()), json.loads('[]'))
        os.remove("Square.json")

    def test_save_empty_list(self):
        """test empty list"""
        Base._Base__nb_object = 0
        Square.save_to_file([])
        with open("Square.json", "r") as file2:
            self.assertEqual("[]", file2.read())
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
