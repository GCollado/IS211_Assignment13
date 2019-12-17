"""
===========================================
Part 1 - Implement the Fibonacci Sequence
===========================================
1. Create a recursive Fibonacci sequence (nth number is the sum of the previous two in the sequence)
2. Save the function in a file call recursion.py, name the function Fibonacci
"""
from functools import lru_cache
import sys

#F(n) = F(n-1) + F(n-2)

@lru_cache(maxsize = 1000)
def fibonacci(n):
    sys.setrecursionlimit(10000)
    if type(n) !=int:
        raise TypeError("n must be a positive number")
    a = n - 1
    b = n - 2
    if n <= 1:
        return n
    else:
        return fibonacci(a) + fibonacci(b)

#0,1,1,,2,3,5,8,13,21,34
if __name__ == '__main__':
    print(fibonacci(500))


