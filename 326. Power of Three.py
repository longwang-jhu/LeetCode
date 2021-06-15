# https://leetcode.com/problems/power-of-three/

# Given an integer n, return true if it is a power of three. Otherwise, return
# false.

# An integer n is a power of three, if there exists an integer x such that n ==
# 3x.

################################################################################

# while n % 3 == 0: n /= 3

# other method
# check 3 ** 19 % n == 0, where 3**19 is the largest number that is power of three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False
        
        while n % 3 == 0:
            n /= 3
        return n == 1
