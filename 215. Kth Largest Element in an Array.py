# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element in
# the array.

# Note that it is the kth largest element in the sorted order, not the kth
# distinct element.

################################################################################

# find nums.sort()[n-k]
# use quick_select

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k # find nums.sort()[n-k]
        self.quick_select(nums, 0, len(nums) - 1, k)
        return nums[k]

    def quick_select(self, nums, start, end, k):
        mid = start + (end - start) // 2
        piv = self.partition(nums, start, end, mid)
        if piv == k:
            return
        elif piv < k:
            self.quick_select(nums, piv + 1, end, k)
        else:
            self.quick_select(nums, start, piv - 1, k)
        return

    def partition(self, nums, start, end, piv):
        piv_val = nums[piv]
        # put piv to end
        nums[piv], nums[end] = nums[end], nums[piv]
        # put smaller number first
        store_idx = start
        for i in range(start, end):
            if nums[i] < piv_val:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx += 1
        # restore piv
        nums[end], nums[store_idx] = nums[store_idx], nums[end]
        return store_idx 
