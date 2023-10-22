from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in set(nums):
                return i

        # all_nums = {n for n in range(len(nums) + 1)}
        # missing_n = all_nums - set(nums)
        # return list(missing_n)[0]

    def solution_2(self, nums):
        return sum([i for i in range(len(nums) + 1)]) - sum(nums)


if __name__ == '__main__':
    s = Solution()
    assert s.missingNumber([3, 0, 1]) == 2

    assert s.missingNumber([0, 1]) == 2
    assert s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8

    assert s.solution_2([9,6,4,2,3,5,7,0,1]) == 8
