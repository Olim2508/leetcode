import math
import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                return mid


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 2)

    def test_example_2(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
