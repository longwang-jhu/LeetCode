# linear search: look for the first number < nums[0]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            if nums[i] < ans:
                return nums[i]
        return ans