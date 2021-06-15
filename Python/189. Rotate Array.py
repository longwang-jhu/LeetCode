# https://leetcode.com/problems/rotate-array/

# Given an array, rotate the array to the right by k steps, where k is non-
# negative.

# Follow up:

###############################################################################

# reverse all -> reverse first k -> reverse last n - k

class Solution:
    def reverse(self, nums, left, right):
        while left < right:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            right -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)