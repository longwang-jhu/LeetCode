# https://leetcode.com/problems/length-of-last-word/

# Given a string s consists of some words separated by spaces, return the
# length of the last word in the string. If the last word does not exist,
# return 0.

# A word is a maximal substring consisting of non-space characters only.

###############################################################################

# backward traversal

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or len(s) == 0: return 0
        if s == ' ': return 0
        
        ans = 0
        for i in range(len(s) - 1, -1, -1): # backward traversal
            if s[i] != ' ':
                ans += 1
            if s[i] == ' ' and ans != 0: # space before the last word
                break
        return ans