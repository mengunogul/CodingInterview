import heapq
from typing import List, Tuple


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calculate_distance(point1, point2):
            return sum([abs(x1 - x2) for x1, x2 in zip(point1, point2)])

        n = len(points)
        total_cost = 0
        visited = {0}
        min_heap: List[Tuple[int, int]] = []
        # Push all edges from starting point (index 0)
        for j in range(1, n):
            heapq.heappush(min_heap, (calculate_distance(points[0], points[j]), j))

        while len(visited) < n:
            cost, j = heapq.heappop(min_heap)
            if j in visited:
                continue
            visited.add(j)
            total_cost += cost
            # Add new edges from the newly added point
            for k in range(n):
                if k not in visited:
                    heapq.heappush(
                        min_heap, (calculate_distance(points[j], points[k]), k)
                    )

        return total_cost
