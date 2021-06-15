# https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.

###############################################################################

# use counter to compare

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        target = Counter(t)
        for char in s:
            target[char] -= 1
            if target[char] < 0:
                return False
        
        return True