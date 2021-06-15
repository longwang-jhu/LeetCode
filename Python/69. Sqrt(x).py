# https://leetcode.com/problems/sqrtx/

# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.

###############################################################################

# binary search -> find target ** 2 == x in [1, ..., x // 2]

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        
        left, right = 1, x // 2
        while left + 1 < right:
            mid = left + (right - left) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq > x:
                right = mid
            else: # sq < x
                left = mid
        
        # left <= sqrt(x) <= right
        if right * right <= x:
            return right
        else:
            return left