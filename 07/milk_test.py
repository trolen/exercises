#!/usr/bin/env python

from datetime import date
import unittest

import milk


class MilkTests(unittest.TestCase):

    def test_input_string_dashes(self):
        self.assertEqual(
            (2014, 7, 30),
            milk.get_date_tuple('2014-7-30')
        )

    def test_input_string_slashes(self):
        self.assertEqual(
            (2014, 7, 30),
            milk.get_date_tuple('2014/7/30')
        )

    def test_input_string_spaces(self):
        self.assertEqual(
            (2014, 7, 30),
            milk.get_date_tuple('2014 7 30')
        )

    def test_input_list(self):
        self.assertEqual(
            (2014, 7, 30),
            milk.get_date_tuple([2014, 7, 30])
        )

    def test_input_tuple(self):
        self.assertEqual(
            (2014, 7, 30),
            milk.get_date_tuple((2014, 7, 30))
        )

    def test_input_date(self):
        self.assertEqual(
            (2014, 7, 30),
            milk.get_date_tuple(date(2014, 7, 30))
        )

    def test_make_year_0(self):
        self.assertEqual(
            2000,
            milk.make_year(0)
        )

    def test_make_year_49(self):
        self.assertEqual(
            2049,
            milk.make_year(49)
        )

    def test_make_year_50(self):
        self.assertEqual(
            1950,
            milk.make_year(50)
        )

    def test_make_year_99(self):
        self.assertEqual(
            1999,
            milk.make_year(99)
        )
       
    def test_equal_day_and_year(self):
        self.assertEqual(
            100,
            milk.chance_not_expired('14-12-14', today='2006-7-5')
        )

    def test_50(self):
        self.assertEqual(
            50,
            milk.chance_not_expired([8, 2, 2006], today=[2006, 7, 5])
        )

    def test_33(self):
        self.assertEqual(
            33,
            milk.chance_not_expired((6, 7, 5), today=(2006, 7, 5))
        )

    def test_67(self):
        self.assertEqual(
            67,
            milk.chance_not_expired('6 5 7', today='2006 7 5')
        )

    def test_0(self):
        self.assertEqual(
            0,
            milk.chance_not_expired('12/31/99', today='2006/7/5')
        )

    def test_year_00(self):
        self.assertEqual(
            100,
            milk.chance_not_expired('00-12-31', today='00-7-5')
        )


if __name__ == '__main__':
    unittest.main()
