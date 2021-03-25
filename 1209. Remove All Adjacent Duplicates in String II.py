# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

# Given a string s, a k duplicate removal consists of choosing k adjacent and
# equal letters from s and removing them causing the left and the right side of
# the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made.

# It is guaranteed that the answer is unique.

###############################################################################

# use stack and record the count
# use dummy element ('#', 0)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]] # dummy element
        
        for char in s:
            if stack[-1][0] == char: # duplicate
                stack[-1][1] += 1 # increment count
                if stack[-1][1] == k:
                    stack.pop() # remove the duplicate
            else: # no duplicate
                stack.append([char, 1])

        return ''.join(char * count for char, count in stack)