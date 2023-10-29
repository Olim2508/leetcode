from collections import defaultdict, Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        counter_map = Counter(s)
        res = 0
        odd_found = False
        for count in counter_map.values():
            if count % 2 == 0:
                res += count
            else:
                if not odd_found:
                    res += count
                    odd_found = True
                    continue
                if count > 1:
                    res += count - 1
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.longestPalindrome("abccccdd") == 7  # dccaccd

    assert s.longestPalindrome("a") == 1

    assert s.longestPalindrome("cbbabbddd") == 7

