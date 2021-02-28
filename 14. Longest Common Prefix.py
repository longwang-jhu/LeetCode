# use the first string as the base and compare with other strings

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        res = ""
        for charIdx in range(len(strs[0])):
            char = strs[0][charIdx]
            
            # compare with other strings
            for strIdx in range(1, len(strs)):
                if (charIdx >= len(strs[strIdx])) or (char != strs[strIdx][charIdx]):
                    return res
            res += char
        return res