"""
===========================================
Part 2 - Implement Euclid's GCD Algorithm
===========================================
1. Create a recursive Greatest common divisor (the largest number that two integers can be divided
 by without a remainder)
2. Called the recursive function "gcd" that takes in parameters a, b,
"""

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)

if __name__ == '__main__':
    print(gcd(5,25))
