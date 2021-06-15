# https://leetcode.com/problems/regular-expression-matching/

# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*' where:

# The matching should cover the entire input string (not partial).

###############################################################################

# True/False -> matching depends on previous substring -> DP
# DP[i,j] = matching s[first i chars] and p[first j chars]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n_s, n_p = len(s), len(p)
        
        # initialize
        dp = [[False] * (n_p + 1) for _ in range(n_s + 1)]
        dp[0][0] = True
        
        # check p to match ''
        # dp[0][1] = False
        for j in range(2, n_p + 1):
            if p[j-1] == "*": # 'c*' can match ''
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, n_s + 1):
            for j in range(1, n_p + 1):
                if p[j-1] == '.': # '.' can match any char
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*': # 'c*' can math 'ccc...'
                    case1 = dp[i][j-2] # use 'c' 0 times
                    case2 = dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.') # use 'c' one more times
                    dp[i][j] = case1 or case2
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1] # two chars match

        return dp[-1][-1]