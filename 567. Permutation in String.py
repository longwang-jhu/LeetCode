# https://leetcode.com/problems/permutation-in-string/

# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.

###############################################################################

# sliding windown -> check window_counter == target_counter

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        
        # sliding window
        window = Counter()
        n_valid_chars = 0

        left = right = 0
        while right < len(s2):
            # update window
            new_char = s2[right]
            if new_char in target: # useful char
                window[new_char] += 1
                if window[new_char] == target[new_char]:
                    n_valid_chars += 1 # for fast comparison
            
            # shrink window
            while right - left + 1 >= len(s1):
                # check if window is good
                if n_valid_chars == len(target):
                    return True
                
                old_char = s2[left]
                if old_char in target:
                    if window[old_char] == target[old_char]:
                        n_valid_chars -= 1
                    window[old_char] -= 1
                left += 1
            
            # expand window
            right += 1
        
        # no solution found
        return False