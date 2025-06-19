class Solution:
    def climbStairs(self, n: int) -> int:
        # Return early if there is 0 or 1 stair: only 1 way to climb.
        if n <= 1:
            return 1

        # Initialize the number of ways for step 0 and step 1.
        prev, curr = 1, 1

        # Calculate the number of ways for each subsequent stair.
        for _ in range(2, n + 1):
            # Update the previous and current number of ways.
            prev, curr = curr, prev + curr
        # Return the number of ways to reach n stairs.
        return curr


# Code execution starts here.
if __name__ == "__main__":
    solution = Solution()
    n = 5  # example input
    print(solution.climbStairs(n))
