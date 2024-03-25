import unittest
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                res.append(num)
            nums[num - 1] = -nums[num - 1]
        return res


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [4,3,2,7,8,2,3,1]
        result = self.solution.findDuplicates(nums)
        self.assertEqual(result, [2,3])

    def test_example_2(self):
        nums = [1,1,2]
        result = self.solution.findDuplicates(nums)
        self.assertEqual(result, [1])

    def test_example_3(self):
        nums = [1]
        result = self.solution.findDuplicates(nums)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
