# https://leetcode.com/problems/count-primes/

# Count the number of prime numbers less than a non-negative number, n.

################################################################################

# search over 2, ..., sqrt(n) -> add multi (starting from i*i)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        
        not_prime = {}
        for i in range(2, int(sqrt(n)) + 1):
            if i not in not_prime:
                for multi in range(i * i, n, i):
                    not_prime[multi] = 1
        
        # also remove 1 and n
        return n - len(not_prime) - 2
