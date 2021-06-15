# https://leetcode.com/problems/count-and-say/

# The count-and-say sequence is a sequence of digit strings defined by the
# recursive formula:

# To determine how you "say" a digit string, split it into the minimal number of
# groups so that each group is a contiguous section all of the same character.
# Then for each group, say the number of characters, then say the character. To
# convert the saying into a digit string, replace the counts with a number and
# concatenate every saying.

# For example, the saying and conversion for digit string "3322251":

# Given a positive integer n, return the nth term of the count-and-say sequence.

################################################################################

# recursive -> do what the question says

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        
        saying = self.countAndSay(n - 1)
        ans = ""
        
        latest_char = saying[0]
        count = 0
        
        for char in saying:
            if char == latest_char: # same char
                count += 1
            else:
                ans += str(count) + latest_char
                latest_char = char # reset
                count = 1
        ans += str(count) + latest_char # for last char
        return ans
