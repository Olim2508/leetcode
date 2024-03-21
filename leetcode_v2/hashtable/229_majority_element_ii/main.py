import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        hash_map = {}
        times = len(nums) / 3
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        for k, v in hash_map.items():
            if v > times:
                res.append(k)

        return res


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 2, 3]
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, [3])

    def test_example_2(self):
        nums = [1]
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, [1])

    def test_example_3(self):
        nums = [1, 2]
        result = self.solution.majorityElement(nums)
        self.assertEqual(result, [1, 2])


if __name__ == '__main__':
    unittest.main()
