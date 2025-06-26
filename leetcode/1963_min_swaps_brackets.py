class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0
        for bracket in s:
            if bracket == "[":
                swaps += 1
            elif swaps > 0:
                swaps -= 1
        return (swaps + 1) // 2
