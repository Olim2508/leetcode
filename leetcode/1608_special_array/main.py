import unittest
from collections import defaultdict
from typing import List

# todo not fully finished yet


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        res = -1
        nums.sort()
        for i in range(len(nums), 0, -1):
            # print("i", i)
            l, r = 0, len(nums) - 1
            is_found = False
            while l <= r:
                mid = (l + r) // 2
                print("nums[mid]---", nums[mid], "i--", i)
                if nums[mid] < i:
                    l = mid + 1
                elif nums[mid] >= i:
                    r = mid - 1
                    if len(nums[mid:]) == i:
                        res = i
                        break
                else:
                    if len(nums[mid:]) == i:
                        res = i
                    break

        return res


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_0(self):
        nums = [3, 5, 2, 7]
        result = self.solution.specialArray(nums)
        self.assertEqual(result, 3)

    def test_example_1(self):
        nums = [3, 5]
        result = self.solution.specialArray(nums)
        self.assertEqual(result, 2)

    def test_example_2(self):
        nums = [0, 0]
        result = self.solution.specialArray(nums)
        self.assertEqual(result, -1)

    def test_example_3(self):
        nums = [0, 4, 3, 0, 4]
        result = self.solution.specialArray(nums)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
