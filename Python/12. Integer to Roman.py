# https://leetcode.com/problems/integer-to-roman/

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

# Given an integer, convert it to a roman numeral.

###############################################################################

# gradually reduce num and append symbols
# values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

class Solution:
    def intToRoman(self, num: int) -> str:
        if num <= 0: return None
        
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        
        ans = ''
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                ans += symbols[i]
        return ans