from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex + 1):
            sub_arr = []
            for j in range(i + 1):
                if j == 0 or j + 1 == i + 1:
                    sub_arr.append(1)
                else:
                    last_arr = res[-1]
                    val = last_arr[j] + last_arr[j - 1]
                    sub_arr.append(val)
            if sub_arr:
                res.append(sub_arr)
        return res[-1]

    def gpt_solution(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []

        # Initialize two lists for the current row and the previous row
        current_row = [1] * (rowIndex + 1)
        previous_row = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                current_row[j] = previous_row[j] + previous_row[j - 1]

            # Swap current_row and previous_row for the next iteration
            current_row, previous_row = previous_row, current_row

        return previous_row


if __name__ == '__main__':
    s = Solution()
    assert s.getRow(3) == [1, 3, 3, 1]
    assert s.gpt_solution(3) == [1, 3, 3, 1]

    assert s.getRow(2) == [1, 2, 1]
    assert s.gpt_solution(2) == [1, 2, 1]

    assert s.getRow(1) == [1, 1]
    assert s.gpt_solution(1) == [1, 1]

    assert s.getRow(0) == [1]
    assert s.gpt_solution(0) == [1]
