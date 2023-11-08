from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        allowed_num = int(len(candyType) / 2)
        counter_map = set(candyType)
        if allowed_num > len(counter_map):
            return len(counter_map)
        else:
            return allowed_num

    def solution_from_net(self, candyType):
        return min(int(len(candyType) / 2), len(set(candyType)))


if __name__ == '__main__':
    s = Solution()
    assert s.distributeCandies([1, 1, 2, 2, 3, 3]) == 3
    assert s.solution_from_net([1, 1, 2, 2, 3, 3]) == 3

    assert s.distributeCandies([1, 1, 2, 3]) == 2
    assert s.solution_from_net([1, 1, 2, 3]) == 2

