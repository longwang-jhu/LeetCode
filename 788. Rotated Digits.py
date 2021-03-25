# https://leetcode.com/problems/rotated-digits/

# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.  Each digit must be rotated -
# we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. 0, 1, and 8
# rotate to themselves; 2 and 5 rotate to each other (on this case they are
# rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and
# 9 rotate to each other, and the rest of the numbers do not rotate to any
# other number and become invalid.

# Now given a positive number N, how many numbers X from 1 to N are good?

# Note:

###############################################################################

# loop over all numbers

class Solution:
    def rotatedDigits(self, N: int) -> int:
        def is_valid(num):
            valid_flag = False
            while num > 0:
                last_digit = num % 10
                if last_digit in [3, 4, 7]:
                    return False
                elif last_digit in [2, 5, 6, 9]:
                    valid_flag = True
                num = num // 10
            return valid_flag

        ans = 0
        for num in range(1, N + 1):
            if is_valid(num):
                ans += 1
        return ans            
        