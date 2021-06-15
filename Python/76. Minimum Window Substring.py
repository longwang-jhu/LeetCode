# https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t, return the minimum window in s which will contain
# all the characters in t. If there is no such window in s that covers all
# characters in t, return the empty string "".

# Note that If there is such a window, it is guaranteed that there will always
# be only one unique minimum window in s.

###############################################################################

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