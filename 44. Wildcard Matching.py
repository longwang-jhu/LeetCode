# https://leetcode.com/problems/wildcard-matching/

# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*' where:

# The matching should cover the entire input string (not partial).

###############################################################################

# matching -> curr depends on prev -> dp
# dp[i][j] = is_match(s[first ith], p[first jth])

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return s == ''
        
        n_s, n_p = len(s), len(p)
        dp = [[False] * (n_p + 1) for _ in range(n_s + 1)]
        
        # initialize
        dp[0][0] = True
        for j in range(1, n_p + 1):
            dp[0][j] = dp[0][j-1] and p[j-1] == '*' # new char must be '*'
        
        # dp[i][j]
        for i in range(1, n_s + 1):
            for j in range(1, n_p + 1):
                if p[j-1] == '?': # '?' matches any char
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] # use or not use '*'
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        
        return dp[-1][-1]