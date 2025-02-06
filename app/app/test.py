'''
test for calc
'''

from django.test import SimpleTestCase

from app import calc

class Calctest(SimpleTestCase):
    """test the class module."""

    def test_add_numbers(self):
        """test adding numbers together"""

        res = calc.addNum(5,6)

        self.assertEqual(res, 11)

    def test_subtraction(self):
        
        res = calc.substract(10,15)

        self.assertEqual(res, 5)