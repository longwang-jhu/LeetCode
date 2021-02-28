# use numDict[idx] = value

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for idx, value in enumerate(nums):
            if (comp := target - value) not in numDict:
                # cannot find the complement, store the current value with its index
                numDict[value] = idx
            else:
                # found the complement, retrive the index
                return [numDict[comp], idx]