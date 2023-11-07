from collections import defaultdict, Counter
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        letter_mapping = {
            "first_row": set("qwertyuiop") ^ {s.upper() for s in "qwertyuiop"},
            "second_row": set("asdfghjkl") ^ {s.upper() for s in "asdfghjkl"},
            "third_row": set("zxcvbnm") ^ {s.upper() for s in "zxcvbnm"},
        }
        for word in words:
            row = 0
            same_row = True
            for s in word:
                if not row:
                    if s in letter_mapping["first_row"]:
                        row = 1
                    elif s in letter_mapping["second_row"]:
                        row = 2
                    else:
                        row = 3
                else:
                    if row == 1 and s not in letter_mapping["first_row"]:
                        same_row = False
                        break
                    if row == 2 and s not in letter_mapping["second_row"]:
                        same_row = False
                        break
                    if row == 3 and s not in letter_mapping["third_row"]:
                        same_row = False
                        break
            if same_row:
                res.append(word)

        return res

    def gpt_sol(self, words):
        row_letters = [
            set("qwertyuiopQWERTYUIOP"),
            set("asdfghjklASDFGHJKL"),
            set("zxcvbnmZXCVBNM"),
        ]
        res = []
        for word in words:
            if any(all(c in row for c in word) for row in row_letters):
                res.append(word)
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
    assert s.gpt_sol(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]

    assert s.findWords(["omk"]) == []

