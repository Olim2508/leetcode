import unittest
from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        result = self.solution.containsDuplicate(nums)
        self.assertTrue(result)

    def test_example_2(self):
        nums = [1, 2, 3, 4]
        result = self.solution.containsDuplicate(nums)
        self.assertFalse(result)

    def test_example_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        result = self.solution.containsDuplicate(nums)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
