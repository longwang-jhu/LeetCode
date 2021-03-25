# https://leetcode.com/problems/remove-duplicate-letters/

# Given a string s, remove duplicate letters so that every letter appears once
# and only once. You must make sure your result is the smallest in
# lexicographical order among all possible results.

# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

###############################################################################

# record last postion of each char
# use stack and pop previous chars when i) new char is smaller and ii) we can add the popped char back later

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_pos = {}
        for idx, char in enumerate(s):
            last_pos[char] = idx
        
        stack = []
        for idx, char in enumerate(s):
            if char not in stack:
                # pop the previous chars if the new char is smaller
                # but only when we can add the popped char back: idx < last_pos[popped_char]
                while stack and char < stack[-1] and idx < last_pos[stack[-1]]:
                    stack.pop()
                stack.append(char)
        return ''.join(stack)