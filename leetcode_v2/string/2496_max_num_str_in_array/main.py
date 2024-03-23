import math
import unittest
from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = -math.inf
        for string in strs:
            max_val = max(max_val, int(string)) if string.isdigit() else max(max_val, len(string))
        return max_val


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        strs = ["alic3", "bob", "3", "4", "00000"]
        result = self.solution.maximumValue(strs)
        self.assertEqual(result, 5)

    def test_example_2(self):
        strs = ["1", "01", "001", "0001"]
        result = self.solution.maximumValue(strs)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
