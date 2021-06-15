# https://leetcode.com/problems/word-break/

# Given a string s and a dictionary of strings wordDict, return true if s can be
# segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.

################################################################################

# dp[i] = if can break using s[0...i]
# update dp[i], check if s[j...i] is word and dp[j-1] == True
# speed up: stop when len(s[j...i]) > max_word_len

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # get max word length
        max_word_len = 0
        for word in wordDict:
            max_word_len = max(max_word_len, len(word))
        
        # base
        dp = [False] * len(s)
        
        # dp
        for i in range(len(s)):
            for j in range(i, -1, -1): # j = i...0
                # check if s[j...i] is word
                if i - j + 1 > max_word_len:
                    break # no need to go further
                if (j == 0 or dp[j - 1]) and s[j : i + 1] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]   
