import unittest
from collections import defaultdict
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        prices = [8, 4, 6, 2, 3]
        output = [4, 2, 4, 2, 3]
        result = self.solution.finalPrices(prices)
        self.assertEqual(result, output)

    def test_example_2(self):
        prices = [1, 2, 3, 4, 5]
        output = [1, 2, 3, 4, 5]
        result = self.solution.finalPrices(prices)
        self.assertEqual(result, output)


    def test_example_3(self):
        prices = [10, 1, 1, 6]
        output = [9, 0, 1, 6]
        result = self.solution.finalPrices(prices)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
