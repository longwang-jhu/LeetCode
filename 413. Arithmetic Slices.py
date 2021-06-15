# https://leetcode.com/problems/arithmetic-slices/

# An integer array is called arithmetic if it consists of at least three elements
# and if the difference between any two consecutive elements is the same.

# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

################################################################################

# dp[i] = number of subarrays in nums[0...i], must use nums[i]
# if can append nums[i]: dp[i] = dp[i-1] + 1 (shift + append)

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        
        n = len(nums)
        dp = [0] * n
        
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        
        return sum(dp)
