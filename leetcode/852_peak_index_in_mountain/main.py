import math
import unittest
from collections import defaultdict
from typing import List


class Solution:  # should be solved in O(log(n)) time
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r:
            mid = l + (r - l) // 2

            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l

    def brute_force(self, arr):
        max_num = -math.inf
        idx = 0
        for i in range(len(arr)):
            if arr[i] > max_num:
                max_num = arr[i]
                idx = i
        return idx


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_example_1(self):
    #     arr = [0, 10, 5, 2]
    #     result = self.solution.peakIndexInMountainArray(arr)
    #     self.assertEqual(result, 1)
    #     result = self.solution.brute_force(arr)
    #     self.assertEqual(result, 1)
    #
    # def test_example_2(self):
    #     arr = [0, 2, 1, 0]
    #     result = self.solution.peakIndexInMountainArray(arr)
    #     self.assertEqual(result, 1)
    #     result = self.solution.brute_force(arr)
    #     self.assertEqual(result, 1)

    def test_example_3(self):
        arr = [3,9,8,6,4]
        result = self.solution.peakIndexInMountainArray(arr)
        self.assertEqual(result, 1)
        result = self.solution.brute_force(arr)
        self.assertEqual(result, 1)

    # def test_example_4(self):
    #     arr = [3,4,5,1]
    #     result = self.solution.peakIndexInMountainArray(arr)
    #     self.assertEqual(result, 2)
    #     result = self.solution.brute_force(arr)
    #     self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
