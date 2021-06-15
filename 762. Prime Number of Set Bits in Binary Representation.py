# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

# Given two integers left and right, return the count of numbers in the inclusive
# range [left, right] having a prime number of set bits in their binary
# representation.

# Recall that the number of set bits an integer has is the number of 1's present
# when written in binary.

################################################################################

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0
        for num in range(L, R + 1):
            if bin(num).count('1') in primes:
                ans += 1
        return ans
