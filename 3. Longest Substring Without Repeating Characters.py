# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating
# characters.

###############################################################################

# longest substring -> sliding window -> use Dict for repeated char position
# Dict with key = char and val = latest_idx
# move start_idx if necessary

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1
        
        char_dict = dict()
        max_len = 0
        start_idx = 0 # starting index for the current substring
        for idx, char in enumerate(s):
            if char in char_dict: # found a repeated char
                char_prev_idx = char_dict[char]
                if char_prev_idx + 1 > start_idx: # move start_idx
                    # set the start idx to the right of the repeated char
                    start_idx = char_prev_idx + 1

            char_dict[char] = idx # update char idx in char_dict
                
            # update max_len
            max_len = max(max_len, idx - start_idx + 1)
            
        return max_len