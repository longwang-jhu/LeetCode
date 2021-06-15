# https://leetcode.com/problems/2-keys-keyboard/

# There is only one character 'A' on the screen of a notepad. You can perform two
# operations on this notepad for each step:

# Given an integer n, return the minimum number of operations to get the character
# 'A' exactly n times on the screen.

################################################################################

# get prime factorization and sum up all the primes
# moves: [CPP][CPPPP][CP]
# n = len1 * len2 * len3 = primes factorization

class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        prime = 2
        while n > 1:
            while n % prime == 0:
                ans += prime
                n /= prime
            prime += 1
        return ans
