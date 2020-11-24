"""
===========================================
Part 1 - Implement the Fibonacci Sequence
===========================================
1. Create a recursive Fibonacci sequence (nth number is the sum of the previous two in the sequence)
2. Save the function in a file call recursion.py, name the function fibonacci
"""


def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return fibonacci(n -1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(5))


