from main import length_of_longest_substring, max_profit, remove_element


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
