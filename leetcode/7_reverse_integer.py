class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_str = str(abs(x))[::-1]
        reversed_int = sign * int(reversed_str)

        return (
            0 if reversed_int > (2**31) - 1 or reversed_int < -(2**31) else reversed_int
        )
