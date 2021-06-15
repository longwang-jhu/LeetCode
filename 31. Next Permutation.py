# https://leetcode.com/problems/next-permutation/

# Implement next permutation, which rearranges numbers into the lexicographically
# next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest
# possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

################################################################################

# in-place 
# -> find first a[i-1] < a[i] from right: 1, 2*, (5, 4, 3)
# -> swap a[i-1] with its next number after it: 1, 3*, (5, 4, 2*)
# -> reverse numbers after a[i-1]: 1, 3, (2*, 4*, 5*)
# numbers in (...) are in decresing order until reverse

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1: return
        
        # find first a[i-1] < a[i] from right
        i = len(nums) - 1
        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i - 1 == -1: # no next permutation
            nums.reverse()
            return
        
        # swap a[i-1] with its next number after it: 1, 2*, (5, 4, 3*)
        j = len(nums) - 1
        while j > i - 1 and nums[j] <= nums[i - 1]:
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1] # swap
        
        # reverse numbers after a[i-1]
        l = i
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
