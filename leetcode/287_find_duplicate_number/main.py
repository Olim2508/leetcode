import math
import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return num
            hash_set.add(num)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 3, 4, 2, 2]
        result = self.solution.findDuplicate(nums)
        self.assertEqual(result, 2)

    def test_example_2(self):
        nums = [3, 1, 3, 4, 2]
        result = self.solution.findDuplicate(nums)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
