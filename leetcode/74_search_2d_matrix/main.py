import unittest
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            row = matrix[mid]

            if row[0] <= target <= row[-1]:
                l_row, r_row = 0, len(row) - 1
                while l_row <= r_row:
                    mid_r = (l_row + r_row) // 2
                    if row[mid_r] < target:
                        l_row = mid_r + 1
                    elif row[mid_r] > target:
                        r_row = mid_r - 1
                    else:
                        return True
                return False
            elif row[-1] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        result = self.solution.searchMatrix(matrix, target)
        self.assertTrue(result)

    def test_example_2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        result = self.solution.searchMatrix(matrix, target)
        self.assertFalse(result)

    # def test_example_3(self):
    #     matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    #     target = 3
    #     result = self.solution.searchMatrix(matrix, target)
    #     self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
