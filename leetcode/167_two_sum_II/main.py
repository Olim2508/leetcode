import unittest
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                print(left, right)
                return [left + 1, right + 1]


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(numbers, target)
        self.assertEqual(result, [1, 2])

    def test_example_2(self):
        numbers = [2, 3, 4]
        target = 6
        result = self.solution.twoSum(numbers, target)
        self.assertEqual(result, [1, 3])

    def test_example_3(self):
        numbers = [-1, 0]
        target = -1
        result = self.solution.twoSum(numbers, target)
        self.assertEqual(result, [1, 2])


if __name__ == '__main__':
    unittest.main()
