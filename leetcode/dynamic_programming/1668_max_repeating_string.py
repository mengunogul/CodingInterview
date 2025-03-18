class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        Returns the maximum number of times word is repeated consecutively in sequence.
        """
        # Early exit: if word is empty, return 0 to avoid errors.
        if not word:
            return 0  # Avoid division by zero if word is empty
        max_count = 0
        word_length = len(word)
        seq_length = len(sequence)
        # Iterate over possible start indices in sequence.
        for i in range(seq_length - word_length + 1):
            count = 0
            # Check consecutive segments from the current index that equal to word.
            while (
                sequence[i + count * word_length : i + (count + 1) * word_length]
                == word
            ):
                count += 1
            # Update max_count if a longer repetition sequence is found.
            if count > max_count:
                max_count = count
        return max_count


def main():
    # Setup sample inputs for testing.
    sequence = "ababc"
    word = "ab"
    sol = Solution()
    print(sol.maxRepeating(sequence, word))  # Output the result of maxRepeating


if __name__ == "__main__":
    # Entry point: Execute main when script is run.
    main()
