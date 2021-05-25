# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# You can return the answer in any order.

###############################################################################

# for every num, search for comp = target - num
# dict: key = num, val = idx

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_dict = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp not in num_idx_dict:
                # cannot find comp, store num and idx
                num_idx_dict[num] = idx
            else:
                # found comp, return idx
                return [num_idx_dict[comp], idx]