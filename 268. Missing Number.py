# https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity
# and O(n) runtime complexity?

################################################################################

# XOR 0,..., n with nums

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1 if nums[0] == 0 else 0
        
        ans = 0
        for i in range(1, n + 1):
            ans ^= i

        for num in nums:
            ans ^= num
        
        return ans
