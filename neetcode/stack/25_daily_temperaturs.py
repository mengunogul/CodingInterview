"""
Question: https://neetcode.io/problems/daily-temperatures

This module provides an optimized solution for the Daily Temperatures problem.
For each day in the input, the solution computes how many days one has to wait
until a warmer temperature. It uses a stack-based approach for an efficient O(n) solution.
"""

from typing import List


class Solution:
    """
    A class that implements the solution for the Daily Temperatures problem.
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        For each day, calculate the number of days until a warmer temperature occurs.

        The function uses a stack to track indices and temperatures. As we iterate
        through the temperatures, we check whether the current day's temperature is
        higher than the temperature at the top of the stack. If so, we update the result
        for that day and pop from the stack.

        :param temperatures: List of daily temperatures.
        :return: List where each position contains the number of days until a warmer temp.
        """
        # Initialize stack with the first day's index and its temperature.
        stack = [[0, temperatures[0]]]
        # Initialize results list with 0's for each day.
        res = [0] * len(temperatures)

        # Iterate over the rest of the temperatures with day indices starting at 1.
        for day, temp in enumerate(temperatures[1:], 1):
            # While there is a previous day in the stack and the current temperature is higher,
            # update the result for that day.
            while stack and temp > stack[-1][1]:
                prev_day, prev_temp = stack.pop()
                res[prev_day] = (
                    day - prev_day
                )  # Calculate how many days until a warmer temperature.
            # Push current day's index and temperature onto the stack.
            stack.append([day, temp])

        return res


if __name__ == "__main__":
    # Example usage:
    solution = Solution()
    temperatures = [30, 38, 30, 36, 35, 40, 28]
    result = solution.dailyTemperatures(temperatures)
    print("Daily temperatures result:", result)
