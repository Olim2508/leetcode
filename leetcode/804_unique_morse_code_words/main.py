import unittest
from collections import defaultdict
from typing import List


class Solution:
    word_mapping = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                    "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    def map_letters(self):
        alph_letters = [chr(v) for v in range(ord('a'), ord('a') + 26)]
        # print(alph_letters)
        mapped = {}
        print(Solution.word_mapping)
        for alp, code in zip(alph_letters, Solution.word_mapping):
            mapped[alp] = code
        return mapped

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique_set = set()
        mapping = self.map_letters()
        for w in words:
            morse_code = []
            for let in w:
                morse_code.append(mapping[let])
            word = "".join(morse_code)
            if word not in unique_set:
                unique_set.add(word)
        return len(unique_set)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        words = ["gin", "zen", "gig", "msg"]
        result = self.solution.uniqueMorseRepresentations(words)
        self.assertEqual(result, 2)

    # def test_example_2(self):
    #     words = ["a"]
    #     result = self.solution.uniqueMorseRepresentations(words)
    #     self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
