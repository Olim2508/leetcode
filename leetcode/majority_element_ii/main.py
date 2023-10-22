from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter_map = {}
        res_list = set()
        for n in nums:
            if n in counter_map:
                counter_map[n] += 1
            else:
                counter_map[n] = 1
            if counter_map[n] > (len(nums) / 3) and n not in res_list:
                res_list.add(n)

        return list(res_list)


if __name__ == '__main__':
    s = Solution()
    assert s.majorityElement([1, 2]) == [1, 2]

    assert s.majorityElement([3, 2, 3]) == [3]

    assert s.majorityElement([1]) == [1]

