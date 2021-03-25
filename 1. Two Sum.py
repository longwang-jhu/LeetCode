# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# You can return the answer in any order.

###############################################################################

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