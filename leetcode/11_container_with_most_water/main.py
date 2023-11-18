import unittest
from collections import defaultdict
from typing import List


class Solution:
    # not efficient, O(n^2)
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                width = j - i
                height_val = min(height[i], height[j])
                area = width * height_val
                if max_area < area:
                    max_area = area
        return max_area

    def linear_time_sol(self, height):
        left, right = 0, len(height) - 1
        max_area = float("-inf")
        while left < right:
            width_val = right - left
            height_val = min(height[left], height[right])
            area = width_val * height_val
            if max_area < area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = self.solution.maxArea(height)
        self.assertEqual(result, 49)
        result = self.solution.linear_time_sol(height)
        self.assertEqual(result, 49)

    def test_example_2(self):
        height = [1, 1]
        result = self.solution.maxArea(height)
        self.assertEqual(result, 1)
        result = self.solution.maxArea(height)
        self.assertEqual(result, 1)



if __name__ == '__main__':
    unittest.main()
