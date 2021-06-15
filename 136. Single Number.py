# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except for
# one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only
# constant extra space.

################################################################################

# use XOR: a^a = 0

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans
