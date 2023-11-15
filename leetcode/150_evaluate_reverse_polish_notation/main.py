import unittest
from collections import defaultdict
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                last = stack.pop()
                first = stack.pop()
                stack.append(first + last)
            elif token == "-":
                last = stack.pop()
                first = stack.pop()
                stack.append(first - last)
            elif token == "*":
                last = stack.pop()
                first = stack.pop()
                stack.append(first * last)
            elif token == "/":
                last = stack.pop()
                first = stack.pop()
                stack.append(int(first / last))
            else:
                stack.append(int(token))
        return stack[0]


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        tokens = ["2", "1", "+", "3", "*"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 9)

    def test_example_2(self):
        tokens = ["4", "13", "5", "/", "+"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 6)

    def test_example_3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 22)


if __name__ == '__main__':
    unittest.main()
