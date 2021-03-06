# binary search: [first part | second part]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] < nums[mid]: # mid is in the first part
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else: # mid is in the second part
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1