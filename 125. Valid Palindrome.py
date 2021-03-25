# https://leetcode.com/problems/valid-palindrome/

# Given a string s, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.

###############################################################################

# use left and right
# use char.isalnum()

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum(): # look for alnum
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True