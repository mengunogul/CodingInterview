from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Initialize with the cost of the last two steps.
        one, two = cost[-2], cost[-1]
        for i in range(len(cost) - 3, -1, -1):
            # Calculate the minimum cost for the current step.
            cur = cost[i] + min(one, two)
            one, two = cur, one
        # Return the minimum cost to climb beyond the first step.
        return min(one, two)


if __name__ == "__main__":
    cost = [10, 15, 20]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost))
