import unittest
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    stack.append(temperatures[j])
                    res[i] += len(stack)
                    stack = []
                    break
                else:
                    stack.append(temperatures[j])
            else:
                stack = []
        return res

    def neetcode_sol(self, temperatures):
        res = [0] * len(temperatures)
        stack = [] # pair [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        output = [1, 1, 4, 2, 1, 1, 0, 0]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, output)
        result_2 = self.solution.neetcode_sol(temperatures)
        self.assertEqual(result_2, output)

    def test_example_2(self):
        temperatures = [30, 40, 50, 60]
        output = [1, 1, 1, 0]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, output)
        result_2 = self.solution.neetcode_sol(temperatures)
        self.assertEqual(result_2, output)

    def test_example_3(self):
        temperatures = [30, 60, 90]
        output = [1, 1, 0]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, output)
        result_2 = self.solution.neetcode_sol(temperatures)
        self.assertEqual(result_2, output)

    def test_example_4(self):
        temperatures = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
        output = [3, 1, 1, 2, 1, 1, 0, 1, 1, 0]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, output)
        result_2 = self.solution.neetcode_sol(temperatures)
        self.assertEqual(result_2, output)


if __name__ == '__main__':
    unittest.main()
