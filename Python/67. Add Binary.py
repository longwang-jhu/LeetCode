# https://leetcode.com/problems/add-binary/

# Given two binary strings a and b, return their sum as a binary string.

###############################################################################

# carry = a.pop() + b.pop()
# carry, last_digit = divmod(carry, 2)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        
        a = list(a)
        b = list(b)
        carry = 0
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
                
            carry, last_digit = divmod(carry, 2)
            ans.append(str(last_digit))

        return ''.join(ans[::-1])