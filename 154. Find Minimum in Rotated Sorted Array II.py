# binary search: [first part | second part]
# set right -= 1 if cannot decide which part mid is in

# linear search: look for the first number < nums[0]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: # mid is in the first part
                left = mid
            elif nums[mid] < nums[right]: # mid is in the second part
                right = mid
            else:
                right -= 1
        
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
        
        # linear search
        ans = nums[0]
        for i in range(len(nums)):
            if nums[i] < ans:
                return nums[i]
        return ans