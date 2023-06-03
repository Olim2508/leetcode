
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

