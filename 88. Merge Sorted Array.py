# https://leetcode.com/problems/merge-sorted-array/

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing
# order, and two integers m and n, representing the number of elements in nums1
# and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be
# stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged, and the
# last n elements are set to 0 and should be ignored. nums2 has a length of n.

################################################################################

# start from the last numbers, move the larger one to end

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2, end = m - 1, n - 1, m + n - 1
        
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] >= nums2[i2]: # move nums[i1] to end
                nums1[end] = nums1[i1]
                i1 -= 1
            else:
                nums1[end] = nums2[i2]
                i2 -= 1
            end -= 1
        
        if i1 == -1 and i2 >= 0: # no more nums1
            nums1[:i2+1] = nums2[:i2+1]
        
        return
