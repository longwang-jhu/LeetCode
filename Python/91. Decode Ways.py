# https://leetcode.com/problems/decode-ways/

# A message containing letters from A-Z can be encoded into numbers using the
# following mapping:

# To decode an encoded message, all the digits must be grouped then mapped back
# into letters using the reverse of the mapping above (there may be multiple
# ways). For example, "11106" can be mapped into:

# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped
# into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode
# it.

# The answer is guaranteed to fit in a 32-bit integer.

###############################################################################

# dp[i] = ways using s[0...i-1]
# if s[i-1] != "0", decode s[i-1] as a letter: dp[i] += dp[i-1]
# if 10 <= s[i-2,i-1] <= 26, decode s[i-2,i-2] as a letter: dp[i] += dp[i-2]

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == "0": return 0
        
        # base
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        
        # dp
        for i in range(2, n + 1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            if 10 <= int(s[i-2] + s[i-1]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]
            