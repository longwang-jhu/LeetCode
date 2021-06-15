# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

# Given an unsorted array of integers nums, return the length of the longest
# continuous increasing subsequence (i.e. subarray). The subsequence must be
# strictly increasing.

# A continuous increasing subsequence is defined by two indices l and r (l < r)
# such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l
# <= i < r, nums[i] < nums[i + 1].

################################################################################

# greedy: record count and reset when not strictly increasing

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        max_count = 1
        count = 1
        for i in range(1, len(nums)): # skip the first ele
            if nums[i] > nums[i-1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1 # reset
        return max(max_count, count)
