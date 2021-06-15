# https://leetcode.com/problems/counting-bits/

# Given an integer num, return an array of the number of 1's in the binary
# representation of every number in the range [0, num].

###############################################################################

# dp[i] = dp[i >> 1] + (i & 1)

class Solution:
    def countBits(self, num: int) -> List[int]:
        # init
        dp = [None] * (num + 1)
        dp[0] = 0
        
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp