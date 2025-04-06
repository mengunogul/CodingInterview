"""
Question: https://neetcode.io/problems/count-connected-components
"""

from typing import List, Dict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph: Dict[int, List[int]] = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components
