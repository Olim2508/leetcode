from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomnote_counter = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for s in ransomnote_counter:
            if magazine_count.get(s) and ransomnote_counter[s] <= magazine_count[s]:
                continue
            else:
                return False
        return True

    def public_solution(self, ransomNote, magazine):
        ran = Counter(ransomNote)
        mag = Counter(magazine)

        if ran & mag == ran:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    assert s.canConstruct("a", "b") == False
    assert s.public_solution("a", "b") == False

    assert s.canConstruct("aa", "ab") == False
    assert s.public_solution("aa", "ab") == False

    assert s.canConstruct("aa", "aab") == True
    assert s.public_solution("aa", "aab") == True
