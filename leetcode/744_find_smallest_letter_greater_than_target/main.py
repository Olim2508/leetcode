import unittest
from collections import defaultdict
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(letters[-1]) <= ord(target):
            return letters[0]

        l, r = 0, len(letters) - 1
        char_code = 0
        while l <= r:
            mid = (l + r) // 2
            if ord(letters[mid]) > ord(target):
                char_code = ord(letters[mid])
                r = mid - 1
            else:
                l = mid + 1
        return chr(char_code)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        letters = ["c", "f", "j"]
        target = "a"
        result = self.solution.nextGreatestLetter(letters, target)
        self.assertEqual(result, "c")

    def test_example_2(self):
        letters = ["c", "f", "j"]
        target = "c"
        result = self.solution.nextGreatestLetter(letters, target)
        self.assertEqual(result, "f")

    def test_example_3(self):
        letters = ["x", "x", "y", "y"]
        target = "z"
        result = self.solution.nextGreatestLetter(letters, target)
        self.assertEqual(result, "x")

    def test_example_4(self):
        letters = ["c", "f", "j"]
        target = "j"
        result = self.solution.nextGreatestLetter(letters, target)
        self.assertEqual(result, "c")


if __name__ == '__main__':
    unittest.main()
