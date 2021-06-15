# https://leetcode.com/problems/longest-nice-substring/

# A string s is nice if, for every letter of the alphabet that s contains, it
# appears both in uppercase and lowercase. For example, "abABB" is nice because
# 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b'
# appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are
# multiple, return the substring of the earliest occurrence. If there are none,
# return an empty string.

################################################################################

# divide and conquer -> split at invalid char

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: return ''
        if len(s) == 1: return ''
        
        n = len(s)
        chars = set(list(s))
        
        for i in range(len(s)):
            if s[i].lower() not in chars or s[i].upper() not in chars:
                # can split at s[i]
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right
        
        return s # s is nice
