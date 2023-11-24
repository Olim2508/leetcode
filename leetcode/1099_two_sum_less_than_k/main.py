import unittest
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        max_tar = float("-inf")
        while l <= r:
            if nums[l] + nums[r] < target:
                max_tar = max(max_tar, nums[l] + nums[r])
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return max_tar if isinstance(max_tar, int) else -1


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [34, 23, 1, 24, 75, 33, 54, 8]
        target = 60
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, 58)

    def test_example_2(self):
        nums = [10, 20, 30]
        target = 15
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
