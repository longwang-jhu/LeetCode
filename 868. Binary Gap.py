# https://leetcode.com/problems/binary-gap/

# Given a positive integer n, find and return the longest distance between any
# two adjacent 1's in the binary representation of n. If there are no two
# adjacent 1's, return 0.

# Two 1's are adjacent if there are only 0's separating them (possibly no 0's).
# The distance between two 1's is the absolute difference between their bit
# positions. For example, the two 1's in "1001" have a distance of 3.

###############################################################################

# find idx of all 1's in binary number

class Solution:
    def binaryGap(self, n: int) -> int:
        # indexes of 1
        one_idxes = [i for i in range(32) if (n >> i) & 1]
        
        ans = 0
        for i in range(len(one_idxes) - 1):
            ans = max(ans, one_idxes[i+1] - one_idxes[i])
        return ans