import unittest
from fib import fib

class TestFibo(unittest.TestCase):

    def test_fib_1(self):
        c = fib()
        for i in range(1):
            next = c.next()
        self.assertEqual(1, next)
	
    def test_fib_7(self):
	c = fib()
	for i in range(7):
	    next = c.next()
	self.assertEqual(21, next)

    def test_fib_20(self):
	c = fib()
	for i in range(20):
	    next = c.next()
	self.assertEqual(10946, next)

  
if __name__ == '__main__':
    unittest.main()
