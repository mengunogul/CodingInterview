from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize result list to store rows of Pascal's triangle
        res: List[List[int]] = []
        for i in range(numRows):
            # Create the current row filled with 1's; length is i + 1
            row = [1] * (i + 1)
            # Update inner values using the sum of two numbers from the previous row
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            # Append the constructed row to the result list
            res.append(row)
        return res


if __name__ == "__main__":
    # Instantiate the solution and run with a sample input
    solution = Solution()
    numRows = 5  # Testing with sample input
    print(solution.generate(numRows))
