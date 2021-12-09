##Elijah Stroot
##CS101 Lab
##Assignment 13
##December 9, 2021


###Code:

import unittest


def total(values):
    x = sum(values)
    x = float(x)
    z = x/(len(values))

    return z

def median(xlist):
    new_list = xlist.sort() 
    middle = len(new_list) // 2
    return new_list[middle]

class my_test(unittest.TestCase):
    def test_average_one(self):
        self.assertAlmostEqual( 0.1 + 0.2, 0.3, 3)

    def test_average_two(self):
        self.assertAlmostEqual( 0.1 + 0.2, 0.3, 3)
    def test_average_returns_nan(self):
        pass
    
