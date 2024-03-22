import unittest
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        mapping_letters_line = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        for word in words:
            line_num = None
            for let in word:
                let = let.lower()
                if line_num is None:
                    if let in mapping_letters_line[0]:
                        line_num = 0
                    elif let in mapping_letters_line[1]:
                        line_num = 1
                    else:
                        line_num = 2
                elif let not in mapping_letters_line[line_num]:
                    break
            else:
                res.append(word)
        return res


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        words = ["Hello", "Alaska", "Dad", "Peace"]
        result = self.solution.findWords(words)
        self.assertEqual(result, ["Alaska", "Dad"])

    def test_example_2(self):
        words = ["omk"]
        result = self.solution.findWords(words)
        self.assertEqual(result, [])

    def test_example_3(self):
        words = ["adsdf", "sfd"]
        result = self.solution.findWords(words)
        self.assertEqual(result, ["adsdf", "sfd"])


if __name__ == '__main__':
    unittest.main()
