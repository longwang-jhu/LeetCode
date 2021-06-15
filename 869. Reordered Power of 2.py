# https://leetcode.com/problems/reordered-power-of-2/

# You are given an integer n. We reorder the digits in any order (including the
# original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a
# power of two.

################################################################################

# reorder digits -> digits count -> compare with digits count of 2**i

from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_counter = Counter(str(n))
        for i in range(31): # max power of 2 is 2**30
            if n_counter == Counter(str(1 << i)):
                return True
        return False
            
