# use slow_ptr and count number of duplicates

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_ptr = 0
        count = 0 # count for dulicates
        for i in range(1, len(nums)):
            if nums[i] != nums[slow_ptr]: # no duplicate
                slow_ptr += 1
                nums[slow_ptr] = nums[i]
                count = 0
            elif count == 0: # duplicate, but the first time
                slow_ptr += 1
                nums[slow_ptr] = nums[i]
                count += 1
        
        return slow_ptr + 1