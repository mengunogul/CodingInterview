from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS = len(isConnected)
        COLS = len(isConnected[0])

        graph: dict[int, List[int]] = {i: [] for i in range(ROWS)}

        for r in range(ROWS):
            for c in range(COLS):
                if isConnected[r][c] == 1 and r != c:
                    graph[r].append(c)

        visited = set()
        q: deque = deque()
        provinces = 0
        for i in range(ROWS):
            if i not in visited:
                q.append(i)
                while q:
                    cur_neighbor = q.popleft()
                    if cur_neighbor in visited:
                        continue
                    visited.add(cur_neighbor)
                    for neighbor in graph[cur_neighbor]:
                        q.append(neighbor)
                provinces += 1
        return provinces
