# https://leetcode.com/problems/merge-sorted-array/

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n
# respectively. You may assume that nums1 has a size equal to m + n such that
# it has enough space to hold additional elements from nums2.

###############################################################################

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