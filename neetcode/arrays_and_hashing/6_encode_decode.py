"""
Question: https://neetcode.io/problems/string-encode-and-decode
Best possible solution using a length-prefixed encoding scheme.
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encode a list of strings to a single string using length-prefixed encoding.
        
        :param strs: List of strings to encode.
        :return: Encoded string.
        """
        encoded_parts = []
        for s in strs:
            encoded_parts.append(f"{len(s)}#{s}")
        return "".join(encoded_parts)

    def decode(self, s: str) -> List[str]:
        """
        Decode a single string back to a list of strings using the length-prefix scheme.
        
        :param s: Encoded string.
        :return: List of decoded strings.
        """
        i = 0
        decoded = []
        while i < len(s):
            # Find the separator to get the length.
            j = s.find("#", i)
            if j == -1:
                break  # Safety check
            length = int(s[i:j])
            decoded.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded

    
if __name__ == "__main__":
    sol = Solution()
    
    # Test with non-empty list
    original_strings = ["Hello", "world", "this", "is", "a", "test"]
    encoded = sol.encode(original_strings)
    print("Encoded string:", encoded)
    decoded = sol.decode(encoded)
    print("Decoded list:", decoded)
    
    # Verify round-trip
    assert decoded == original_strings, "Round-trip encoding/decoding failed!"
    print("Success: Decoded list matches the original strings.")