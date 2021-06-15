# https://leetcode.com/problems/plus-one/

# Given a non-empty array of decimal digits representing a non-negative integer,
# increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the
# list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number
# 0 itself.

################################################################################

# travel backwards, add 1 to digit and return
# if digit == 9, change it 0 and move on

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1): # backward traversal
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else: # digits[i] = 9
                digits[i] = 0
        
        # for 999...
        return [1] + digits
