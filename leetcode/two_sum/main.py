from typing import List


def two_sum_with_hash(nums, target):
    hash_map = {}
    for i, val in enumerate(nums):
        diff = target - val
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[val] = i

    return


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        return two_sum_with_hash(nums, target)


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 1, 5, 3], 4) == [1, 3]

    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]

    assert s.twoSum([3, 2, 4], 6) == [1, 2]

    assert s.twoSum([3, 3], 6) == [0, 1]
