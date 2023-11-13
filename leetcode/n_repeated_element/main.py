import unittest
from collections import defaultdict
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return num
            hash_set.add(num)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 3]
        result = self.solution.repeatedNTimes(nums)
        self.assertEqual(result, 3)

    def test_example_2(self):
        nums = [2, 1, 2, 5, 3, 2]
        result = self.solution.repeatedNTimes(nums)
        self.assertEqual(result, 2)

    def test_example_3(self):
        nums = [5, 1, 5, 2, 5, 3, 5, 4]
        result = self.solution.repeatedNTimes(nums)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
