"""
Question: https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree

This script implements the Lowest Common Ancestor algorithm for a Binary Search Tree,
and provides utilities to build and search within a binary tree.
"""

from collections import deque
from typing import Optional, List


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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        order: List[List[int]] = []

        def dfs(level, node):
            if not node:
                return
            if len(order) <= level:
                order.append([node.val])
            elif len(order) > level:
                order[level].append(node.val)

            dfs(level + 1, node.left)
            dfs(level + 1, node.right)

        dfs(0, root)
        return [level[-1] for level in order]


def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list representation.
    """
    if not nodes:
        return None
    if nodes[0] is None:  # Added guard for first element
        return None
    root = TreeNode(nodes[0])
    queue: deque[TreeNode] = deque([root])  # Annotate queue with TreeNode type
    index = 1
    while queue and index < len(nodes):
        node = queue.popleft()  # Efficiently dequeue the next node
        if index < len(nodes):
            left_val = nodes[index]
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            index += 1
        if index < len(nodes):
            right_val = nodes[index]
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
            index += 1
    return root


def main() -> None:
    # Initialize level-order list and search values for p and q.
    nodes = [1, 2, 3]

    # Build the binary tree.
    root = build_tree(nodes)  # type:ignore

    solution = Solution()
    print(solution.rightSideView(root))


if __name__ == "__main__":
    main()
