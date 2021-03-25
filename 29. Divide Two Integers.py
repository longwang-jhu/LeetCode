# https://leetcode.com/problems/divide-two-integers/

# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero, which means losing its
# fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

# Note: Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−231, 231 − 1]. For this
# problem, assume that your function returns 231 − 1 when the division result
# overflows.

###############################################################################

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = - 2 ** 31
        INT_MAX = 2 ** 31 - 1
        
        if dividend == 0: return 0
        if divisor == 1: return dividend
        if divisor == -1:
            if dividend > INT_MIN: return -dividend
            else: return INT_MAX
        
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        
        a = abs(dividend)
        b = abs(divisor)
        
        def divideSimple(a: int, b: int) -> int:
            if a < b: return 0
            count = 1
            bTemp = b
            while bTemp * 2 <= a:
                count *= 2
                bTemp *= 2
            return count + divideSimple(a - bTemp, b)
        
        res = divideSimple(a,b)
        
        if sign > 0:
            if res > INT_MAX:
                res == INT_MAX
            return res
        else:
            return -res;