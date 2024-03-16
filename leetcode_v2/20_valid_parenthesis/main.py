import unittest
from collections import defaultdict
from typing import List


class Solution:
    par_pair_map = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if not stack:
                if p not in self.par_pair_map:
                    return False
                stack.append(p)
            else:
                last = stack[-1]
                if p not in self.par_pair_map:
                    if p != self.par_pair_map[last]:
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(p)
        return bool(len(stack) == 0)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "()"
        result = self.solution.isValid(s)
        self.assertTrue(result)

    def test_example_2(self):
        s = "()[]{}"
        result = self.solution.isValid(s)
        self.assertTrue(result)

    def test_example_3(self):
        s = "(]"
        result = self.solution.isValid(s)
        self.assertFalse(result)

    def test_example_4(self):
        s = "{[]}"
        result = self.solution.isValid(s)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
