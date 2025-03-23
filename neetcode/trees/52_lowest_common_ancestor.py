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
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if root.val > p.val and root.val > q.val and root.left is not None:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val and root.right is not None:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


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


def find_node(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    """
    Recursively find a node with the given value in the binary tree.
    """
    if root is None:
        return None
    if root.val == value:
        return root
    left_result = find_node(root.left, value)
    if left_result:
        return left_result
    return find_node(root.right, value)


def main() -> None:
    # Initialize level-order list and search values for p and q.
    nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p_val = 3
    q_val = 5

    # Build the binary tree.
    root = build_tree(nodes)
    if root is None:  # Added check for empty tree
        print("The tree is empty.")
        return

    # Locate nodes p and q.
    p_node = find_node(root, p_val)
    q_node = find_node(root, q_val)

    if p_node is None or q_node is None:
        print("One of the specified nodes was not found in the tree.")
        return

    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p_node, q_node)
    print(f"Lowest Common Ancestor: {lca.val}")


if __name__ == "__main__":
    main()
