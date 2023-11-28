import unittest
from collections import defaultdict
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        total_candies_Alice = sum(aliceSizes)
        total_candies_Bob = sum(bobSizes)

        difference = (total_candies_Alice - total_candies_Bob) // 2

        aliceSizes.sort()
        bobSizes.sort()

        def binary_search(arr, target):
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return arr[mid]
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return None

        for alice_candy in aliceSizes:
            target = alice_candy - difference
            found = binary_search(bobSizes, target)

            if found is not None:
                return [alice_candy, found]


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        aliceSizes = [1, 1]
        bobSizes = [2, 2]
        output = [1, 2]
        result = self.solution.fairCandySwap(aliceSizes, bobSizes)
        self.assertEqual(result, output)

    def test_example_2(self):
        aliceSizes = [1, 2]
        bobSizes = [2, 3]
        output = [1, 2]
        result = self.solution.fairCandySwap(aliceSizes, bobSizes)
        self.assertEqual(result, output)

    def test_example_3(self):
        aliceSizes = [2]
        bobSizes = [1, 3]
        output = [2, 3]
        result = self.solution.fairCandySwap(aliceSizes, bobSizes)
        self.assertEqual(result, output)

    def test_example_4(self):
        aliceSizes = [1, 2, 5]
        bobSizes = [2, 4]
        output = [5, 4]
        result = self.solution.fairCandySwap(aliceSizes, bobSizes)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
