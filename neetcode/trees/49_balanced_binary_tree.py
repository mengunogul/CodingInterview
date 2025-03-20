"""
Question: https://neetcode.io/problems/balanced-binary-tree

This implementation checks if a binary tree is height-balanced using a recursive DFS approach.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Return True if the binary tree is height-balanced; otherwise, return False."""
        return self._height(root) != -1

    def _height(self, node: Optional[TreeNode]) -> int:
        """
        Compute the height of the tree rooted at 'node'.
        Return -1 immediately if a subtree is unbalanced.
        """
        if node is None:
            return 0

        left_height = self._height(node.left)
        if left_height == -1:
            return -1  # Left subtree is unbalanced

        right_height = self._height(node.right)
        if right_height == -1:
            return -1  # Right subtree is unbalanced

        if abs(left_height - right_height) > 1:
            return -1  # Current node is unbalanced

        return max(left_height, right_height) + 1
