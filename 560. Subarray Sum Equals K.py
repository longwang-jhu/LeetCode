# https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers nums and an integer k, return the total number of
# continuous subarrays whose sum equals to k.

###############################################################################

# pre_sums[i] = sum(sums[0...i-1])
# check if pre_sums[i] - k in pre_sums_dict

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return 1 if nums[0] == k else 0
        
        ans = 0
        # pre_sums_dict: key = pre_sums[i], val = counters
        pre_sums = defaultdict(int)
        pre_sums[0] = 1 # base case
        
        pre_sum = 0
        for i in range(len(nums)):
            # update pre_sum
            pre_sum += nums[i]
            
            if pre_sum - k in pre_sums: # found a solution
                ans += pre_sums[pre_sum - k]
            
            # update pre_sums
            pre_sums[pre_sum] += 1
        
        return ans