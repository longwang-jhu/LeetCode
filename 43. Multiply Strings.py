# https://leetcode.com/problems/multiply-strings/

# Given two non-negative integers num1 and num2 represented as strings, return the
# product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to
# integer directly.

################################################################################

# multiply -> (reversely) multi[i+j] = nums[-i-1] * nums[-j-1]
# -> handle (multi[i] >= 10) afterwards
# int(char) = ord(char) - ord('0')
# chr(num) = chr(num + ord('0'))

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        if num1 == '1': return num2
        if num2 == '1': return num1
        
        n1, n2 = len(num1), len(num2)
        multi = [0] * (n1 + n2)
        
        for i in range(n1):
            for j in range(n2):
                multi[i+j] += (ord(num1[-i-1]) - ord('0')) * (ord(num2[-j-1]) - ord('0'))        
        # multi is in reverse order

        # handle ans[i] >= 10
        carry = 0
        for i in range(n1 + n2):
            multi[i] += carry
            carry, multi[i] = divmod(multi[i], 10)

        # handle leading '0'
        ans = ''
        for i in range(n1 + n2 - 1, -1, -1): # travel reversely
            if multi[i] == 0 and ans == '':
                continue
            ans += chr(multi[i] + ord('0'))
        return ans
