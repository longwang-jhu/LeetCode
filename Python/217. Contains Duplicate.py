# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.

###############################################################################

# set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False