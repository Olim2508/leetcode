import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        print("array", arr)
        print("k", k)
        for n in range(1, arr[-1] + 1):
            l, r = 0, len(arr) - 1
            found = False
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] > n:
                    r = mid - 1
                elif arr[mid] < n:
                    l = mid + 1
                else:
                    found = True
                    break
            if not found:
                missing.append(n)
        if len(missing) >= k:
            return missing[k - 1]
        else:
            if len(missing) == 0:
                nums = self.get_num(arr[-1], arr[-1] + k)
                return nums[-1]
            else:
                nums = self.get_num(arr[-1] + 1, arr[-1] + k)
                return nums[-len(missing) - 1]

    def get_num(self, start, end):
        return list(range(start, end + 1))


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        arr = [2, 3, 4, 7, 11]
        k = 5
        result = self.solution.findKthPositive(arr, k)
        self.assertEqual(result, 9)

    def test_example_2(self):
        arr = [1, 2, 3, 4]
        k = 2
        result = self.solution.findKthPositive(arr, k)
        self.assertEqual(result, 6)

    def test_example_3(self):
        arr = [5, 6, 7, 8, 9]
        k = 9
        result = self.solution.findKthPositive(arr, k)
        self.assertEqual(result, 14)


if __name__ == '__main__':
    unittest.main()
