# https://leetcode.com/problems/increasing-subsequences/

# Given an integer array, your task is to find all the different possible
# increasing subsequences of the given array, and the length of an increasing
# subsequence should be at least 2.

###############################################################################

# dfs(idx), generate child for i >= idx and when holder[-1] <= nums
# use set of tuples to avoid replicate

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        self.dfs(ans, 0, [], nums)
        return ans
    
    def dfs(self, ans, idx, holder, nums):      
        if len(holder) >= 2:
            ans.add(tuple(holder))
        
        # generate child
        for i in range(idx, len(nums)):
            # want to add nums[i] into holder
            if len(holder) == 0 or holder[-1] <= nums[i]:
                holder.append(nums[i])
                self.dfs(ans, i + 1, holder, nums)
                holder.pop()