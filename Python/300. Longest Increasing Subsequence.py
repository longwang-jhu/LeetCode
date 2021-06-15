# https://leetcode.com/problems/longest-increasing-subsequence/

# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

###############################################################################

# dp[i] = longest increasing subseq ending at i
# update by checking all prev dp[j] such that nums[j] < nums[i]

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        dp = [1 for _ in range(n)]
        for right in range(1, n):
            for left in range(right): # from 0 to right - 1
                if nums[left] < nums[right]:
                    dp[right] = max(dp[right], dp[left] + 1)

        return max(dp)