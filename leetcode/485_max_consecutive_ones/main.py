import math
import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = -math.inf
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                max_count = max(max_count, count)
                count = 0
        return max_count


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 0, 1, 1, 1]
        result = self.solution.findMaxConsecutiveOnes(nums)
        self.assertEqual(result, 3)

    # def test_example_2(self):
    #     nums = [1, 0, 1, 1, 0, 1]
    #     result = self.solution.findMaxConsecutiveOnes(nums)
    #     self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
