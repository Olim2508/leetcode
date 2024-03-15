import unittest
from collections import defaultdict
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}
        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

        for k, v in s_count.items():
            if k not in t_count:
                return False
            if v != t_count[k]:
                return False
        return True


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s, t = "anagram", "nagaram"
        result = self.solution.isAnagram(s, t)
        self.assertTrue(result)

    def test_example_2(self):
        s, t = "rat", "car"
        result = self.solution.isAnagram(s, t)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
