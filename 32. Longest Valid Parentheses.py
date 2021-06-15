# https://leetcode.com/problems/longest-valid-parentheses/

# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.

################################################################################

# dp[i] = longest valid of s[i:n] starting with s[i] -> travel backwards
# s[i], [valid of len = dp[i+1]], s[j], [valid of len = dp[j+1]], ...


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1: return 0
        
        n = len(s)
        ans = 0
        dp = [0] * n
        
        for i in range(n - 2, -1, -1):
            if s[i] == "(":
                # loop for ")" at j: s[i], [valid of len = dp[i+1]], s[j]
                j = i + dp[i + 1] + 1
                if j < n and s[j] == ")":
                    dp[i] = dp[i + 1] + 2
                    
                    if j + 1 < n: # cumlative valid length starting with s[j+1]
                        dp[i] += dp[j + 1]
                        
        return max(dp)
