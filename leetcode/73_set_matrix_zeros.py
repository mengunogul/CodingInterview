from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rows_zero = set()
        cols_zero = set()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows_zero.add(r)
                    cols_zero.add(c)

        for r in rows_zero:
            for col in range(COLS):
                matrix[r][col] = 0

        for c in cols_zero:
            for row in range(ROWS):
                matrix[row][c] = 0
