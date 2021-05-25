# https://leetcode.com/problems/binary-prefix-divisible-by-5/

# Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to
# A[i] interpreted as a binary number (from most-significant-bit to least-
# significant-bit.)

# Return a list of booleans answer, where answer[i] is true if and only if N_i
# is divisible by 5.

# Example 1:

# Example 2:

# Example 3:

# Example 4:

###############################################################################

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        num = 0
        for i in range(len(A)):
            num = num * 2 + A[i]
            ans.append(num % 5 == 0)
        return ans