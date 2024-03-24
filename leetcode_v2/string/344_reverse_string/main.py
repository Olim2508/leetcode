import math
import unittest
from typing import List

import string


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_str = len(s)
        i = 0
        while i < len_str // 2:
            s[i], s[len_str - i - 1] = s[len_str - i - 1], s[i]
            i += 1


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = ["h", "e", "l", "l", "o"]
        self.solution.reverseString(s)

    def test_example_2(self):
        s = ["H", "a", "n", "n", "a", "h"]
        self.solution.reverseString(s)


if __name__ == '__main__':
    unittest.main()
