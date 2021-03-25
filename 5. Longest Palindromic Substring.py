# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

###############################################################################

# check length by expanding around center
# two cases: start with "A" or "AB"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # Expand around center to get the longest Palindromic substring
        def getLen(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        centerIdx = 0
        maxLen = 0

        for idx in range(n):
            currLen = max(getLen(idx, idx), getLen(idx, idx + 1)) # two cases

            if currLen > maxLen:
                maxLen = currLen
                centerIdx = idx

        startIdx = centerIdx - (maxLen - 1) // 2
        return s[startIdx : startIdx + maxLen]