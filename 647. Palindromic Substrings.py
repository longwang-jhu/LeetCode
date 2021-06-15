# https://leetcode.com/problems/palindromic-substrings/

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

################################################################################

# dp[i][j] = if s[i...j] is good

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        if n == 1: return 1
        
        ans = 0
        dp = [[False] * n for _ in range(n)]
        # base case
        for i in range(n): # one char str
            dp[i][i] = True
            ans += 1
        for i in range(n - 1): # two chars str
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans += 1
        
        # check s[i...i+incr]
        for incr in range(2, n): # incr = 2...n-1
            for i in range(n - incr): # i + incr <= n - 1
                j = i + incr
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans += 1
        
        return ans            
