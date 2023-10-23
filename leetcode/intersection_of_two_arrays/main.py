from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    def gpt_solution(self, nums1, nums2):
        unique_set = set(nums1)

        res = []

        for n in nums2:
            if n in unique_set:
                res.append(n)
                unique_set.remove(n)
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.intersection([1,2,2,1], [2,2]) == [2]
    assert s.gpt_solution([1,2,2,1], [2,2]) == [2]

    assert s.intersection([4,9,5], [9,4,9,8,4]) == [9,4]
    assert s.gpt_solution([4,9,5], [9,4,9,8,4]) == [9,4]
