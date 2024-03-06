import unittest
import random
from stores import *

class TestVectorMethodsRandomized(unittest.TestCase):

    def generate_random_vector(self, length):
        """Generate a random vector of a given length."""
        return v([random.randint(-10, 10) for _ in range(length)])

    def test_add_random(self):
        for _ in range(5):  # Run the test 5 times with different vectors
            length = random.randint(1, 10)
            v1 = self.generate_random_vector(length)
            v2 = self.generate_random_vector(length)
            result = v1 + v2
            expected = [n + m for n, m in zip(v1.data, v2.data)]
            self.assertEqual(result.data, expected, f"Failed for {v1.data} + {v2.data}")

    def test_sub_random(self):
        for _ in range(5):
            length = random.randint(1, 10)
            v1 = self.generate_random_vector(length)
            v2 = self.generate_random_vector(length)
            result = v1 - v2
            expected = [n - m for n, m in zip(v1.data, v2.data)]
            self.assertEqual(result.data, expected, f"Failed for {v1.data} - {v2.data}")

    def test_mul_random(self):
        for _ in range(5):
            length = random.randint(1, 10)
            v1 = self.generate_random_vector(length)
            v2 = self.generate_random_vector(length)
            result = v1 * v2
            expected = [n * m for n, m in zip(v1.data, v2.data)]
            self.assertEqual(result.data, expected, f"Failed for {v1.data} * {v2.data}")

    def test_intersection_random(self):
        for _ in range(5):
            length1 = random.randint(1, 10)
            length2 = random.randint(1, 10)
            v1 = self.generate_random_vector(length1)
            v2 = self.generate_random_vector(length2)
            result = v1.intersection(v2)
            expected = [n for n in v1.data if n in v2.data]
            self.assertEqual(result.data, expected, f"Failed for intersection of {v1.data} and {v2.data}")

    def test_union_random(self):
        for _ in range(5):  # Run the test 5 times with different vectors
            length1 = random.randint(1, 10)
            length2 = random.randint(1, 10)
            v1 = self.generate_random_vector(length1)
            v2 = self.generate_random_vector(length2)
            print(f"v1 : {v1.data}")
            print(f"v2 : {v2.data}")
            result = v1.union(v2)
            expected = list(v1.data)  # Elements from the first vector
            expected += [n for n in v2.data if n not in expected]  # Non-duplicate elements from the second vector
            self.assertEqual(result.data, expected, f"Failed for union of {v1.data} and {v2.data}")


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
