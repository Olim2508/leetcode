import math
import re
from collections import defaultdict
from typing import List, Optional, Tuple


# 14. Longest common prefix
class CommonPrefix:
    """
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

    Input: strs = ["dog","racecar","car"]
    Output: ""
    """

    def longest_common_prefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InOrderTraversal:
    """
    Input: root = [1,null,2,3]
    Output: [1,3,2]

    Input: root = []
    Output: []
    """

    # solution from internet
    # def inorder(root):
    #     return inorder(root.left) + [root.val] + inorder(root.right)

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # To store the inorder traversal

        def inorder(node):
            if node:
                # Traverse the left subtree
                inorder(node.left)
                # Visit the current node
                result.append(node.val)
                # Traverse the right subtree
                inorder(node.right)

        inorder(root)
        return result


# 144
def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


# 3
# solution from internet
def length_of_longest_substring(s: str) -> int:
    dic = {}  # Dictionary to store characters and their indices
    left = 0  # Left pointer to track the start of the current substring
    max_len = 0  # Maximum length of the substring without repeating characters

    for right in range(len(s)):
        if s[right] not in dic:  # If the current character is not in the dictionary
            max_len = max(max_len, right - left + 1)
        else:
            if dic[
                s[right]] < left:  # If the character is in the dictionary but its index is before the current substring
                max_len = max(max_len, right - left + 1)
            else:
                left = dic[s[right]] + 1  # Update the left pointer to skip the repeated character
        dic[s[right]] = right  # Update the index of the current character in the dictionary

    return max_len


# 121. Best Time to Buy and Sell Stock
def max_profit(prices: List[int]) -> int:
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            low = mid - 1
        if guess <= item:
            high = mid + 1
    return None


# 27. Remove element
def remove_element(nums: List[int], val: int) -> int:
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            count += 1
            i += 1
    return count


