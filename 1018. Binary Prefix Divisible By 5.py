# https://leetcode.com/problems/binary-prefix-divisible-by-5/

# You are given a binary array nums (0-indexed).

# We define xi as the number whose binary representation is the subarray
# nums[0..i] (from most-significant-bit to least-significant-bit).

# Return an array of booleans answer where answer[i] is true if xi is divisible by
# 5.

################################################################################

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        num = 0
        for i in range(len(A)):
            num = num * 2 + A[i]
            ans.append(num % 5 == 0)
        return ans
