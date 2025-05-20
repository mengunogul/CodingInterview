"""
Question: https://neetcode.io/problems/eating-bananas
This module solves the Eating Bananas problem from Neetcode using binary search.
The goal is to determine the minimum eating speed such that all bananas are eaten within h hours.
"""

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Determine the minimum integer eating speed (bananas per hour) such that Koko can eat all the bananas
        in the given piles within h hours.

        Args:
            piles (List[int]): A list where each element represents the number of bananas in a pile.
            h (int): The number of hours within which all the bananas must be eaten.

        Returns:
            int: The minimum eating speed required.
        """
        # Set search bounds: minimum speed is 1 and maximum is the largest pile.
        low = 1
        high = max(piles)
        res = high  # Initialize result to the maximum possible speed.

        # Binary search to find the minimum valid speed.
        while low <= high:
            k = (low + high) // 2  # Guess the current eating speed.
            # Calculate total hours required with current speed k.
            time = sum(math.ceil(p / k) for p in piles)
            # If the hours required is within the allowed time, try a smaller speed.
            if time <= h:
                res = k
                high = k - 1
            else:
                low = k + 1  # Otherwise, increase the speed.
        return res


if __name__ == "__main__":
    solution = Solution()
    # Test case: Determine minimum eating speed for given piles and time.
    piles = [1, 4, 3, 2]
    h = 9
    result = solution.minEatingSpeed(piles, h)
    print(result)
