import unittest
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.dig_to_let = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        total = 1
        for d in digits:
            total *= len(self.dig_to_let[d])
            if not res:
                for let in self.dig_to_let[d]:
                    res.append(let)
            else:
                temp = []
                for item in res:
                    for let in self.dig_to_let[d]:
                        new = item + let
                        temp.append(new)
                res += temp
        return res[-total::]

    def gpt_sol(self, digits: str) -> List[str]:
        if not digits:
            return []

        combinations = []

        def backtrack(index, path):
            if index == len(digits):
                combinations.append(path)
                return

            for letter in self.dig_to_let[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, '')
        return combinations


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        digits = "23"
        output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, output)
        result = self.solution.gpt_sol(digits)
        self.assertEqual(result, output)

    def test_example_2(self):
        digits = ""
        output = []
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, output)

    def test_example_3(self):
        digits = "2"
        output = ["a", "b", "c"]
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
