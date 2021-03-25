# https://leetcode.com/problems/permutations-ii/

# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.

###############################################################################

# dfs: sort first, add all unused as child
# use is_used = [] to record if child has been used or not
# avoid duplicate: i) not used AND ii) i == 0 OR (!= prev) OR (== prev, but prev is used)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0: return []
        
        nums.sort()
        ans = []
        is_used = [False] * len(nums) # to record if num is used
        self.dfs(ans, [], nums, is_used)
        return ans
    
    def dfs(self, ans, holder, nums, is_used):
        if len(holder) == len(nums):
            ans.append(holder.copy())
            return
        
        # generate child
        for i in range(len(nums)):
            if not is_used[i]: # i) not used
                if i == 0 or nums[i] != nums[i-1] or is_used[i-1]: # ii) i == 0 OR (!= prev) OR (== prev, but prev is used)
                    holder.append(nums[i])
                    is_used[i] = True
                    self.dfs(ans, holder, nums, is_used)
                    holder.pop()
                    is_used[i] = False