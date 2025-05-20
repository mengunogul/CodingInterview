"""
Question: https://neetcode.io/problems/network-delay-time
"""

from typing import List, Dict, Tuple
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n + 1)}
        for u, v, w in times:
            edges[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        t = 0
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            t = weight

            for neighbor_node, neighbor_weight in edges[node]:
                if neighbor_node not in visited:
                    heapq.heappush(min_heap, (weight + neighbor_weight, neighbor_node))

        return t if len(visited) == n else -1
