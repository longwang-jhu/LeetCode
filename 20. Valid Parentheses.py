# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.

# An input string is valid if:

###############################################################################

# make a tracker list and pop the last element if there is a match

class Solution:
    def isValid(self, s: str) -> bool:
        tracker = []
        for char in s:
            if char in ['(', '[', '{']:
                tracker.append(char)
            elif len(tracker) == 0:
                return False
            elif char == ')' and tracker[-1] != '(':
                return False
            elif char == ']' and tracker[-1] != '[':
                return False
            elif char == '}' and tracker[-1] != '{':
                return False
            else:
                tracker.pop()
        return len(tracker) == 0