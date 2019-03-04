import unittest
from nameScore import score

class TestNameScore(unittest.TestCase):

    def test_1(self):
        file_data = '"CDEF", "ABC", "FIJK"'
	self.assertEqual(score(file_data), 150)

    def test_2(self):
        file_data = '"QABB", "KK", "QWE"'
	self.assertEqual(score(file_data), 201)

    def test_3(self):
        file_data = '"ABC", "ABDE", "ABCD"'
	self.assertEqual(score(file_data), 62)

    def test_4(self):
	file_data = '"", "", ""'
	self.assertEqual(score(file_data), 0)

if __name__ == '__main__':
    unittest.main()
