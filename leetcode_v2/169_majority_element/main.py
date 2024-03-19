import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)
            if hash_map[num] > len(nums) / 2:
                return num


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        temperatures = [3, 2, 3]
        result = self.solution.majorityElement(temperatures)
        self.assertEqual(result, 3)

    def test_example_2(self):
        temperatures = [2, 2, 1, 1, 1, 2, 2]
        result = self.solution.majorityElement(temperatures)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
