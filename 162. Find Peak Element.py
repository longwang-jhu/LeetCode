# Binary search: look for nums[mid] > nums[mid + 1]

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        
        if nums[left] < nums[right]:
            return right
        elif nums[left] > nums[right]:
            return left