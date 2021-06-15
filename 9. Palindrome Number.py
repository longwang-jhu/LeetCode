# https://leetcode.com/problems/palindrome-number/

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For
# example, 121 is palindrome while 123 is not.

################################################################################

# palindrome number -> find x_rev -> compare x and x_rev

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0: return False
        
        x_copy = x
        x_rev = 0
        while x_copy != 0:
            x_copy, last_digit = divmod(x_copy, 10)
            x_rev = x_rev * 10 + last_digit
        return x == x_rev
