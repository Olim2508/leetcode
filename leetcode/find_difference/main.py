from collections import defaultdict, Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        seen_letter_map = defaultdict(int)
        for s_let in s:
            seen_letter_map[s_let] += 1

        for t_let in t:
            if t_let in seen_letter_map:
                if seen_letter_map[t_let] == 0:
                    return t_let
                seen_letter_map[t_let] -= 1
            else:
                return t_let

    def gpt_solution(self, s, t):
        s_count = Counter(s)
        t_count = Counter(t)

        for letter, count in t_count.items():
            if s_count[letter] != count:
                return letter


if __name__ == '__main__':
    s = Solution()
    assert s.findTheDifference("abcd", "abcde") == "e"
    assert s.gpt_solution("abcd", "abcde") == "e"

    assert s.findTheDifference("a", "aa") == "a"
    assert s.gpt_solution("a", "aa") == "a"

    assert s.findTheDifference("", "y") == "y"
    assert s.gpt_solution("", "y") == "y"
