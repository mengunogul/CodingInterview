"""
Question: https://neetcode.io/problems/combination-target-sum-ii
This module generates all unique combinations from candidates that sum up to the target.
Each candidate may only be used once and duplicate combinations are avoided.
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations in candidates where the candidate numbers sum to target.
        Each candidate can only be used once in each combination.

        Args:
            candidates (List[int]): A list of candidate numbers.
            target (int): Target sum for the combinations.

        Returns:
            List[List[int]]: A list of unique combinations that sum to target.
        """
        combinations = set()  # Use a set to avoid duplicate combinations
        candidates.sort()  # Sort to simplify duplicate checking

        def backtrack(idx: int, current: List[int]) -> None:
            total = sum(current)  # Calculate current combination sum
            # If we hit the target, add current combination (as a tuple) for deduplication.
            if total == target:
                combinations.add(tuple(current))
                return
            # If the sum exceeds target or no more candidates remain, stop exploring.
            if total > target or idx == len(candidates):
                return

            # Case 1: Include the candidate at the current index.
            current.append(candidates[idx])
            backtrack(idx + 1, current)
            current.pop()  # Backtrack: Remove the candidate.

            # Case 2: Exclude the candidate at the current index.
            backtrack(idx + 1, current)

        backtrack(0, [])
        # Convert each tuple in the set back to a list.
        return [list(comb) for comb in combinations]


if __name__ == "__main__":
    solution = Solution()
    # Print unique combinations that sum up to 8.
    print(solution.combinationSum2([9, 2, 2, 4, 6, 1, 5], 8))
