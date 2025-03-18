class Solution:
    def divisorGame(self, n: int) -> bool:
        # Returns True if n is even (winning strategy for Alice), else False.
        return True if n % 2 == 0 else False


if __name__ == "__main__":
    # Set up test value for n.
    n = 2
    # Instantiate the solution.
    sol = Solution()
    # Output the result of divisorGame.
    print(sol.divisorGame(n))
