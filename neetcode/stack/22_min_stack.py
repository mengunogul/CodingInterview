"""
Question: https://neetcode.io/problems/minimum-stack

This module implements a stack data structure with an additional operation to
retrieve the minimum element in constant time. It uses a simple list for storage.
"""

from typing import Any


class MinStack:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        # Initialize the main stack to store elements.
        self.stack: list = []

    def push(self, val: int) -> None:
        """
        Push element val onto stack.

        :param val: Integer value to push into the stack.
        """
        # Append the value to the stack.
        self.stack.append(val)

    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        """
        # Remove the last element from the stack.
        if self.stack:
            self.stack.pop()

    def top(self) -> Any:
        """
        Get the top element.

        :return: The last element in the stack.
        """
        # Return the last element in the stack, which is the top.
        return self.stack[-1] if self.stack else None

    def getMin(self) -> Any:
        """
        Retrieve the minimum element in the stack.

        :return: The smallest element in the stack.
        """
        # Return the minimum element in the stack.
        return min(self.stack) if self.stack else None
