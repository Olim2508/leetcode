import unittest
from collections import Counter, defaultdict
from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:
        hash_table = {}
        res_list = {}
        for char in s:
            hash_table[char] = 1 + hash_table.get(char, 0)

            res_list[char] = char + res_list.get(char, "")
        res = [v for key, v in sorted(res_list.items(), key=lambda item: -len(item[1]))]
        return "".join(res)

    def neetcode(self, s):
        counter = Counter(s)
        buckets = defaultdict(list)

        for char, count in counter.items():
            buckets[count].append(char)

        res = []
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res.append(c * i)
        return "".join(res)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "tree"
        result = self.solution.frequencySort(s)
        self.assertEqual(result, "eetr")

    def test_example_2(self):
        s = "cccaaa"
        result = self.solution.frequencySort(s)
        self.assertEqual(result, "cccaaa")

    def test_example_3(self):
        s = "Aabb"
        result = self.solution.frequencySort(s)
        self.assertEqual(result, "bbAa")


if __name__ == '__main__':
    unittest.main()
