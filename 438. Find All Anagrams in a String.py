# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.

###############################################################################

# sliding window -> check window_counter == target_counter

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        
        ans = []
        window = Counter()
        n_valid_chars = 0 # for fast comparsion
        
        # sliding window
        left = right = 0
        while right < len(s):
            # update window
            new_char = s[right]
            if new_char in target:
                window[new_char] += 1
                if window[new_char] == target[new_char]:
                    n_valid_chars += 1
            
            # shrink window
            while right - left + 1 >= len(p):
                # check if window is good
                if n_valid_chars == len(target):
                    ans.append(left)
                
                # update window
                old_char = s[left]
                if old_char in target:
                    if window[old_char] == target[old_char]:
                        n_valid_chars -= 1
                    window[old_char] -= 1
                left += 1
            
            # expand window
            right += 1
            
        return ans