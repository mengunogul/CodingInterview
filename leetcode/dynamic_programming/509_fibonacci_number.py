class Solution:
    def fib(self, n: int) -> int:
        # Initialize cache with base Fibonacci values
        cache = {0: 0, 1: 1}
        # Compute Fibonacci numbers from 2 up to n
        for i in range(2, n + 1):
            # If the value has not been computed, add it to the cache
            if i not in cache:
                cache[i] = cache[i - 1] + cache[i - 2]
        # Return the nth Fibonacci number
        return cache[n]


# If running this file directly, test the fib method.
if __name__ == "__main__":
    # Example input
    n = 7
    sol = Solution()
    # Print the Fibonacci number for the given n
    print(sol.fib(n))
