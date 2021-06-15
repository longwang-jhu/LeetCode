# https://leetcode.com/problems/reverse-string-ii/

# Given a string s and an integer k, reverse the first k characters for every
# 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are
# less than 2k but greater than or equal to k characters, then reverse the
# first k characters and left the other as original.

###############################################################################

# use range(0, n, 2k)

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)