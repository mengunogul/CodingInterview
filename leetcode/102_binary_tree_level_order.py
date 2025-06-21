from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_mapping: dict[int, List[int]] = {}

        q: deque[tuple[int, Optional[TreeNode]]] = deque()
        q.append((0, root))
        while q:
            level, node = q.popleft()
            if node:
                cluster = level_mapping.get(level, [])
                cluster.append(node.val)
                level_mapping[level] = cluster

                if node.left:
                    q.append((level + 1, node.left))
                if node.right:
                    q.append((level + 1, node.right))

        return list(level_mapping.values())
