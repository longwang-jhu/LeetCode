# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of
# strings.

# If there is no common prefix, return an empty string "".

###############################################################################

# one-pass -> compare with the first string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        
        ans = ''
        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs[1:]: # compare with other strings
                if i >= len(string) or char != string[i]:
                    return ans
            ans += char
        return ans