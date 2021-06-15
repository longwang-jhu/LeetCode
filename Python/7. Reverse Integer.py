# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).

###############################################################################

# reverse num -> get last digit -> divmod -> check overflow
# convert to abs(x) first
# range = [-2147483648, 2147483647]

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if x == INT_MIN or x == INT_MAX: return 0 # overflow
        if x == 0: return 0
        
        # convert x to abs(x) first
        x_abs = abs(x)
        x_rev = 0
        while x_abs != 0:
            x_abs, last_digit = divmod(x_abs, 10)

            # check overflow
            if x_rev > INT_MAX // 10 or (x_rev == INT_MAX // 10 and last_digit > 7):
                return 0 # overflow
            else:
                x_rev = x_rev * 10 + last_digit
        
        # put sign back
        return x_rev if x > 0 else -x_rev