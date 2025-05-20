"""
Question:
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value and optional children
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Determines if subRoot is a subtree of root.
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Return True if subRoot is None (an empty tree is a subtree of any tree)
        if not subRoot:
            return True
        # Return False if tree is empty.
        if not root:
            return False

        # Check if the current trees have the same structure and nodes
        if self.sameTree(root, subRoot):
            return True
        # Recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Recursively determine if two trees are identical.
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees are identical
        if not root and not subRoot:
            return True
        # If both nodes exist and values match, continue comparing children
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(
                root.right, subRoot.right
            )
        # Trees are not identical
        return False


# Entry point for testing the solution.
if __name__ == "__main__":
    # Build a binary tree from a list of values.
    def build_tree(nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            node = queue.pop(0)
            if i < len(nodes):
                left_val = nodes[i]
                if left_val is not None:
                    node.left = TreeNode(left_val)
                    queue.append(node.left)
                i += 1
            if i < len(nodes):
                right_val = nodes[i]
                if right_val is not None:
                    node.right = TreeNode(right_val)
                    queue.append(node.right)
                i += 1
        return root

    # Construct trees and check if one is a subtree of the other.
    root = build_tree([1, 2, 3, 4, 5])
    subRoot = build_tree([2, 4, 5])

    sol = Solution()
    print(sol.isSubtree(root, subRoot))
