class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        levels: dict[int, list[str]] = {i: [] for i in range(numRows)}

        level = 0
        direction = 1
        for i in range(len(s)):
            if level == 0:
                direction = 1
            if level == numRows - 1:
                direction = -1

            levels[level].append(s[i])
            level += direction

        res = []

        for i in range(numRows):
            res += levels[i]
        return "".join(res)
