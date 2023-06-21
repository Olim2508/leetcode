
from typing import List, Optional, Union


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
            if dic[s[right]] < left:  # If the character is in the dictionary but its index is before the current substring
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
