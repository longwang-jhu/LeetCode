# https://leetcode.com/problems/permutations-ii/

# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.

###############################################################################

# all unique combos -> sort, dfs -> add child that is not used
# is_used = [] for recording
# avoid duplicate: i) not used AND ii) first child OR (!= prev) OR (== prev, but prev is used)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0: return []
        
        nums.sort()
        self.ans = []
        self.holder = []
        self.used = set()
        self.nums = nums
        self.dfs()
        return self.ans
    
    def dfs(self):
        if len(self.holder) == len(self.nums):
            self.ans.append(self.holder.copy())
            return
        
        # generate child
        for i in range(len(self.nums)):
            # i) not used
            if i not in self.used:
                # ii) first child OR (!= prev) OR (== prev, but prev is used)
                if i == 0 or self.nums[i] != self.nums[i-1] or i - 1 in self.used:
                    self.holder.append(self.nums[i])
                    self.used.add(i)
                    
                    self.dfs()
                    
                    self.holder.pop()
                    self.used.remove(i)