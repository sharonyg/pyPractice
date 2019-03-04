import unittest
from perfectNum import is_perfect

class TestPerfect(unittest.TestCase):

    def test_6(self):
	self.assertEqual(is_perfect(6), 1)

    def test_8(self):
	self.assertEqual(is_perfect(8), 0)

    def test_28(self):
	self.assertEqual(is_perfect(28), 1)

if __name__ == '__main__':
    unittest.main()


