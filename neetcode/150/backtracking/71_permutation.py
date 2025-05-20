"""
Question: https://neetcode.io/problems/permutations
This module generates all possible permutations of a given list of integers.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible permutations of the input array.

        Args:
            nums (List[int]): List of distinct integers.

        Returns:
            List[List[int]]: List of all possible permutations.
        """
        permutations = []

        def backtrack(permutation: List[int], candidates: List[int]):
            """
            Build permutations recursively.

            Args:
                permutation (List[int]): Current permutation being built.
                candidates (List[int]): Remaining numbers available for selection.
            """
            # If the permutation is complete, add a copy to our results
            if len(permutation) == len(nums):
                permutations.append(permutation[:])
                return
            # If no candidates remain, stop recursing
            if not candidates:
                return

            # Try each candidate as the next element in the permutation
            for i, num in enumerate(candidates):
                # Add the current number to our permutation
                permutation.append(num)

                # Create a new candidates list without the current number
                remaining = (
                    candidates[:i] + candidates[i + 1 :]
                )  # More efficient slicing

                # Recurse to build the rest of the permutation
                backtrack(permutation, remaining)

                # Backtrack to try other possibilities
                permutation.pop()

        # Start with an empty permutation and all numbers as candidates
        backtrack([], nums)
        return permutations


if __name__ == "__main__":
    sol = Solution()
    # Example: Generate all permutations of [1, 2, 3]
    print(sol.permute([1, 2, 3]))
