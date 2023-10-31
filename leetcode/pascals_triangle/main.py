from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows + 1):
            sub_arr = []
            for j in range(i):
                if j == 0 or j + 1 == i:
                    sub_arr.append(1)
                else:
                    last_arr = res[-1]
                    val = last_arr[j] + last_arr[j - 1]
                    sub_arr.append(val)
            res.append(sub_arr)
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.generate(3) == [[1], [1, 1], [1, 2, 1]]

    assert s.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    assert s.generate(1) == [[1]]
