# https://leetcode.com/problems/valid-palindrome-ii/

# Given a string s, return true if the s can be palindrome after deleting at most
# one character from it.

################################################################################

# use left and right pts
# if no match check substrings from left+1 to right, and from left to right-1

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else: # no match
                is_left = self.is_pali_range(s, left + 1, right) # delete left char
                is_right = self.is_pali_range(s, left, right - 1) # delete right char
                return is_left or is_right
        return True
    
    # check is substring from l to r is palindrome
    def is_pali_range(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
