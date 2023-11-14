import unittest
from collections import defaultdict
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counter = defaultdict(int)
        for c in chars:
            char_counter[c] += 1
        res = 0

        for word in words:
            tem_map = char_counter.copy()
            for c in word:
                if c in tem_map and tem_map[c] > 0:
                    tem_map[c] -= 1
                else:
                    break
            else:
                res += len(word)
        return res


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        words, chars = ["cat", "bt", "hat", "tree"], "atach"
        result = self.solution.countCharacters(words, chars)
        self.assertEqual(result, 6)

    def test_example_2(self):
        words, chars = ["hello", "world", "leetcode"], "welldonehoneyr"
        result = self.solution.countCharacters(words, chars)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
