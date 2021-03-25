# https://leetcode.com/problems/roman-to-integer/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.

# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:

# Given a roman numeral, convert it to an integer.

###############################################################################

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