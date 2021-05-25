# https://leetcode.com/problems/sum-of-square-numbers/

# Given a non-negative integer c, decide whether there're two integers a and b
# such that a2 + b2 = c.

###############################################################################

# two ptrs search over 0...sqrt(c)

from math import *
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            total = left ** 2 + right ** 2
            if total < c:
                left += 1
            elif total > c:
                right -= 1
            else:
                return True
        return False