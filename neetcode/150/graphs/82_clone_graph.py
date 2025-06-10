"""
Question: https://neetcode.io/problems/clone-graph
"""

# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        self.cloned: dict[
            Node, Node
        ] = {}  # use a dictionary mapping original node to clone

        def dfs(node: Optional["Node"]) -> Optional["Node"]:
            if not node:
                return None
            if node in self.cloned:
                return self.cloned[node]
            clone = Node(node.val, [])
            self.cloned[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
