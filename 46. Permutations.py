# https://leetcode.com/problems/permutations/

# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.

###############################################################################

# dfs: add all as child
# skip those already in holder

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0: return []
        
        ans = []
        self.dfs(ans, [], nums)
        return ans
        
    def dfs(self, ans, holder, nums):
        if len(holder) == len(nums):
            ans.append(holder.copy())
            return
        
        # generate child
        for num in nums:
            if num not in holder: # all nums are distinct
                holder.append(num)
                self.dfs(ans, holder, nums)
                holder.pop()