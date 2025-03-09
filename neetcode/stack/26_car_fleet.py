"""
Question: https://neetcode.io/problems/car-fleet
This module solves the Car Fleet problem from Neetcode.
It calculates the number of car fleets that will reach the target.
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Calculate the number of car fleets that will arrive at the target.

        Args:
            target (int): The destination position.
            position (List[int]): Starting positions of the cars.
            speed (List[int]): Speeds of the cars.

        Returns:
            int: The number of car fleets.
        """
        # Pair each car's position with its speed.
        pair = [(p, s) for p, s in zip(position, speed)]
        # Sort cars by position in descending order (cars closest to target first).
        pair.sort(reverse=True)
        # Stack to maintain the time it takes for each fleet to reach the target.
        stack = []
        # Process each car in the sorted order.
        for p, s in pair:  # Reverse Sorted Order: car nearest to target comes first.
            # Calculate time required to reach the target.
            travel_time = (target - p) / s
            stack.append(travel_time)
            # Merge fleets: if the current car's travel time is less than or equal to the previous fleet's,
            # it joins that fleet. Remove the current travel time as it's absorbed.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


if __name__ == "__main__":
    sol = Solution()
    # Run an example test case.
    result = sol.carFleet(target=10, position=[1, 4], speed=[3, 2])
    print(result)
