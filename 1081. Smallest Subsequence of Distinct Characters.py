# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

# Return the lexicographically smallest subsequence of s that contains all the
# distinct characters of s exactly once.

# Note: This question is the same as 316: https://leetcode.com/problems/remove-
# duplicate-letters/

################################################################################

# record last postion of each char
# use stack and pop previous chars when i) new char is smaller and ii) we can add the popped char back later

class Solution:
    def smallestSubsequence(self, s: str) -> str:
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
