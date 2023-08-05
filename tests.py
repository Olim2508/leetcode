from main import *
from nodes import *


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


def test_merge_two_sorted_lists():
    """
    list1 = [1,2,4], list2 = [1,3,4]
    output - [1,1,2,3,4,4]
    """

    list_1 = ListNode(1)
    node_1 = ListNode(2)
    list_1.next = node_1
    node_1.next = ListNode(4)

    list_2 = ListNode(1)
    node_2 = ListNode(3)
    list_2.next = node_1
    node_2.next = ListNode(4)
    s = MergeTwoSortedListSolution()
    res = s.mergeTwoLists(list_1, list_2)
    print(res)


def test_simplify_path():
    list_1 = ListNode(1)
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(3)

    list_1.next = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    s = DeleteDuplicatesSolution()
    res = s.deleteDuplicates(list_1)
    # print(res)


def test_max_depth():
    s = MaxDepthSolution()
    inpt = "(1+(2*3)+((8)/4))+1"
    res = s.maxDepth(inpt)
    assert res == 3

    inpt = "(1)+((2))+(((3)))"
    res = s.maxDepth(inpt)
    assert res == 3


def test_min_length():
    s = MinLengthSolution()
    inpt = "ABFCACDB"
    res = s.minLength(inpt)
    assert res == 2

    inpt = "ACBBD"
    res = s.minLength(inpt)
    assert res == 5


def test_is_palindrome():
    list_1 = ListNode(1)
    node_1 = ListNode(2)
    node_2 = ListNode(2)
    node_3 = ListNode(1)

    list_1.next = node_1
    node_1.next = node_2
    node_2.next = node_3

    s = IsPalindromeLinkedListSolution()
    res = s.isPalindrome(list_1)
    assert res


def test_is_power_of_two():
    s = IsPowerOfTwoSolution()
    # solution 1
    n = 15
    res = s.isPowerOfTwo(n)
    assert not res
    n = 8
    res = s.isPowerOfTwo(n)
    assert res

    # solution 2
    n = 15
    res = s.solution(n)
    assert not res
    n = 8
    res = s.solution(n)
    assert res

    # solution 3
    n = 15
    res = s.solution_from_web(n)
    assert not res
    n = 8
    res = s.solution_from_web(n)
    assert res


# def test_first_unique_char():
#     s = FirstUniqCharSolution()
#     st = "loveleetcode"
#     res = s.firstUniqChar(st)
#     print(res)
#     assert res == 2

    # st = "leetcode"
    # res = s.firstUniqChar(st)
    # assert res == 0

def test_backspace_compare():
    s = BackSpaceCompareSolution()
    # solution 1
    first_s, second_s = "y#fo##f", "y#f#o##f"
    res = s.backspaceCompare(first_s, second_s)
    assert res

    first_s, second_s = "ab#c", "ad#c"
    res = s.backspaceCompare(first_s, second_s)
    assert res

    first_s, second_s = "ab##", "c#d#"
    res = s.backspaceCompare(first_s, second_s)
    assert res

    first_s, second_s = "a#c", "b"
    res = s.backspaceCompare(first_s, second_s)
    assert not res


def test_count_students():
    s = CountStudentsSolution()

    students = [1, 1, 0, 0]
    sandwiches = [0, 1, 0, 1]
    res = s.countStudents(students, sandwiches)
    assert res == 0

    # students = [1,1,1,0,0,1]
    # sandwiches = [1,0,0,0,1,1]
    # res = s.countStudents(students, sandwiches)
    # assert res == 3


def test_recent_counter():
    obj = RecentCounter()
    res = obj.ping(1)
    assert res == 1

    res = obj.ping(100)
    assert res == 2

    res = obj.ping(3001)
    assert res == 3

    res = obj.ping(3002)
    assert res == 3
