# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

# Given two integers L and R, find the count of numbers in the range [L, R]
# (inclusive) having a prime number of set bits in their binary representation.

# (Recall that the number of set bits an integer has is the number of 1s
# present when written in binary. For example, 21 written in binary is 10101
# which has 3 set bits. Also, 1 is not a prime.)

# 

# Example 1:

# 

# Example 2:

# 

# Note:

# 

###############################################################################

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0
        for num in range(L, R + 1):
            if bin(num).count('1') in primes:
                ans += 1
        return ans