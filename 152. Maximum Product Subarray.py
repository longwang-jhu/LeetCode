# https://leetcode.com/problems/maximum-product-subarray/

# Given an integer array nums, find a contiguous non-empty subarray within the
# array that has the largest product, and return the product.

# It is guaranteed that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

################################################################################

# num may < 0
# dp_max[i] = max_prod ending at nums[i]
# dp_min[i] = min_prod ending at nums[i]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        # init
        dp_max = [None] * n
        dp_min = [None] * n
        dp_max[0] = dp_min[0] = nums[0]
        
        # dp
        for i in range(1, n):
            if nums[i] > 0:
                dp_max[i] = max(nums[i], dp_max[i-1] * nums[i])
                dp_min[i] = min(nums[i], dp_min[i-1] * nums[i])
            elif nums[i] < 0:
                dp_max[i] = max(nums[i], dp_min[i-1] * nums[i])
                dp_min[i] = min(nums[i], dp_max[i-1] * nums[i])
            else:
                dp_max[i] = dp_min[i] = 0
        
        return max(dp_max)
