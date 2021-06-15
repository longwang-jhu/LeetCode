# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating
# characters.

###############################################################################

# sliding window -> check window_counter

from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1
        
        # sliding window
        max_len = 0
        window = Counter()
        
        left = right = 0
        while right < len(s):
            # update window
            new_char = s[right]
            window[new_char] += 1
            
            # shrink window when exist repeating char
            while window[new_char] > 1:
                old_char = s[left]
                window[old_char] -= 1
                left += 1
            
            # window is good, update ans
            max_len = max(max_len, right - left + 1)
            
            # expand window
            right += 1
            
        return max_len