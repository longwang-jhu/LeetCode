# get the right-most bit by n % 2 or n & 1
# 2**1 + 2**2 is bit OR operation 2**1 | 2**2 

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        pow_idx = 31
        while n > 0:
            d = n & 1 # get the right-most bit
            ans += d << pow_idx # d ** pow_idx
            n = n >> 1 # remove the right-most bit
            pow_idx -= 1
        return ans
        