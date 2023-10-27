from collections import defaultdict
from typing import List


class Solution:
    # todo not finished
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = defaultdict(int)

        output = []
        for i in nums2:
            if i in nums2:
                hash_map[i] += 1
                if hash_map[i] > 0:
                    output.append(i)
                    hash_map[i] -= 1

        return output


if __name__ == '__main__':
    s = Solution()
    assert s.intersection([1,2,2,1], [2,2]) == [2, 2]

    assert s.intersection([4,9,5], [9,4,9,8,4]) == [9,4]
