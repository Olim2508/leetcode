import math
import unittest
from typing import List

import string


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and t:
            return True
        s_stack = list(s)
        for char in t[::-1]:
            if s_stack:
                last_ch = s_stack[-1]
                if char == last_ch:
                    s_stack.pop()

        return True if not s_stack else False


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "abc"
        t = "ahbgdc"
        res = self.solution.isSubsequence(s, t)
        self.assertTrue(res)

    def test_example_2(self):
        s = "axc"
        t = "ahbgdc"
        res = self.solution.isSubsequence(s, t)
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
