class Solution:
    def myAtoi(self, s: str) -> int:
        integer = 0
        sign = 1
        first = False

        for ch in s.strip():
            if ch == "-" and not first:
                first = True
                sign = -1
            elif ch == "+" and not first:
                first = True
                sign = 1
            elif ch.isdigit():
                first = True
                integer = (integer * 10) + int(ch)
            else:
                break
        
        val  = sign * integer
        if val > (2 ** 31) -1:
            return (2 ** 31) -1
        elif val < (-2 ** 31):
            return (-2 ** 31)
        else:
            return val