# 496. Next greater element
class NextGreaterElementSolution:
    # O(n * m) time complexity - not good

    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = True
                if found and nums1[i] < nums2[j]:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
        return res

    # O(m + n) time complexity
    def next_greater_element_optimal(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {v: i for i, v in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:  # top of the stack
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1:
                stack.append(cur)
        return res


# 682. Baseball game
class BaseBallGame:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "C":
                stack.pop()
            if o == "D":
                stack.append(stack[-1] * 2)
            if o == "+":
                stack.append(stack[-1] + stack[-2])
            try:
                stack.append(int(o))
            except ValueError:
                pass
        return sum(stack)


# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeTwoSortedListSolution:
    # solution from neetcode
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next


# 83. Remove Duplicates from Sorted List
class DeleteDuplicatesSolution:
    # solution from net
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


# 1614. Maximum Nesting Depth of the Parentheses
class MaxDepthSolution:
    """inpt = '(1+(2*3)+((8)/4))+1'  outpt = 3"""

    def maxDepth(self, s: str) -> int:
        max = depth = 0
        for let in s:
            if let == "(":
                depth += 1
                if depth > max:
                    max = depth
            elif let == ")":
                depth -= 1
        return max


# 2696. Minimum String Length After Removing Substrings
class MinLengthSolution:
    """
    inpt = 'ABFCACDB'  outpt = 2
    need to remove AB or CD substring
    """

    def minLength(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if (s[i] == "B" and stack and stack[-1] == "A") or (s[i] == "D" and stack and stack[-1] == "C"):
                stack.append(s[i])
                stack.pop()
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)


# 234. Palindrome linked list
class IsPalindromeLinkedListSolution:
    # memory should be in O(1), but it is not
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]


class IsPowerOfTwoSolution:
    # solution 1
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        nth_power = float("-inf")
        res_power = self.powerFunc(n, nth_power)
        if res_power == n:
            return True
        return False

    def powerFunc(self, n, nth_power):
        i = 0
        while nth_power < n:
            nth_power = 2 ** i
            i += 1
        return nth_power

    # solution 2
    def solution(self, n):
        i = 0
        res_power = self.powerRecursion(n, i)
        if res_power == n:
            return True
        return False

    def powerRecursion(self, n, i):
        if 2 ** i < n:
            return self.powerRecursion(n, i + 1)
        return 2 ** i

    # solution 3
    def solution_from_web(self, n):
        power = 0
        temp = 0
        while temp <= n:
            temp = math.pow(2, power)
            if temp == n:
                return True
            power += 1
        return False


# class FirstUniqCharSolution:
#     def firstUniqChar(self, s: str) -> int:
#         print(s)
#         queue = {}
#         for i in range(len(s)):
#             # print(s[i])
#             if s[i] not in queue:
#                 queue[i] = 1
#             else:
#                 # del queue[i]
#                 queue[i] += 1
#         print("queue", queue)
#         return -1


# 844
class BackSpaceCompareSolution:

    # my slution
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list, t_list = [], []
        for i in s:
            if i == "#" and s_list:
                s_list.pop()
            elif i == "#":
                pass
            else:
                s_list.append(i)
        for j in t:
            if j == "#" and t_list:
                t_list.pop()
            elif j == "#":
                pass
            else:
                t_list.append(j)
        return s_list == t_list


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# todo not finished
class IncreasingSolutionBST:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        tail = dummy

        def inorder(node):
            nonlocal tail
            if not node: return
            inorder(node.left)

            tail.right = TreeNode(val=node.val)
            tail = tail.right

            inorder(node.right)

        return dummy.right


# 1700
class CountStudentsSolution:
    """
    1 - squared sandwiches
    0 - circular sandwiches
    """
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stuck_in_queue = 0
        while stuck_in_queue < len(students):
            student = students.pop(0)
            if sandwiches[0] == student:
                sandwiches.pop(0)
                stuck_in_queue = 0
            else:
                students.append(student)
                stuck_in_queue += 1
        return stuck_in_queue

    def my_solution(self, students, sandwiches):
        if not students:
            return 0
        for i in range(len(students)):
            if not any(item in students for item in sandwiches):
                return len(students)
            if students[i] == sandwiches[0]:
                students.pop(i)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
        return 0


# 933
class RecentCounter:

    def __init__(self):
        self.recent_requests = []

    def ping(self, t: int) -> int:
        self.recent_requests.append(t)
        temp = self.recent_requests
        range_req = [t - 3000, t]
        count_items_in_range = len(temp)

        in_range = False
        while not in_range:
            # starting point
            if start_in_range := (range_req[0] > temp[0]):
                temp.pop(0)
                count_items_in_range -= 1

            # ending point
            if end_in_range := (range_req[-1] > temp[-1]):
                temp.pop(-1)
                count_items_in_range -= 1

            if not start_in_range and not end_in_range:
                in_range = True
        return count_items_in_range


# 1021
class RemoveOuterParenthesisSolution:
    # my solution
    def removeOuterParentheses(self, s: str) -> str:
        if not s:
            return ""
        res = ""
        sub = []
        par_count = {
            "open_par": 0,
            "closed_par": 0,
        }
        for i in range(len(s)):
            sub.append(s[i])
            if s[i] == "(":
                par_count['open_par'] += 1
            else:
                par_count['closed_par'] += 1
            if (sub[0] == "(") and (sub[-1] == ")") and (par_count['open_par'] == par_count['closed_par']):
                sub.pop(0)
                sub.pop(-1)
                res += "".join(sub)
                sub.clear()
                par_count['open_par'] = 0
                par_count['closed_par'] = 0
        return res

    # chatgpt solution
    def solution(self, s):
        res = ""
        balance = 0  # To keep track of open and closed parentheses balance
        sub = []

        for char in s:
            if char == "(":
                balance += 1
            else:
                balance -= 1

            sub.append(char)

            if balance == 0:
                res += "".join(sub[1:-1])  # Append the inner substring excluding outer parentheses
                sub = []

        return res


# 1047
class RemoveDuplicatesSolution:
    """aababaab -> ba"""

    def removeDuplicates(self, s: str) -> str:
        if len(s) < 1:
            return s

        res_list = []
        for let in s:
            if res_list:
                if res_list[-1] != let:
                    res_list.append(let)
                else:
                    res_list.pop()
            else:
                res_list.append(let)
        return "".join(res_list)


class IsValidParenthesis:

    # from neetcode
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


# 387
class FirstUniqueCharacterSolution:

    def firstUniqChar(self, s: str) -> int:
        queue = {}
        char_order = {}
        for index, char in enumerate(s):
            if char not in queue:
                queue[char] = 1
                char_order[char] = index
            else:
                queue[char] += 1
        for k, v in queue.items():
            if v == 1:
                return char_order[k]
        return -1


class TimeRequiredSolution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        tickets_queue = tickets.copy()
        while tickets_queue[k] > 0:
            for i in range(len(tickets_queue)):
                if tickets_queue[i] > 0:
                    if i == k:
                        tickets_queue[i] -= 1
                        seconds += 1
                    else:
                        tickets_queue[i] -= 1
                        # seconds += 1
            seconds += 1
        return seconds

    def gpt_solution(self, tickets: List[int], k: int) -> int:
        seconds = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    if i == k:
                        tickets[i] -= 1
                        seconds += 1
                        if tickets[k] == 0:
                            return seconds
                    else:
                        tickets[i] -= 1
                        seconds += 1


# todo need to fix
def basic_calculator_ii(s: str) -> int:
    """3+2*2"""
    res = 0
    sign = ""
    for i in range(len(s)):
        if s[i] == "*":
            c = int(s[i - 1]) * int(s[i + 1])
            print("it is multiply", s[i], "sign", sign, "c", c, "res", res)

            if sign:
                if sign == "-":
                    res -= int(c)
                else:
                    res += int(c)
            else:
                res += int(s[i])
        elif s[i] == "/":
            c = int(s[i - 1]) // int(s[i + 1])
            if sign:
                if sign == "-":
                    res -= int(c)
                else:
                    res += int(c)
            else:
                res += int(s[i])
        elif s[i] == "-" or s[i] == "+":
            sign = s[i]
            print("it is s", s[i], "sign", sign, "res", res)
        elif s[i] == "":
            continue
        else:
            if sign:
                if sign == "-":
                    res -= int(s[i])
                else:
                    res += int(s[i])
            else:
                res += int(s[i])
            print("it is number", s[i], "sign", sign, "res", res)
    return res


def remove_duplicate_nums(nums: List[int]) -> Tuple[int, List[int]]:
    if len(nums) < 2:
        return len(nums), nums

    nums_copy = nums.copy()
    for i in range(len(nums_copy)):
        # if next num is duplicate
        if i < len(nums_copy) - 1 and nums_copy[i] == nums_copy[i + 1]:
            del nums[i + 1]
    count = len(nums)
    remaining_num = count - len(nums_copy)
    nums += ["_" for i in range(remaining_num)]
    return count, nums


def min_chips(total: int) -> int:
    chip_types = [100, 50, 25, 10, 5, 1]
    count = 0
    for chip in chip_types:
        if chip <= total:
            count += total // chip
            total = total % chip
    return count


def count_most_duplicate(string: str) -> str:
    count = 0
    count_map = defaultdict(int)
    res = None
    for char in string:
        count_map[char] += 1
        if count_map[char] > count:
            count = count_map[char]
            res = char
    return res

