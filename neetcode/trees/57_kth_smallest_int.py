"""
Question: https://neetcode.io/problems/kth-smallest-integer-in-bst
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def dfs(node):
            if not node:
                return
            else:
                dfs(node.left)
                values.append(node.val)
                dfs(node.right)

        dfs(root)
        return values[k - 1]


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
    nodes = [2, 1, 3]

    # Build the binary tree.
    root = build_tree(nodes)  # type:ignore
    k = 1
    solution = Solution()
    print(solution.kthSmallest(root, k))  # type:ignore


if __name__ == "__main__":
    main()
