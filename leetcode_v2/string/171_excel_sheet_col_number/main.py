import math
import unittest
from typing import List

import string


class Solution:

    def titleToNumber(self, columnTitle: str) -> int:
        let_map = {}
        for let, num in zip(string.ascii_uppercase, range(1, 27)):
            let_map[let] = num
        len_col = len(columnTitle)
        res = 0
        for col in columnTitle:
            col_num = let_map[col]
            res += col_num * (26 ** (len_col - 1))
            len_col -= 1
        return res




class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        columnTitle = "A"
        result = self.solution.titleToNumber(columnTitle)
        self.assertEqual(result, 1)

    def test_example_2(self):
        columnTitle = "AB"
        result = self.solution.titleToNumber(columnTitle)
        self.assertEqual(result, 28)

    def test_example_3(self):
        columnTitle = "ZY"
        result = self.solution.titleToNumber(columnTitle)
        self.assertEqual(result, 701)


if __name__ == '__main__':
    unittest.main()
