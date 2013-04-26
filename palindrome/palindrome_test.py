import unittest
from palindrome import *

# looks for classes that inherit from unittest.TestCase
# run all methods like test.*

class PalindromeTest(unittest.TestCase):

    def testPalTestNone(self):
        self.assertNone(palTest(None))

    def testPalTestEven(self):
        pass

    def testPalTestOdd(self):
        pass

