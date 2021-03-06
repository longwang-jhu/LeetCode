# binary search: [first part | second part]
# set right -= 1 if cannot decide which part mid is in

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] > nums[right]: # mid is in the first part
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            elif nums[mid] < nums[right]: # mid is in the second part
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                right -= 1
        
        return nums[left] == target or nums[right] == target