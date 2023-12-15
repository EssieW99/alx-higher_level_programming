#!/usr/bin/python3
"""defines unit tests for base.py"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


class Test_id_instantiation(unittest.TestCase):
    """tests for instantiation of the base class"""

    def test_for_no_arg(self):
        case1 = Base()
        case2 = Base()
        self.assertEqual(case1.id, case2.id - 1)

    def test__arg_given(self):
        case1 = Base(4)
        self.assertEqual(4, case1.id)

    def test_for_args_andno_arg(self):
        case1 = Base()
        case2 = Base(5)
        case3 = Base()
        self.assertEqual(case1.id, case3.id - 1)

    def test_for_None(self):
        case1 = Base(None)
        case2 = Base(None)
        self.assertEqual(case1.id, case2.id - 1)

    def test_float_arg(self):
        case1 = Base(6.7)
        self.assertEqual(case1.id, 6.7)

    def test_range(self):
        self.assertEqual(range(3), Base(range(3)).id)

    def test_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_list(self):
        self.assertEqual([5, 2, 7, 1], Base([5, 2, 7, 1]).id) 


class Test_to_json_string(unittest.TestCase):
    """tests for to_json_string method of the base class"""

    def test_for_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_a_rectangle(self):
        rect = Rectangle(10, 7, 2, 8, 2)
        self.assertEqual(str, type(Base.to_json_string(rect.to_dictionary())))

    def test_a_square(self):
        sq = Square(10, 2, 1, 3)
        self.assertEqual(str, type(Base.to_json_string(sq.to_dictionary())))

if __name__ == "__main__":
    unittest.main()
