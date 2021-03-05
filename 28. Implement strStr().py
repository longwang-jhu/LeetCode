# loop over haystack and compare with needle
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)        
        for i in range(m - n + 1):
            if haystack[i: i + n] == needle:
                return i       
        return -1