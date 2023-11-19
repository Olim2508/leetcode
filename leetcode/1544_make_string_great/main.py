import unittest
from collections import defaultdict
from typing import List


class Solution:

    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 2:
                first_char = stack[-1]
                second_char = stack[-2]
                if first_char != second_char and first_char.lower() == second_char.lower():
                    stack.pop()
                    stack.pop()
        return "".join(stack)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "leEeetcode"
        output = "leetcode"
        result = self.solution.makeGood(s)
        self.assertEqual(result, output)

    def test_example_2(self):
        s = "abBAcC"
        output = ""
        result = self.solution.makeGood(s)
        self.assertEqual(result, output)

    def test_example_3(self):
        s = "s"
        output = "s"
        result = self.solution.makeGood(s)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
