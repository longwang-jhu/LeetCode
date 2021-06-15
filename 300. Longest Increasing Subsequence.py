# https://leetcode.com/problems/longest-increasing-subsequence/

# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some
# or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

################################################################################

# dp[i] = longest increasing subseq of nums[0...i], must use nums[i]
# update by checking all prev dp[j] such that nums[j] < nums[i]

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        
        # base
        n = len(nums)
        dp = [1] * n
        
        # dp
        for i in range(1, n):
            for j in range(i): # j = 0...i-1
                if nums[j] < nums[i]: # append nums[i] in subseq
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
