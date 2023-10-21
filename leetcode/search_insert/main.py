from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        low = 0
        high = len(nums) - 1
        pos_index = 0

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = pos_index = mid + 1
            else:
                high = mid - 1

        return pos_index


if __name__ == '__main__':
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2

    assert s.searchInsert([1, 3, 5, 6], 2) == 1

    assert s.searchInsert([1, 3, 5, 6], 7) == 4

    assert s.searchInsert([1, 3, 5, 6], 0) == 0

    assert s.searchInsert([1, 3], 2) == 1
