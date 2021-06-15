# https://leetcode.com/problems/combination-sum-ii/

# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate numbers
# sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

################################################################################

# all unique combos -> sort and dfs
# avoid duplicate: add child if first child or != prev child

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
            if i == start_idx or candidates[i] != candidates[i-1]: # avoid duplicate
                holder.append(candidates[i])
                # use i + 1 since cannot reuse, set remain = remain - number
                self.dfs(ans, holder, i + 1, candidates, remain - candidates[i])
                holder.pop()
