# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# You can return the answer in any order.

###############################################################################

# search for num pairs -> Dict
# Dict with key = value, val = idx
# for every num, look for its complement value in Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp not in num_dict:
                # cannot find the complement, store the current value with its index
                num_dict[num] = idx
            else:
                # found the complement, retrive the index
                return [num_dict[comp], idx]