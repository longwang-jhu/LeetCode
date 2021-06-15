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

# a / b -> make both positive -> recursive

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if dividend == 0: return 0
        if divisor == 1: return dividend
        if divisor == -1: return -dividend if dividend > INT_MIN else INT_MAX

        # determine sign
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        
        a, b = abs(dividend), abs(divisor)
        ans = self.divide_simple(a,b)
        
        if sign > 0:
            return INT_MAX if ans > INT_MAX else ans
        else:
            return -ans
    
    def divide_simple(self, a, b):
        if a < b: return 0
        
        count = 1
        b_multi = b
        while b_multi * 2 <= a:
            count *= 2
            b_multi *= 2
            
        return count + self.divide_simple(a - b_multi, b)