from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        read = write = 0

        while read < n:
            char = chars[read]
            # 1) copy the character
            chars[write] = char
            write += 1

            # 2) count how many times it repeats
            start = read
            while read < n and chars[read] == char:
                read += 1
            count = read - start

            # 3) if more than one, write its digits
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # write is now the length of the compressed array
        return write
