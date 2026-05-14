#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    """Calculates the fewest number of operations
    needed to result in exactly n H characters in the file."""
    if n <= 1:
        return 0

    operations = 0
    current_length = 1

    while current_length < n:
        if n % current_length == 0:
            operations += 2  # Copy All and Paste
            current_length *= 2
        else:
            operations += 1  # Paste

    return operations
