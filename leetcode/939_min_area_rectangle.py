from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float("inf")
        visited: set[tuple[int, int]] = set()
        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    min_area = min(min_area, area)
            visited.add((x1, y1))
        return 0 if min_area == float("inf") else min_area  # type: ignore
