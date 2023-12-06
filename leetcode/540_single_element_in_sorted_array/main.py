import unittest
from collections import defaultdict
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid
        return nums[left]


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 2)

    def test_example_2(self):
        nums = [3, 3, 7, 7, 10, 11, 11]
        result = self.solution.singleNonDuplicate(nums)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
