# https://leetcode.com/problems/sort-an-array/

# Given an array of integers nums, sort the array in ascending order.

################################################################################

# quick sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        
        # self.quick_sort_first(nums, 0, len(nums) - 1)
        # self.quick_sort_last(nums, 0, len(nums) - 1)
        self.quick_sort_mid(nums, 0, len(nums) - 1)
        return nums

    # pick first ele as pivot
    def quick_sort_first(self, nums, low, high):
        if low >= high: return

        left, right = low + 1, high
        piv_val = nums[low]

        while left <= right: # stop when left > right
            while left <= right and nums[left] <= piv_val: # search for larger value
                left += 1
            while left <= right and piv_val <= nums[right]: # search for smaller value
                right -= 1
            if left < right: # swap
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # swap piv_val with smaller value at right
        nums[low], nums[right] = nums[right], nums[low]

        # divide
        self.quick_sort_first(nums, low, right - 1)
        self.quick_sort_first(nums, right + 1, high)

    # pick last ele as pivot
    def quick_sort_last(self, nums, low, high):
        if low >= high: return

        left, right = low, high - 1
        piv_val = nums[high]

        while left <= right: # stop when left > right
            while left <= right and nums[left] <= piv_val: # search for larger value
                left += 1
            while left <= right and piv_val <= nums[right]: # search for smaller value
                right -= 1
            if left < right: # swap
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # swap piv_val with larger value at left
        nums[high], nums[left] = nums[left], nums[high]

        # divide
        self.quick_sort_last(nums, low, left - 1)
        self.quick_sort_last(nums, left + 1, high)

    # pick mid ele as pivot
    def quick_sort_mid(self, nums, low, high):
        if low >= high: return

        left, right = low, high
        mid = left + (right - left) // 2
        piv_val = nums[mid]

        while left <= right: # stop when left > right
            while left <= right and nums[left] <= piv_val: # search for larger value
                left += 1
            while left <= right and piv_val <= nums[right]: # search for smaller value
                right -= 1
            if left < right: # swap
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # determine piv position
        if right > mid: # smaller value on right
            nums[mid], nums[right] = nums[right], nums[mid]
            piv = right
        elif left < mid: # larger value on left
            nums[left], nums[mid] = nums[mid], nums[left]
            piv = left
        else:
            piv = mid

        self.quick_sort_mid(nums, low, piv - 1)
        self.quick_sort_mid(nums, piv + 1, high)
