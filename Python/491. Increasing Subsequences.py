# https://leetcode.com/problems/increasing-subsequences/

# Given an integer array nums, return all the different possible increasing
# subsequences of the given array with at least two elements. You may return
# the answer in any order.

# The given array may contain duplicates, and two equal integers should also be
# considered a special case of increasing sequence.

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