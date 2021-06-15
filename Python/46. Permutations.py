# https://leetcode.com/problems/permutations/

# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.

###############################################################################

# all combos -> dfs -> add child that is not used

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0: return []
        
        self.nums = nums
        self.ans = []
        self.holder = []
        self.used = set()
        self.dfs()
        return self.ans
        
    def dfs(self):
        if len(self.holder) == len(self.nums):
            self.ans.append(self.holder.copy())
            return
        
        # generate child
        for num in self.nums:
            if num not in self.used: # no reuse
                self.holder.append(num)
                self.used.add(num)
                self.dfs()
                self.holder.pop()
                self.used.remove(num)