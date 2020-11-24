"""
==========================================
Part 3: String Comparison
==========================================
1. Create a recursive program called "compareTo" that compares two strings
and returns:
    a) a negative number if s1 < s2
    b) 0 if s1 == s2
    c a positive number if s1 > s2
"""

def compareTo(s1, s2):
        if len(s1) == 1 and len(s2) == 1:
            if s1 > s2:
                return 1
            elif s1 == s2:
                return 0
            else:
                return -1
        x, y = len(s1), len(s2)
        return compareTo(s1[x-1], s2[y-1])

if __name__ == "__main__":
  compareTo('Hello', 'hello')
