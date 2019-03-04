import unittest
from listCompre import listCompre

class TestListComprehension(unittest.TestCase): 
    def test_1(self):
        self.assertEqual(0, listCompre(1))

    def test_11(self):
        self.assertEqual(-55, listCompre(11))

    def test_21(self):
        self.assertEqual(-210, listCompre(21))

if __name__ == '__main__':
    unittest.main() 
