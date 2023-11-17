import unittest
from collections import defaultdict
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_arr = []
        for c in s:
            if self.is_alpha_num(c):
                alpha_arr.append(c.lower())
        left, right = 0, len(alpha_arr) - 1
        while left < right:
            if alpha_arr[left] == alpha_arr[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
        return True

    def is_alpha_num(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9")
                )

    def gpt_sol(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "A man, a plan, a canal: Panama"
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, True)
        result_2 = self.solution.gpt_sol(s)
        self.assertEqual(result_2, True)

    def test_example_2(self):
        s = "race a car"
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, False)

    def test_example_3(self):
        s = " "
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
