"""
Question: https://neetcode.io/problems/evaluate-reverse-polish-notation

This module provides a solution for evaluating arithmetic expressions written in
Reverse Polish Notation (RPN). The implementation uses a stack to process the tokens.
"""

from typing import List


class Solution:
    """
    A class used to evaluate Reverse Polish Notation (RPN) expressions.
    """

    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.

        The expression is given as a list of tokens, where each token is either an operand
        or an operator (+, -, *, /). The function uses a stack to compute the result.

        :param tokens: List of tokens representing the RPN expression.
        :return: The integer result of evaluating the expression.
        """
        # Define the set of valid operators.
        operators = ["+", "-", "*", "/"]
        # Initialize an empty stack to keep operands.
        stack: List[int] = []

        for element in tokens:
            if element in operators:
                # Pop the top two operands from the stack.
                second = stack.pop()  # Second operand (right-hand side)
                first = stack.pop()  # First operand (left-hand side)

                # Evaluate the expression using Python's eval() with proper formatting.
                # int() is used to force the result into an integer (truncates towards zero).
                result = int(eval(f"{first}{element}{second}"))
                # Push the computed result back onto the stack.
                stack.append(result)
            else:
                # If the token is an operand, convert it to int and push it onto the stack.
                stack.append(int(element))

        # The final result is the only element remaining in the stack.
        return stack.pop()


if __name__ == "__main__":
    # Example usage:
    sol = Solution()
    # Expression tokens representing: 4 + (13 / 5)
    tokens = ["4", "13", "5", "/", "+"]
    result = sol.evalRPN(tokens)
    print("Evaluation result:", result)
