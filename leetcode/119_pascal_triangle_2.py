from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Use O(rowIndex) space by building the row iteratively
        row = [1]
        for i in range(1, rowIndex + 1):
            # Update row in-place from the end
            row.append(1)
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        return row


if __name__ == "__main__":
    # Instantiate the solution and run with a sample input
    solution = Solution()
    rowIndex = 5  # Testing with sample input
    print(solution.getRow(rowIndex))
