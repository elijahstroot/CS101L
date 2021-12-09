##Elijah Stroot
##CS101 Lab
##Assignment 13
##December 9, 2021


###Code:

import unittest
import Grades
import Assignment15_Grades


def total(values):
    x = sum(values)
    x = float(x)
    return x

class Grade_Test(unittest.TestCase):

    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")

    def test_total_returns_0(self):
        Grades.total([])


unittest.main()
