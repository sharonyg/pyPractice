import unittest
from find3Max import readfile, find3Max

class TestReadFile(unittest.TestCase):

    def test_file(self):
        fileData = ['2134', '3412', '6421', '8723', '9239', '1234', '2345']
        f = readfile("sample1.dat")
	self.assertEqual(f, fileData)

class TestFind3Max(unittest.TestCase):

    def test1(self):
        data = [2134, 3412, 6421, 8723, 9239, 1234, 2345]
	value = [6421, 8723, 9239]
	self.assertEqual(find3Max(data), value)

    def test2(self):
        data = [234, 325, 421, 873, 929, 14, 5]
	value = [421, 873, 929]
	self.assertEqual(find3Max(data), value)

    def test_nag(self):
        data = [4, 12, 6, 00, 77, -12, -143]
	value = [6, 12, 77]
	self.assertEqual(find3Max(data), value)


if __name__ == '__main__':
    unittest.main() 
