import unittest, random
from MS import v

class TestVectorMethodsRandomized(unittest.TestCase):
    testtimes = 10
    def generate_random_vector(self, length):
        # self.testtime = length
        """Generate a random vector of a given length."""
        return [random.randint(-10, 10) for _ in range(length)]

    def test_add_random(self):
        for _ in range(self.testtimes):  # Run the test 5 times with different vectors
            length = random.randint(1, 10)
            v1 = self.generate_random_vector(length)
            v2 = self.generate_random_vector(length)
            result = v(v1) + v(v2)
            
            expected = [n + m for n, m in zip(v1, v2)]
            self.assertEqual(result.data, expected, f"Failed for {v1} + {v2}")

    def test_sub_random(self):
        for _ in range(self.testtimes):
            length = random.randint(1, 10)
            v1 = self.generate_random_vector(length)
            v2 = self.generate_random_vector(length)
            result = v(v1) - v(v2)
            expected = [n - m for n, m in zip(v1, v2)]
            self.assertEqual(result.data, expected, f"Failed for {v1} - {v2}")

    def test_mul_random(self):
        for _ in range(self.testtimes):
            length = random.randint(1, 10)
            v1 = self.generate_random_vector(length)
            v2 = self.generate_random_vector(length)
            result = v(v1) * v(v2)
            expected = [n * m for n, m in zip(v1, v2)]
            self.assertEqual(result.data, expected, f"Failed for {v1} * {v2}")

    def test_intersection_random(self):
        for _ in range(5):
            length1 = random.randint(1, 10)
            length2 = random.randint(1, 10)
            v1 = self.generate_random_vector(length1)
            v2 = self.generate_random_vector(length2)
            result = v(v1).intersection(v(v2))
            seen = set()
            expected = [n for n in v1 if n in set(v2) and (n not in seen and not seen.add(n))]
            self.assertEqual(result.data, expected, f"Failed for intersection of {v1} and {v2}")

    def test_union_random(self):
        for _ in range(self.testtimes):  # Run the test 5 times with different vectors
            length1 = random.randint(1, 10)
            length2 = random.randint(1, 10)
            v1 = self.generate_random_vector(length1)
            v2 = self.generate_random_vector(length2)
            result = v(v1).union(v(v2))
            expected = list(set(v1).union(set(v2))) # Non-duplicate elements from the second vector
            self.assertEqual(result.data, sorted(expected), f"Failed for union of {v1} and {v2}")

if __name__ == '__main__':
    unittest.main()