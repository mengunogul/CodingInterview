from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights += [-1]
        stack: List[List[int]] = []
        res = 0

        for height in heights:
            step = 0
            while stack and stack[-1][1] >= height:
                w, h = stack.pop()
                step += w
                area = step * h
                res = max(res, area)
            stack.append([step + 1, height])
        return res
