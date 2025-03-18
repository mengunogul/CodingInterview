from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]


if __name__ == "__main__":
    solution = Solution()
    n = 5
    print(solution.countBits(n))
