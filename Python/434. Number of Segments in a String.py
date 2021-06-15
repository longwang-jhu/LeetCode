# https://leetcode.com/problems/number-of-segments-in-a-string/

# You are given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.

###############################################################################

# look for ' *'

class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                count += 1
        
        return count