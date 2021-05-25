# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

# Given a string s and a string array dictionary, return the longest string in
# the dictionary that can be formed by deleting some of the given string
# characters. If there is more than one possible result, return the longest
# word with the smallest lexicographical order. If there is no possible result,
# return the empty string.

###############################################################################

# sort dict and check if key can be substr

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        
        for key in dictionary:
            # if key is a substr of s
            if self.is_substr(key, s):
                return key
        return ''
    
    def is_substr(self, substr, s):
        i = j = 0
        while i < len(substr) and j < len(s):
            if substr[i] == s[j]: # move i only when there is a match
                i += 1
            j += 1
        return i == len(substr)