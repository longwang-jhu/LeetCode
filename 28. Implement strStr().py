# method 1: loop over haystack and compare with needle
# method 2: loop over haystack and needle, compare char haystack[i+j] and needle[j]
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)        
        for i in range(m - n + 1):
            if haystack[i: i + n] == needle:
                return i       
        return -1
        
        # if n == 0: return 0
        # for i in range(m - n + 1):
        #     for j in range(n):
        #         if haystack[i+j] != needle[j]:
        #             break
        #         if j == n - 1:
        #             return i
        # return -1