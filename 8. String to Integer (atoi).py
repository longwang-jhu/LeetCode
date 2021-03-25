# https://leetcode.com/problems/string-to-integer-atoi/

# Implement the myAtoi(string s) function, which converts a string to a 32-bit
# signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Note:

###############################################################################

# range = [-2147483648, 2147483647]

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2 ** 31 - 1, - 2 ** 31
        
        res = 0
        sign = 1
        i = 0
        
        # skip leading whitespace
        while i < len(s) and s[i] == " ":
            i += 1
        
        # check optional sign
        if i < len(s) and (s[i] == "+" or s[i] == "-"):
            sign = 1 if s[i] == "+" else -1
            i += 1
        
        while i < len(s) and s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if sign == 1:
                if res > int(INT_MAX/10) or (res == int(INT_MAX/10) and int(s[i]) > 7):
                    return INT_MAX
                else:
                    res = res * 10 + int(s[i])
            else:
                if res < int(INT_MIN/10) or (res == int(INT_MIN/10) and int(s[i]) > 8):
                    return INT_MIN
                else:
                    res = res * 10 - int(s[i])
            
            i += 1
        return res