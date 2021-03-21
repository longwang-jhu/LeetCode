# use a slow ptr and modify it on the go
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_ptr = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow_ptr]:
                slow_ptr += 1
                nums[slow_ptr] = nums[i]
        return slow_ptr + 1