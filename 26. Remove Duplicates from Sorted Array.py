# use a slow idx and modify it on the go
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowIdx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slowIdx]:
                slowIdx += 1
                nums[slowIdx] = nums[i]
        return slowIdx + 1