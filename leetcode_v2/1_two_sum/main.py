import unittest
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target - nums[i]], i]
            else:
                hash_map[nums[i]] = i


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums, target = [2, 7, 11, 15], 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_example_2(self):
        nums, target = [3, 2, 4], 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [1, 2])

    def test_example_3(self):
        nums, target = [3, 3], 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_example_4(self):
        nums, target = [3, 4, 10, 1], 5
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [1, 3])

    def test_example_5(self):
        nums, target = [3, 2, 3], 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 2])


if __name__ == '__main__':
    unittest.main()
