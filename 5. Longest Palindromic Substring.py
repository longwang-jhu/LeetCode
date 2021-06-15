# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

################################################################################

# palindrome -> dp
# dp[i][j] = s[i...j] is good
# dp[i][j] = s[i+1...j-1] is good and s[i] == s[j]
# time: O(n^2), space: O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return None
        n = len(s)
        if n == 1: return s
        
        max_len_start = max_len_end = 0
        dp = [[False] * n for _ in range(n)]
        
        # base case
        for i in range(n): # single char str
            dp[i][i] = True
        for i in range(n - 1): # double char str
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_len_start, max_len_end = i, i + 1
        
        # loop for incr
        for incr in range(2, n): # incr = 2, ..., n - 1
            for i in range(n - incr): # i = 0, ..., n - 1 - incr
                j = i + incr # s[i...j]
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    max_len_start, max_len_end = i, j

        return s[max_len_start : max_len_end + 1]

# palindrome -> expand around center
# expand around 'a' and 'ab' for every char in string
# time: O(n^2), space: O(1)

# class Solution:
    def expand_center(self, s):
        if not s: return None
        n = len(s)
        if len(s) == 1: return s
        
        max_len = 0
        max_len_start = max_len_end = 0
        
        for i in range(n):
            len_a, start_a, end_a = self.get_len(i, i, s) # expand around 'a'
            len_ab, start_ab, end_ab = self.get_len(i, i + 1, s) # expand around 'ab'
            
            if len_a > max_len:
                max_len = len_a
                max_len_start, max_len_end = start_a, end_a
                
            if len_ab > max_len:
                max_len = len_ab
                max_len_start, max_len_end = start_ab, end_ab

        return s[max_len_start : max_len_end + 1]
    
    # Expand around center
    def get_len(self, l, r, s):
        if l < 0 or r >= len(s): return 0, None, None
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1, l + 1, r - 1 # length, start_idx, end_idx
