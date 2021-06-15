# https://leetcode.com/problems/power-of-two/

# Given an integer n, return true if it is a power of two. Otherwise, return
# false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

################################################################################

# bit operation -> not power of two: n & n-1 == 0

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n-1)
