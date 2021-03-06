# binary search: find first position >= target

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid
            elif nums[mid] < target:
                left = mid
        
        if nums[left] >= target:
            return left
        elif nums[right] >= target:
            return right
        else:
            return len(nums)