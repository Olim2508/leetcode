import unittest
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licence_map = {}
        for let in licensePlate:
            if not let.isdigit() and let != " ":
                licence_map[let.lower()] = 1 + licence_map.get(let.lower(), 0)

        res = []  # [len, word]
        for word in words:
            word_map = {}
            for let in word:
                word_map[let.lower()] = 1 + word_map.get(let.lower(), 0)

            for k, v in licence_map.items():
                if k not in word_map or v > word_map[k]:
                    break
            else:
                if not res or res[0] > len(word):
                    res = [len(word), word]
        return res[1]


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        licensePlate = "1s3 PSt"
        words = ["step", "steps", "stripe", "stepple"]
        result = self.solution.shortestCompletingWord(licensePlate, words)
        self.assertEqual(result, "steps")

    def test_example_2(self):
        licensePlate = "1s3 456"
        words = ["looks", "pest", "stew", "show"]
        result = self.solution.shortestCompletingWord(licensePlate, words)
        self.assertEqual(result, "pest")


if __name__ == '__main__':
    unittest.main()
