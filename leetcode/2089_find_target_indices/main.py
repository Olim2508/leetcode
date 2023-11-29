import unittest
from collections import defaultdict
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i in range(len(nums)) if nums[i] == target]


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 5, 2, 3]
        target = 2
        output = [1, 2]
        result = self.solution.targetIndices(nums, target)
        self.assertEqual(result, output)

    def test_example_2(self):
        nums = [1, 2, 5, 2, 3]
        target = 3
        output = [3]
        result = self.solution.targetIndices(nums, target)
        self.assertEqual(result, output)

    def test_example_3(self):
        nums = [1, 2, 5, 2, 3]
        target = 5
        output = [4]
        result = self.solution.targetIndices(nums, target)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
