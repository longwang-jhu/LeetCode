# n & n-1 gives the last bit

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n-1)