import math
import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        if len(timeSeries) == 1:
            return duration
        for i in range(len(timeSeries) - 1):
            a = duration + timeSeries[i] - 1
            print("timeSeries[i]", timeSeries[i], "duration", duration, "a", a)
            if a < timeSeries[i + 1]:
                total += duration
                if i == len(timeSeries) - 2:
                    total += duration
            else:
                total += timeSeries[i + 1] - timeSeries[i]
                if i == len(timeSeries) - 2:
                    total += duration
        return total

    def gpt_sol(self, timeSeries, duration):
        total_poisoned = 0
        n = len(timeSeries)

        if n == 0:
            return 0

        for i in range(n - 1):
            current_attack = timeSeries[i]
            next_attack = timeSeries[i + 1]

            poisoned_duration = min(duration, next_attack - current_attack)
            total_poisoned += poisoned_duration

        # Add the duration of the last attack
        total_poisoned += duration

        return total_poisoned


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        timeSeries = [1, 4]
        duration = 2
        result = self.solution.findPoisonedDuration(timeSeries, duration)
        self.assertEqual(result, 4)
        result = self.solution.gpt_sol(timeSeries, duration)
        self.assertEqual(result, 4)

    def test_example_2(self):
        timeSeries = [1, 2]
        duration = 2
        result = self.solution.findPoisonedDuration(timeSeries, duration)
        self.assertEqual(result, 3)
        result = self.solution.gpt_sol(timeSeries, duration)
        self.assertEqual(result, 3)

    def test_example_3(self):
        timeSeries = [1, 2, 3, 4, 5]
        duration = 5
        result = self.solution.findPoisonedDuration(timeSeries, duration)
        self.assertEqual(result, 9)
        result = self.solution.gpt_sol(timeSeries, duration)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
