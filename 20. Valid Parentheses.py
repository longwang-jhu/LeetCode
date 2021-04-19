# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.

# An input string is valid if:

###############################################################################

# stack

class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 0: return True
        if len(s) == 1: return False
        
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            elif not stack: # no match for ')', ']', '}'
                return False
            elif char == ')' and stack[-1] != '(':
                return False
            elif char == ']' and stack[-1] != '[':
                return False
            elif char == '}' and stack[-1] != '{':
                return False
            else:
                stack.pop()
        
        return True if not stack else False