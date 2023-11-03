from collections import Counter
from typing import List


class Solution:
    # brute force solution using O(n) space with O(n) time
    def singleNumber(self, nums: List[int]) -> int:
        seen_nums = Counter(nums)
        for key, value in seen_nums.items():
            if value == 1:
                return key

    def gpt_solution(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.singleNumber([2, 2, 1]) == 1
    assert s.gpt_solution([2, 2, 1]) == 1

    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
    assert s.gpt_solution([4, 1, 2, 1, 2]) == 4
    assert s.gpt_solution([1, 1, 3, 4, 4]) == 3
