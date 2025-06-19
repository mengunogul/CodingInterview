"""
Module: 121_buy_sell_stock
Purpose: Provides solution to compute maximum profit from a single buy-sell transaction.
"""

from typing import List


class Solution:
    """
    Class to calculate the maximum profit from stock prices.
    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        Compute the optimal profit from a single buy and sell operation.

        :param prices: List of daily stock prices.
        :return: Maximum profit achievable.
        """
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == "__main__":
    prices = [7, 6, 4, 3, 1]
    solution = Solution()
    print(solution.maxProfit(prices))
