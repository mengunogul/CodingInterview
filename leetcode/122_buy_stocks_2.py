from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = inf
        profit = 0

        for price in prices[:]:
            if price < buy:
                buy = price
            else:
                profit += price-buy
                buy = price

        return profit
