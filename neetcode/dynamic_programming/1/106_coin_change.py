"""
This module implements a solution for the Coin Change problem using DFS with caching.
The DFS method recursively explores coin combinations while pruning redundant paths.
"""

from typing import List, Dict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int | float:
        """
        Returns the minimum number of coins required to form the given amount.
        Uses a depth-first search (DFS) approach with caching to reduce redundant computations.

        Parameters:
            coins (List[int]): Available coin denominations.
            amount (int): The target amount to form.

        Returns:
            int: Minimum number of coins needed, or -1 if it is not possible.
        """
        self.number_of_change = float("inf")
        self.cache: Dict[int, int] = {}
        coins.sort()  # Sort coins for an early break in the loop when the coin value exceeds the remaining amount

        def dfs(iter, left_amount):
            # iter: current number of coins used so far
            # left_amount: remaining amount to be formed
            # If the current state has been reached before with a lower or equal number of coins, skip further work.
            if left_amount in self.cache and self.cache[left_amount] <= iter:
                return
            self.cache[left_amount] = iter

            # Base case: If left_amount is exactly 0, update the minimum coin count.
            if left_amount == 0:
                self.number_of_change = min(self.number_of_change, iter)
                return
            # Prune paths that already use more coins than the best solution found so far.
            if iter >= self.number_of_change:
                return

            # Explore further coin choices
            for coin in coins:
                # Since coins are sorted, break early if the coin exceeds the remaining amount.
                if coin > left_amount:
                    break
                dfs(iter + 1, left_amount - coin)

        dfs(0, amount)
        return -1 if self.number_of_change == float("inf") else self.number_of_change


if __name__ == "__main__":
    sol = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(sol.coinChange(coins, amount))
