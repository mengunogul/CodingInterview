"""
Question: https://neetcode.io/problems/min-cost-climbing-stairs
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Starting from the third-to-last element down to the first
        for i in range(len(cost) - 3, -1, -1):
            # Update cost at index i by adding the minimum cost between the next two steps
            cost[i] += min(cost[i + 1], cost[i + 2])
        # Return the minimum cost between the first two indices, representing the optimal start
        return min(cost[0], cost[1])


if __name__ == "__main__":
    # Example usage with a predefined cost array
    cost = [1, 2, 1, 2, 1, 1, 1]
    solution = Solution()
    print(solution.minCostClimbingStairs(cost))
