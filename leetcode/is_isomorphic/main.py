from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t:
            return True

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = t[i]
            elif s_map[s[i]] != t[i]:
                return False
            else:
                pass

            if t[i] not in t_map:
                t_map[t[i]] = s[i]
            elif t_map[t[i]] != s[i]:
                return False
            else:
                pass

        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isIsomorphic(s="egg", t="add") == True

    assert s.isIsomorphic(s="foo", t="bar") == False

    assert s.isIsomorphic(s="paper", t="title") == True
