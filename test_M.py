import unittest, random 
from MS import M

class TestMatrixClass(unittest.TestCase):

    def setUp(self):
        self.m = M([[1, 2], [3, 4]])

    def test_init(self):
        self.assertEqual(self.m.mat, [[1, 2], [3, 4]])

    def test_iter(self):
        self.assertEqual(list(iter(self.m)), [[1, 2], [3, 4]])

    def test_add_matrix(self):
        m2 = M([[5, 6], [7, 8]])
        result = self.m + m2
        self.assertEqual(result.mat, [[6, 8], [10, 12]])

    def test_add_int(self):
        result = self.m + 5
        self.assertEqual(result.mat, [[6, 7], [8, 9]])

    def test_add_list(self):
        result = self.m + [5, 6]
        self.assertEqual(result.mat, [[6, 8], [8, 10]])

    def test_repr(self):
        self.assertEqual(repr(self.m), "1 2\n3 4")


if __name__ == '__main__':
    unittest.main()