from collections import defaultdict
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums_1_counter = self.count_numbers(nums1)
        nums_2_counter = self.count_numbers(nums2)

        for k, v in nums_1_counter.items():
            for k_2, v_2 in nums_2_counter.items():
                if k == k_2:
                    times = [k] * min(v, v_2)
                    res += times
        return res

    def count_numbers(self, nums):
        nums_counter = defaultdict(int)
        for num in nums:
            nums_counter[num] += 1
        return nums_counter


if __name__ == '__main__':
    s = Solution()
    assert s.intersection([1,2,2,1], [2,2]) == [2, 2]

    assert s.intersection([4,9,5], [9,4,9,8,4]) == [9,4]
