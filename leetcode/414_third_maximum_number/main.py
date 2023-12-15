import unittest
from collections import defaultdict
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximums = []
        for num in nums:
            if len(maximums) < 3 and num not in maximums:
                maximums.append(num)
            else:
                min_in_list = min(maximums)
                if min_in_list < num and num not in maximums:
                    maximums.remove(min_in_list)
                    maximums.append(num)
        return min(maximums) if len(maximums) == 3 else max(maximums)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 2, 1]
        result = self.solution.thirdMax(nums)
        self.assertEqual(result, 1)

    def test_example_2(self):
        nums = [1, 2]
        result = self.solution.thirdMax(nums)
        self.assertEqual(result, 2)

    def test_example_3(self):
        nums = [1, 2, 2, 5, 3, 5]
        result = self.solution.thirdMax(nums)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
