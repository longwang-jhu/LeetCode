# https://leetcode.com/problems/implement-strstr/

# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great
# question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().

###############################################################################

# loop over haystack and compare with needle

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        
        for i in range(m - n + 1):
            if haystack[i: i + n] == needle:
                return i       
        return -1