import unittest
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        res = set()
        has_set = set()
        for i in range(len(s) - 9):
            if s[i: i + 10] in has_set:
                res.add(s[i: i + 10])
            else:
                has_set.add(s[i: i + 10])
        return list(res)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        result = self.solution.findRepeatedDnaSequences(s)
        self.assertEqual(result, ["AAAAACCCCC", "CCCCCAAAAA"])

    def test_example_2(self):
        s = "AAAAAAAAAAA"
        result = self.solution.findRepeatedDnaSequences(s)
        self.assertEqual(result, ["AAAAAAAAAA"])

    def test_example_3(self):
        s = "AAAAAAAAAAAAA"
        result = self.solution.findRepeatedDnaSequences(s)
        self.assertEqual(result, ["AAAAAAAAAA"])


if __name__ == '__main__':
    unittest.main()
