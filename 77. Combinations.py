# https://leetcode.com/problems/combinations/

# Given two integers n and k, return all possible combinations of k numbers out of
# the range [1, n].

# You may return the answer in any order.

################################################################################

# dfs

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        
        self.ans = []
        self.holder = []
        
        self.dfs(0)
        
        return self.ans
    
    def dfs(self, i):
        if len(self.holder) == self.k:
            self.ans.append(self.holder.copy())
            return
        
        for j in range(i + 1, self.n + 1): # j = i+1...n
            self.holder.append(j)
            self.dfs(j)
            self.holder.pop()            
