# https://leetcode.com/problems/single-number-ii/

# Given an integer array nums where every element appears three times except for
# one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only
# constant extra space.

################################################################################

# consider a 32-bit num and count how many 1 appears in each bit
# count %= 3 to remove three-appearance number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        
        # make all nums positive
        neg_sign_count = 0
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = -num
                neg_sign_count += 1
        
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1 == 1: # check if ith bit (from right) is 1
                    count += 1
            count %= 3 # remove three-appearance number
            ans |= (count << i) # make ith bit (from right) in ans to 1
                
        if neg_sign_count % 3 == 0:
            return ans
        else:
            return -ans
