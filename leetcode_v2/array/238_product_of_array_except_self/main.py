import unittest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [24, 12, 8, 6])

    def test_example_2(self):
        nums = [-1, 1, 0, -3, 3]
        result = self.solution.productExceptSelf(nums)
        self.assertEqual(result, [0, 0, 9, 0, 0])

    # def test_example_3(self):
    #     nums = [1]
    #     result = self.solution.findDuplicates(nums)
    #     self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
