import unittest
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """time - O(n), space - O(n)"""
        res = {num for num in range(1, len(nums) + 1)}
        for num in nums:
            if num in res:
                res.remove(num)
        return list(res)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        result = self.solution.findDisappearedNumbers(nums)
        self.assertEqual(result, [5, 6])

    def test_example_2(self):
        nums = [1, 1]
        result = self.solution.findDisappearedNumbers(nums)
        self.assertEqual(result, [2])


if __name__ == '__main__':
    unittest.main()
