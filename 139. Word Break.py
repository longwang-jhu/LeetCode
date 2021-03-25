# https://leetcode.com/problems/word-break/

# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.

###############################################################################

# dp[i] = if can break substring from 0 to i
# update by checking prev dp[j] and make sure substring (left, right) is in wordDict
# get max word length for speed up

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # get max word length
        max_word_len = 0
        for word in wordDict:
            max_word_len = max(max_word_len, len(word))
        
        # dp[i] = if can break substring from 0 to i
        n = len(s)
        dp = [False for _ in range(n)]
        for right in range(n):
            left_start = max(0, right - 1 - max_word_len) # for speed up
            for left in range(left_start, right + 1): # cut just before left
                if s[left:right + 1] in wordDict: # check if substring (left, right) is in wordDict
                    if left == 0 or dp[left - 1]: # entire substring, or the prev substring (0, left-1) is in wordDict
                        dp[right] = True
                        continue

        return dp[-1]