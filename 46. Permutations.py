# https://leetcode.com/problems/permutations/

# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.

###############################################################################

# all combos -> dfs -> add child that is not used

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0: return []
        
        ans = []
        is_used = set()
        self.dfs(ans, [], nums, is_used)
        return ans
        
    def dfs(self, ans, holder, nums, is_used):
        if len(holder) == len(nums):
            ans.append(holder.copy())
            return
        
        # generate child
        for num in nums:
            if num not in is_used: # no reuse
                holder.append(num)
                is_used.add(num)
                self.dfs(ans, holder, nums, is_used)
                holder.pop()
                is_used.remove(num)