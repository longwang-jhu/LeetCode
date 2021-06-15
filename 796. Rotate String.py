# https://leetcode.com/problems/rotate-string/

# We are given two strings, s and goal.

# A shift on s consists of taking string s and moving the leftmost character to
# the rightmost position. For example, if s = 'abcde', then it will be 'bcdea'
# after one shift on s. Return true if and only if s can become goal after some
# number of shifts on s.

# Note:

################################################################################

# check if B is a substring of A + A
# O(n^2): use B in A + A

# O(n): rolling Hash
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A
