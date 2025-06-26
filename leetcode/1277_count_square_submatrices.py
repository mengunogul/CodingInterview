from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def get_value(row, col):
            val = matrix[row][col]

            left = matrix[row][col - 1] if col - 1 >= 0 else 0
            up = matrix[row - 1][col] if row - 1 >= 0 else 0
            cross = matrix[row - 1][col - 1] if left and up else 0

            val += min(left, up, cross)
            return val

        total_squares = 0
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] != 0:
                    val = get_value(row, col)
                    matrix[row][col] = val
                    total_squares += val
        return total_squares
