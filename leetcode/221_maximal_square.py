from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        max_side = 0

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == "0":
                    continue
                if row == 0 or col == 0:
                    max_side = max(max_side, int(matrix[row][col]))
                    continue

                left = int(matrix[row][col - 1])
                right = int(matrix[row - 1][col])
                cross = int(matrix[row - 1][col - 1])
                min_side = min(left, right, cross)

                matrix[row][col] = str(min_side + 1)
                max_side = max(max_side, min_side + 1)

        return max_side * 2 if max_side != 0 else 0
