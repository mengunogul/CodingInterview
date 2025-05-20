"""
Question: https://neetcode.io/problems/valid-tree
"""

from typing import List, Dict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Determines if the undirected graph forms a valid tree.
        A valid tree is acyclic and fully connected.
        Note: A tree with n nodes must have exactly n-1 edges.
        """
        # Quick check: a valid tree should have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        graph: Dict[int, List[int]] = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited: set = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    sol = Solution()
    print(sol.validTree(n, edges))
