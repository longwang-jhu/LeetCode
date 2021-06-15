# https://leetcode.com/problems/convert-to-base-2/

# Given a number N, return a string consisting of "0"s and "1"s that represents
# its value in base -2 (negative two).

# The returned string must have no leading zeroes, unless the string is "0".

###############################################################################

# similar to base 2 -> note -1 = (-2) ** 1 + (-2) ** 0

class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0: return "0"
        
        ans = []
        while N:
            N, rem = divmod(N, -2)
            if rem == -1: # -1 = (-2) ** 1 + (-2) ** 0
                N += 1
                rem = 1
            ans.append(str(rem))
        
        return ''.join(ans[::-1])