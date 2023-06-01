
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
    # def preorder(root):
    #     return [root.val] + preorder(root.left) + preorder(root.right)

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


if __name__ == "__main__":
    root = TreeNode(3)
    child = TreeNode(1)
    child.right = TreeNode(2)
    root.left = child
    root.right = TreeNode(4)
    # output: [1, 2, 3, 4]


    i_t = InOrderTraversal()
    print(i_t.inorder_traversal(root))
