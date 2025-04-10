"""
Questions: https://neetcode.io/problems/cheapest-flight-path
"""

import heapq
from typing import List, Dict, Tuple


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Build graph for all airports
        graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n)}
        for from_i, to_i, price_i in flights:
            graph[from_i].append((to_i, price_i))

        min_heap = [(0, src, 0)]  # (cost, current airport, stops)
        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)
            if node == dst:
                return cost
            if stops <= k:
                for neighbor, price in graph[node]:
                    heapq.heappush(min_heap, (cost + price, neighbor, stops + 1))
        return -1
