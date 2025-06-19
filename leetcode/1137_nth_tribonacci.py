class Solution:
    # Calculate the nth Tribonacci number.
    def tribonacci(self, n: int) -> int:
        cache = {
            0: 0,
            1: 1,
            2: 1,
        }
        for i in range(3, n + 1):
            if i not in cache:
                cache[i] = cache[i - 3] + cache[i - 2] + cache[i - 1]

        return cache[n]


if __name__ == "__main__":
    n = 25
    sol = Solution()
    print(sol.tribonacci(n))
