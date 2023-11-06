from typing import List


class Solution:
    def gpt_sol(self, nums):
        n = len(nums)
        for num in nums:
            index = abs(num) - 1
            print("index", index, "num", num, "nums[index]", nums[index])
            if nums[index] > 0:
                nums[index] = -nums[index]

        result = [i + 1 for i in range(n) if nums[i] > 0]
        return result

    def my_sol(self, nums):
        res = {i for i in range(1, len(nums) + 1)}
        for num in nums:
            if num in res:
                res.remove(num)
        return list(res)


if __name__ == '__main__':
    s = Solution()
    # assert s.my_sol([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert s.gpt_sol([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]

    # assert s.my_sol([1, 1]) == [2]
