"""
Question: https://neetcode.io/problems/k-closest-points-to-origin
"""

from typing import List
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[self.distance(x, y), x, y] for x, y in points]
        heapq.heapify(distances)
        return [[x, y] for _, x, y in heapq.nsmallest(k, distances)]

    def distance(self, x, y):
        return math.sqrt(x**2 + y**2)
