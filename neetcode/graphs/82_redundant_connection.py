"""
Question: https://neetcode.io/problems/redundant-connection
"""

from typing import List, Dict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    return True
            return False

        graph: Dict[int, List[int]] = {}
        for u, v in edges:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)

            visited: set = set()
            if dfs(u, -1):
                return [u, v]
        return []
