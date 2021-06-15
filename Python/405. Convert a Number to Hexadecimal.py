# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

# Given an integer num, return a string representing its hexadecimal
# representation. For negative integers, two’s complement method is used.

# All the letters in the answer string should be lowercase characters, and
# there should not be any leading zeros in the answer except for the zero
# itself.

###############################################################################

# if negative, num += 2 ** 32

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        
        if num < 0:
            num += 2 ** 32
        
        ans = []
        letter_dict = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        while num:
            num, rem = divmod(num, 16)
            if rem >= 10:
                ans.append(letter_dict[rem])
            else:
                ans.append(str(rem))
        return ''.join(ans[::-1])