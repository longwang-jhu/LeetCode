# https://leetcode.com/problems/subsets/

# Given an integer array nums of unique elements, return all possible subsets
# (the power set).

# The solution set must not contain duplicate subsets. Return the solution in
# any order.

###############################################################################

# dfs: add child from start to end

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        self.dfs(ans, 0, [], nums)
        return ans
    
    def dfs(self, ans, start, holder, nums):
        ans.append(holder.copy())
        
        for i in range(start, len(nums)):
            holder.append(nums[i])
            self.dfs(ans, i + 1, holder, nums)
            holder.pop()