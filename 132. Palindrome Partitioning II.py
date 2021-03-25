# https://leetcode.com/problems/palindrome-partitioning-ii/

# Given a string s, partition s such that every substring of the partition is a
# palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

###############################################################################

# dp_pali[i][j] = if substring from i to j is palindrome
# dp_cut[i] = min cut of substring from 0 to i
# update by checking prev dp_cut[j] and make sure substring (j, i) is palindrome

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        
        # check all substring for palidrome
        dp_pali = [[True for _ in range(n)] for _ in range(n)]        
        for incr in range(1, n):
            for i in range(n - incr):
                j = i + incr
                if s[i] == s[j] and (j <= i + 2 or dp_pali[i+1][j-1]):
                    dp_pali[i][j] = True
                else:
                    dp_pali[i][j] = False
        
        # determine min cut by checking prev cut
        dp_cut = [i for i in range(n)]
        for right in range(1, n):
            for left in range(right + 1): # from 0 to right, cut just before left
                if dp_pali[left][right]: # check if substring (left, right) is palindrome
                    if left == 0:
                        dp_cut[right] = 0 # entire substring is palindrome
                    else:
                        dp_cut[right] = min(dp_cut[right], dp_cut[left - 1] + 1)

        return dp_cut[-1]