# binary search: [first part | second part]
# determine which part mid is in

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: # mid is in the first part
                left = mid
            else: # num[mid] < mid[right], mid is in the second part
                right = mid
        
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]