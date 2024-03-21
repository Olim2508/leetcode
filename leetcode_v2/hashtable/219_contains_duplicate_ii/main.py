import unittest
from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for idx, num in enumerate(nums):
            if num not in hash_map:
                hash_map[num] = idx
            else:
                if abs(hash_map[num] - idx) <= k:
                    return True
                else:
                    hash_map[num] = idx  # update existing index with the bigger one, so that the diff would be minimal
        return False


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        k = 3
        result = self.solution.containsNearbyDuplicate(nums, k)
        self.assertTrue(result)

    def test_example_2(self):
        nums = [1, 0, 1, 1]
        k = 1
        result = self.solution.containsNearbyDuplicate(nums, k)
        self.assertTrue(result)

    def test_example_3(self):
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        result = self.solution.containsNearbyDuplicate(nums, k)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
