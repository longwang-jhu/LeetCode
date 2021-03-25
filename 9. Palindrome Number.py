# https://leetcode.com/problems/palindrome-number/

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For
# example, 121 is palindrome while 123 is not.

###############################################################################

# compare x and xRev

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0: return False
        
        xRev = 0
        xCopy = x
        while xCopy != 0:
            xCopy, digitLast = divmod(xCopy, 10)
            xRev = xRev * 10 + digitLast
        
        return x == xRev