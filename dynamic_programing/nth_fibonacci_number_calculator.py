"""
The Fibonacci sequence is a series of numbers where each number is the sum of
the two numbers before it. It starts with 0 and 1, then continues indefinitely:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

The pattern is: F(n) = F(n-1) + F(n-2)

A module for calculating Fibonacci numbers using a dynamic programming approach.

This module defines a function to compute the nth Fibonacci number. It utilizes
a bottom-up technique to optimize performance by reducing redundant calculations.

Functions:
- fibonacci: Computes the nth Fibonacci number.
"""


def fibonacci(n):
    sequence = [0, 1]  # Initialize with [0, 1] as required

    # Edge case: if n is 0 or 1, return from sequence
    if n == 0:
        return sequence[0]
    if n == 1:
        return sequence[1]

    #  Dynamic programming: compute and append each number
    for i in range(2, n + 1):
        next_num = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_num)
        print(f"Fibonacci {next_num} = {sequence[i - 1]} + {sequence[i - 2]}")

    return sequence[n]


if __name__ == "__main__":
    result = fibonacci(10)
    print(f"\nThe 10th Fibonacci number is: {result}")
