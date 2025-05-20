"""
Question: https://neetcode.io/problems/climbing-stairs
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # Edge case: for 0 or 1 step, there's only one way.
        if n <= 1:
            return 1

        # Using descriptive variable names for clarity.
        prev, curr = 1, 1

        # Build the solution from smaller subproblems.
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr
