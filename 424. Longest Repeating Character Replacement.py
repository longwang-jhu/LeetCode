# https://leetcode.com/problems/longest-repeating-character-replacement/

# You are given a string s and an integer k. You can choose any character of the
# string and change it to any other uppercase English character. You can perform
# this operation at most k times.

# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.

################################################################################

# sliding window -> move when right - left - max_char_count > k
# use dict to record char count

from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n == 1: return 1
        
        max_len = 0
        window = Counter()
        max_char_freq = 0 # max char freq for windown
        
        left = right = 0
        while right < n:
            # update window
            new_char = s[right]
            window[new_char] += 1
            max_char_freq = max(max_char_freq, window[new_char])
            
            # shrink window
            while right - left + 1 - max_char_freq > k:
                old_char = s[left]
                window[old_char] -= 1
                left += 1
            
            # update max_len
            max_len = max(max_len, right - left + 1)
            
            # expand window
            right += 1
        
        return max_len
