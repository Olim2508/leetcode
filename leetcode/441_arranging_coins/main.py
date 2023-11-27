import unittest
from collections import defaultdict
from typing import List


class Solution:
    def arrangeCoins(self, n: int) -> int:
        full_stairs = 0
        for i in range(1, n + 1):
            if n >= i:
                full_stairs += 1
                n = n - i
            else:
                break
        return full_stairs

    def binary_sol(self, n):
        stairs = 0
        while n >= 0:
            stairs += 1
            n = n - stairs
        return stairs - 1


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 5
        result = self.solution.arrangeCoins(n)
        self.assertEqual(result, 2)
        result = self.solution.binary_sol(n)
        self.assertEqual(result, 2)

    def test_example_2(self):
        n = 8
        result = self.solution.arrangeCoins(n)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
