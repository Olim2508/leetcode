import unittest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(0, len(nums) + 1)) - sum(nums)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 0, 1]
        result = self.solution.missingNumber(nums)
        self.assertEqual(result, 2)

    def test_example_2(self):
        nums = [0, 1]
        result = self.solution.missingNumber(nums)
        self.assertEqual(result, 2)

    def test_example_3(self):
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        result = self.solution.missingNumber(nums)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
