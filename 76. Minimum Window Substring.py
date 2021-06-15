# https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates) is
# included in the window. If there is no such substring, return the empty string
# "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

################################################################################

# sliding window -> compare window counter with target counter

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # target counter
        target = Counter(t)
        
        # sliding window
        min_len = float("inf")
        min_len_start = 0
        window = Counter()
        n_valid_chars = 0
        
        left = right = 0
        while right < len(s):
            # update window
            new_char = s[right]
            if new_char in target: # useful char
                window[new_char] += 1
                if window[new_char] == target[new_char]:
                    n_valid_chars += 1
            
            # shrink window
            while n_valid_chars == len(target):
                # update min_len
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_len = curr_len
                    min_len_start = left

                # update window dict by removing s[left]
                old_char = s[left]
                if old_char in target: # useful char
                    if window[old_char] == target[old_char]:
                        n_valid_chars -= 1
                    window[old_char] -= 1
                left += 1 # shrink window
            
            # expand window
            right += 1 # expand window
        
        # return ans
        if min_len == float("inf"):
            return ""
        
        return s[min_len_start : min_len_start + min_len]
