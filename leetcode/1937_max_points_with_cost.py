from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Initialize dp with the first row's points
        dp = points[0]
        # Process each subsequent row in the matrix
        for row in points[1:]:
            n = len(row)  # number of columns in the row
            left = [0] * n  # will hold best dp values computed from left to right
            right = [0] * n  # will hold best dp values computed from right to left

            # Left-to-right pass:
            # At the very first column, the best value is just dp[0]
            left[0] = dp[0]
            for j in range(1, n):
                # For current column j, either:
                # - Continue from the left column (left[j-1] - 1) which deducts a cost of 1,
                # - Or use the current dp[j] directly.
                # This computes the maximum value reachable from the left, taking the movement cost into account.
                left[j] = max(left[j - 1] - 1, dp[j])

            # Right-to-left pass:
            # Start from the last column where the best value is dp[-1]
            right[-1] = dp[-1]
            for j in range(n - 2, -1, -1):
                # For current column j, either:
                # - Continue from the right column (right[j+1] - 1) with penalty,
                # - Or take dp[j] directly.
                # This computes the maximum value reachable from the right.
                right[j] = max(right[j + 1] - 1, dp[j])

            # For the current row, compute the new dp values.
            # For each column, add the row point to the best reachable value from either left or right.
            newdp = [0] * n
            for j in range(n):
                newdp[j] = row[j] + max(left[j], right[j])
            dp = newdp  # Update dp for processing the next row.

        # After processing all rows, return the maximum value from the final row.
        return max(dp)


if __name__ == "__main__":
    points = [[1, 5], [2, 3], [4, 2]]
    sol = Solution()
    print(sol.maxPoints(points))
