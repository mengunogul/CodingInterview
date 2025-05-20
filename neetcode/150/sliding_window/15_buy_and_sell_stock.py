"""
Question: https://neetcode.io/problems/buy-and-sell-crypto

This module provides a solution to the "buy and sell stock" problem (or crypto),
where the goal is to determine the maximum profit that can be achieved by buying
on one day and selling on another later day.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate the maximum profit possible by buying and selling once.

        The function iterates over the list of prices, maintaining the minimum
        price seen so far and updating the maximum profit accordingly.

        :param prices: List of prices (integers) representing the cost on each day.
        :return: Maximum profit achievable.
        """
        if not prices:
            return 0

        min_price: int = prices[0]
        max_profit: int = 0

        for price in prices:
            # Update max_profit if selling at current price gives higher profit.
            max_profit = max(max_profit, price - min_price)
            # Update the minimum price seen so far.
            min_price = min(min_price, price)

        return max_profit


if __name__ == "__main__":
    sol = Solution()
    prices: List[int] = [10, 1, 5, 6, 7, 1]
    result: int = sol.maxProfit(prices)
    print("Maximum profit:", result)
