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

# Dict with key = Roman letter, value = num
# one-pass add, subtract if next letter has larger value

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s) - 1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                ans -= roman_dict[s[i]]
            else:
                ans += roman_dict[s[i]]
        
        ans += roman_dict[s[-1]]
        return ans