import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for n1 in arr1:
            is_all = True
            for n2 in arr2:
                if abs(n1 - n2) <= d:
                    is_all = False
            if is_all:
                res += 1
        return res

    def binary_search_sol(self, arr1, arr2, d):
        res = 0
        arr2.sort()
        for n1 in arr1:
            l, r = 0, len(arr2) - 1
            is_all = True
            while l <= r:
                mid = (l + r) // 2
                if abs(arr2[mid] - n1) <= d:
                    is_all = False
                    break
                elif n1 < arr2[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            if is_all:
                res += 1
        return res


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        arr1 = [4, 5, 8]
        arr2 = [10, 9, 1, 8]
        d = 2
        result = self.solution.findTheDistanceValue(arr1, arr2, d)
        self.assertEqual(result, 2)
        result = self.solution.binary_search_sol(arr1, arr2, d)
        self.assertEqual(result, 2)

    def test_example_2(self):
        arr1 = [1, 4, 2, 3]
        arr2 = [-4, -3, 6, 10, 20, 30]
        d = 3
        result = self.solution.findTheDistanceValue(arr1, arr2, d)
        self.assertEqual(result, 2)
        result = self.solution.binary_search_sol(arr1, arr2, d)
        self.assertEqual(result, 2)

    def test_example_3(self):
        arr1 = [2, 1, 100, 3]
        arr2 = [-5, -2, 10, -3, 7]
        d = 6
        result = self.solution.findTheDistanceValue(arr1, arr2, d)
        self.assertEqual(result, 1)
        result = self.solution.binary_search_sol(arr1, arr2, d)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
