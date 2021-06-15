# https://leetcode.com/problems/sum-of-two-integers/

# Given two integers a and b, return the sum of the two integers without using
# the operators + and -.

###############################################################################

# consider add in bits

class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0: return b
        if b == 0: return a

        INT_MAX = 0x7FFFFFFF # 32-bit INT_MAX
        INT_MIN = 0x80000000 # 32-bit INT_MIN
        mask = 0xFFFFFFFF # fot getting last 32-bit
        
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        if a <= INT_MAX:
            return a
        else:
            return ~(a ^ mask)