# https://leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.

###############################################################################

# all combs -> DFS
# count n_left_p and n_right_p

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1: return []
        
        ans = []
        self.dfs(ans, [], 0, 0, n)
        return ans
    
    def dfs(self, ans, holder, n_left_p, n_right_p, n):
        if n_left_p == n and n_right_p == n:
            ans.append(''.join(holder))
            return
        
        if n_left_p < n:
            holder.append('(')
            self.dfs(ans, holder, n_left_p + 1, n_right_p, n)
            holder.pop()
        if n_left_p > n_right_p:
            holder.append(')')
            self.dfs(ans, holder, n_left_p, n_right_p + 1, n)
            holder.pop()