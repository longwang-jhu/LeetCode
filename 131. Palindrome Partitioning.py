# https://leetcode.com/problems/palindrome-partitioning/

# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

################################################################################

# use all substrings for palindrome
# use dp[i][j] = if substring from i to j is palindrome to speed up

# dfs: add child for start to i, check if substring from start to i is palindrome
# add the substring to holder if palindrome and move to i + 1

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        
        # check all substrings for palindrome
        dp = [[True for _ in range(n)] for _ in range(n)]
        for incr in range(1, n):
            for i in range(n - incr):
                j = i + incr
                if s[i] == s[j] and (j <= i + 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        
        ans = []
        self.dfs(s, 0, [], ans, dp)
        return ans

    def dfs(self, s, start, holder, ans, dp):
        if start == len(s):
            ans.append(holder.copy())
        
        for i in range(start, len(s)):
            if dp[start][i]: # substring from start to i is palindrome
                holder.append(s[start:i + 1]) # add the substring to holder
                self.dfs(s, i + 1, holder, ans, dp)
                holder.pop()
