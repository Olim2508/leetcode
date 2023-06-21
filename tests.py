from main import *


def test_length_of_longest_substring():
    s = "abcabcbb"
    assert length_of_longest_substring(s) == 3
    s = "bbbbb"
    assert length_of_longest_substring(s) == 1
    s = "pwwkew"
    assert length_of_longest_substring(s) == 3
    s = ""
    assert length_of_longest_substring(s) == 0
    s = " "
    assert length_of_longest_substring(s) == 1
    s = "au"
    assert length_of_longest_substring(s) == 2


def test_max_profit():
    """
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
    """
    prices = [7, 1, 5, 3, 6, 4]
    assert max_profit(prices) == 5
    prices = [7, 6, 4, 3, 1]
    assert max_profit(prices) == 0


def test_remove_element():
    nums, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
    assert remove_element(nums, val) == 5


def test_next_greater_element():
    s = NextGreaterElementSolution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    res = s.next_greater_element(nums1, nums2)
    assert res == [-1, 3, -1]

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    res = s.next_greater_element(nums1, nums2)
    assert res == [3, -1]


def test_next_greater_element_optimal():
    s = NextGreaterElementSolution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    res = s.next_greater_element_optimal(nums1, nums2)
    assert res == [-1, 3, -1]

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    res = s.next_greater_element_optimal(nums1, nums2)
    assert res == [3, -1]


def test_baseball_game():
    b = BaseBallGame()
    ops = ["5", "2", "C", "D", "+"]
    res = b.calPoints(ops)
    assert res == 30

    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    res = b.calPoints(ops)
    assert res == 27
