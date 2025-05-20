"""
Question: https://neetcode.io/problems/search-2d-matrix
This module implements a solution for searching a target value in a 2D matrix.
The approach identifies the row where the target may exist based on the last element,
then applies binary search within that row.
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search for a target value in a 2D matrix.

        The matrix has the following properties:
        - Integers in each row are sorted in ascending order.
        - The first integer of each row is greater than the last integer of the previous row.

        Args:
            matrix (List[List[int]]): 2D list of integers representing the matrix.
            target (int): The integer value to search for.

        Returns:
            bool: True if target is found, False otherwise.
        """
        # Identify the row where the target may exist based on its last element.
        r = 0
        for idx, row in enumerate(matrix):
            # If target is less than or equal to the last element in the row, this row is a candidate.
            if target <= row[-1]:
                r = idx
                break

        # Apply binary search on the identified row.
        low = 0
        high = len(matrix[r]) - 1
        while low <= high:
            mid = (low + high) // 2  # Find the middle index.
            if matrix[r][mid] == target:
                return True  # Target found.
            elif matrix[r][mid] < target:
                low = mid + 1  # Target is in the right half.
            else:
                high = mid - 1  # Target is in the left half.
        return False  # Target is not present in the candidate row.


if __name__ == "__main__":
    matrix = [[1], [3]]
    target = 1
    solution = Solution()
    print(solution.searchMatrix(matrix, target))
