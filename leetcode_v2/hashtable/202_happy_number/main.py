import unittest
from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        is_happy = True
        while is_happy:
            sum = self.calc_sum(n)
            if sum == 1:
                return True
            if sum in hash_set:
                is_happy = False
            else:
                hash_set.add(sum)
            n = sum
        return False

    def calc_sum(self, n):
        sum = 0
        for dig in str(n):
            sum += int(dig) ** 2
        return sum


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.isHappy(19)
        self.assertEqual(result, True)

    # def test_example_2(self):
    #     result = self.solution.isHappy(2)
    #     self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
