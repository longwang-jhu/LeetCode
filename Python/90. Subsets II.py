# https://leetcode.com/problems/subsets-ii/

# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in
# any order.

###############################################################################

# dfs: sort first, add child from start to end
# avoid duplicate: add child if first child OR != prev child

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.dfs(ans, 0, [], nums)
        return ans
        
    
    def dfs(self, ans, start, holder, nums):
        ans.append(holder.copy())
        
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[i-1]: # add child if != prev child
                holder.append(nums[i])
                self.dfs(ans, i + 1, holder, nums)
                holder.pop()