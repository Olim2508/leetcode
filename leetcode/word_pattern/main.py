from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words_list = s.split(" ")
        if len(pattern) != len(words_list):
            return False
        hash_map = {}
        seen_words = set()
        for p, word in zip(pattern, words_list):
            if p not in hash_map:
                if word in seen_words:
                    return False
                hash_map[p] = word
                seen_words.add(word)
                continue
            if hash_map[p] != word:
                return False
        return True

    def neetcode_solution(self, pattern, s):
        words = s.split(" ")
        char_to_word = {}
        word_to_char = {}
        if len(pattern) != len(words):
            return False

        for c, w in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False
            word_to_char[w] = c
            char_to_word[c] = w

        return True


if __name__ == '__main__':
    s = Solution()
    assert s.wordPattern("abba", "dog cat cat dog") == True
    assert s.neetcode_solution("abba", "dog cat cat dog") == True

    assert s.wordPattern("abba", "dog cat cat fish") == False
    assert s.neetcode_solution("abba", "dog cat cat fish") == False

