from typing import Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = -inf

        def dfs(root):
            if not root:
                return 0

            left_val = dfs(root.left)
            right_val = dfs(root.right)
            self.max_val = max(
                self.max_val,
                root.val,
                left_val + root.val,
                right_val + root.val,
                left_val + right_val + root.val,
            )

            return max(left_val + root.val, right_val + root.val, root.val)

        dfs(root)
        return self.max_val  # type: ignore
