"""
Question: https://neetcode.io/problems/binary-tree-diameter
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution class to compute the diameter of a binary tree.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum diameter.
        self.res = 0

        def dfs(root):
            # Base case: An empty node contributes a depth of 0.
            if not root:
                return 0
            # Recursively compute the depth of the left subtree.
            left = dfs(root.left)
            # Recursively compute the depth of the right subtree.
            right = dfs(root.right)
            # Update the maximum diameter found so far.
            self.res = max(self.res, left + right)
            # Return the height of the current subtree.
            return 1 + max(left, right)

        # Begin depth-first search from the root.
        dfs(root)
        # Return the computed diameter of the tree.
        return self.res
