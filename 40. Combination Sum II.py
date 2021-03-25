# https://leetcode.com/problems/combination-sum-ii/

# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

###############################################################################

# dfs: sort first, add child from start to end
# avoid duplicate: add child if first child OR != prev child

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.dfs(ans, 0, [], candidates, target)
        return ans
    
    def dfs(self, ans, start, holder, candidates, remain):
        if remain < 0:
            return
        if remain == 0:
            ans.append(holder.copy())
        
        for i in range(start, len(candidates)):
            if i == start or candidates[i] != candidates[i-1]: # avoid duplicates
                holder.append(candidates[i])
                self.dfs(ans, i + 1, holder, candidates, remain - candidates[i]) # use i + 1 since cannot reuse, set remain = remain - number
                holder.pop()