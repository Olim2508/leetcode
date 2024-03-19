import unittest
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                last = stack.pop()
                pre_last = stack.pop()
                stack.append(last + pre_last)
            elif char == "-":
                last = stack.pop()
                pre_last = stack.pop()
                stack.append(pre_last - last)
            elif char == "*":
                last = stack.pop()
                pre_last = stack.pop()
                stack.append(last * pre_last)
            elif char == "/":
                last = stack.pop()
                pre_last = stack.pop()
                stack.append(int(pre_last / last))
            else:
                stack.append(int(char))
        return stack[-1]


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
