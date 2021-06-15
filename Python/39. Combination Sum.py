# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target
# is less than 150 combinations for the given input.

###############################################################################

# all unique combos -> sort and dfs
# unlimited times -> don't incr i when go to child

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.dfs(ans, [], 0, candidates, target)
        return ans
    
    def dfs(self, ans, holder, start_idx, candidates, remain):
        if remain < 0:
            return
        if remain == 0:
            ans.append(holder.copy())
            return
        
        for i in range(start_idx, len(candidates)):
            holder.append(candidates[i])
            # use i since can reuse, set remain = remain - number
            self.dfs(ans, holder, i, candidates, remain - candidates[i])
            holder.pop()