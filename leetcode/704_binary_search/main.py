import unittest
from collections import defaultdict
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        result = self.solution.search(nums, target)
        self.assertEqual(result, 4)

    def test_example_2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        result = self.solution.search(nums, target)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
