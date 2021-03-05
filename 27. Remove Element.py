# use a slow idx and modify nums[slowIdx] on the go
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slowIdx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slowIdx] = nums[i]
                slowIdx += 1
        return slowIdx