import unittest
from collections import defaultdict
from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        for i in range(len(haystack) - n_len + 1):
            if haystack[i:i + n_len] == needle:
                return i
        return -1


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        haystack = "sadbutsad"
        needle = "sad"
        result = self.solution.strStr(haystack, needle)
        self.assertEqual(result, 0)

    def test_example_2(self):
        haystack = "leetcode"
        needle = "leeto"
        result = self.solution.strStr(haystack, needle)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
