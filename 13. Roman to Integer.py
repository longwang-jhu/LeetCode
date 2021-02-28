# use romanDict, determine value of each symbol and use subtraction if necessary

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s) - 1):
            if s[i] + s[i+1] in ['IV', 'IX']:
                res -= romanDict[s[i]]
            elif s[i] + s[i+1] in ['XL', 'XC']:
                res -= romanDict[s[i]]
            elif s[i] + s[i+1] in ['CD', 'CM']:
                res -= romanDict[s[i]]
            else:
                res += romanDict[s[i]]
        
        res += romanDict[s[-1]]
        return res