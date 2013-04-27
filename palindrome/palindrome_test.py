import unittest
from palindrome import *

<<<<<<< HEAD
# looks for classes that inherit from unittest.TestCase
# run all methods like test.*

class PalindromeTest(unittest.TestCase):

    def testPalTestNone(self):
        self.assertNone(palTest(None))

    def testPalTestEven(self):
        pass

    def testPalTestOdd(self):
        pass

=======

class PalindromeTest(unittest.TestCase):

    def testListMakerNone(self):
        pass


    def testListMakerEven(self):
        pass


    def testListMakerOdd(self):
        pass






def main():
    unittest.main()

if __name__ == '__main__':
    main()
        
>>>>>>> 9c6d8b484d6504bddb1368adfaaf584cdbe88497
