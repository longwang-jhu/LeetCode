# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

###############################################################################

# palindrome -> DP
# DP[i,j] = s[i, ..., j] is palindromic
# time: O(n^2), space: O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return None
        if len(s) == 1: return s
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = (0, 0) # (start_idx, end_idx) for longest palindromic substring
        
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = (i, i + 1)
        
        for incr in range(2, n): # incr = 2, ..., n - 1
            for i in range(n - incr): # i = 0, ..., n - 1 - incr
                j = i + incr
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    ans = (i, j)

        return s[ans[0]:ans[1] + 1]

# palindrome -> expand around center
# expand around 'a' and 'ab' for every char in string
# time: O(n^2), space: O(1)

# class Solution:
    def longestPalindrome2(self, s: str) -> str:
        if not s: return None
        if len(s) == 1: return s
        
        n = len(s)
        max_len = 0
        start, end = 0, 0 # start_idx and end_idx for longest palindromic substring
        for idx in range(n):
            pali_len_a, start_a, end_a = self.get_pali_len(idx, idx, s) # expand around 'a'
            pali_len_ab, start_ab, end_ab = self.get_pali_len(idx, idx + 1, s) # expand around 'ab'
            
            if pali_len_a > max_len:
                max_len = pali_len_a
                start, end = start_a, end_a
            if pali_len_ab > max_len:
                max_len = pali_len_ab
                start, end = start_ab, end_ab

        return s[start:end + 1]
    
    # Expand around center to get the longest Palindromic substring
    def get_pali_len(self, l, r, s):
        if l < 0 or r >= len(s): return 0, None, None
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
        return r - l - 1, l + 1, r - 1 # lenght, start_idx, end_idx