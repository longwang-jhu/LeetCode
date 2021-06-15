# https://leetcode.com/problems/power-of-four/

# Given an integer n, return true if it is a power of four. Otherwise, return
# false.

# An integer n is a power of four, if there exists an integer x such that n ==
# 4x.

###############################################################################

# while n % 4 == 0: n /= 4
# check power of two first

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1: return False
        if n & n-1: return False # must be power of 2
        
        while n % 4 == 0:
            n /= 4
        return n == 1        