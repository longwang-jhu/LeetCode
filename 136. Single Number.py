# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity
# and without using extra memory?

###############################################################################

# use XOR: a^a = 0

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans