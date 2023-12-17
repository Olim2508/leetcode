import unittest
from collections import defaultdict
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1
        return n - left


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        citations = [0, 1, 3, 5, 6]
        result = self.solution.hIndex(citations)
        self.assertEqual(result, 3)
    #
    # def test_example_2(self):
    #     citations = [1, 2, 100]
    #     result = self.solution.hIndex(citations)
    #     self.assertEqual(result, 2)

    # def test_example_3(self):
    #     citations = [0]
    #     result = self.solution.hIndex(citations)
    #     self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
