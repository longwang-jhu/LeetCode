# https://leetcode.com/problems/rotate-string/

# We are given two strings, A and B.

# A shift on A consists of taking string A and moving the leftmost character to
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
# after one shift on A. Return True if and only if A can become B after some
# number of shifts on A.

# Note:

###############################################################################

# check if B is a substring of A + A
# O(n^2): use B in A + A

# O(n): rolling Hash
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A