# https://leetcode.com/problems/regular-expression-matching/

# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*' where:

# The matching should cover the entire input string (not partial).

################################################################################

# True/False -> matching depends on previous substring -> DP
# DP[i][j] = matching s[0...i-1] and p[0...j-1]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        
        # base
        dp = [[False] * (np + 1) for _ in range(ns + 1)]
        dp[0][0] = True
        # dp[0][1] = False
        # check if p can match ''
        for j in range(2, np + 1):
            if p[j-1] == "*": # 'c*' can match ''
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                if p[j-1] == '.': # '.' can match any char
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*': # 'c*' can math 'ccc...'
                    case0 = dp[i][j-2] # use '*' 0 times
                    case1 = dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.') # use '*'
                    dp[i][j] = case0 or case1
                elif p[j-1] == s[i-1]: # two chars match
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False

        return dp[-1][-1]
