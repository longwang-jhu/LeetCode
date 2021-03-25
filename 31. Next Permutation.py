# https://leetcode.com/problems/next-permutation/

# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest
# possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

###############################################################################

# find first a[i-1] < a[i] from right: 1, 2*, 5*, 4, 3
# swap a[i-1] with its next larger number after it: 1, 3*, 5, 4, 2*
# reverse numbers after a[i-1]: 1, 3, 2*, 4*, 5*

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find first a[i-1] < a[i] from right
        i = len(nums) - 1
        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # swap a[i-1] with its next larger number after it: 1, 3*, 5, 4, 2*
        if i - 1 >= 0:
            j = i
            while j <= len(nums) - 1 and nums[i-1] < nums[j]:
                j += 1
            # swap
            nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
        
        # reverse numbers after a[i-1]
        l = i
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1