# https://leetcode.com/problems/letter-case-permutation/

# Given a string s, we can transform every letter individually to be lowercase or
# uppercase to create another string.

# Return a list of all possible strings we could create. You can return the output
# in any order.

################################################################################

# dfs

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S: return []
        
        self.n = len(S)
        self.S = S
        self.ans = []
        self.holder = []
        
        self.dfs(0)
        return self.ans
    
    def dfs(self, pos):
        if len(self.holder) == self.n:
            self.ans.append(''.join(self.holder))
            return
        
        if "0" <= self.S[pos] <= "9": # move to next pos
            self.holder.append(self.S[pos])
            self.dfs(pos + 1)
            self.holder.pop()
        else:
            for char in [self.S[pos].lower(), self.S[pos].upper()]:
                self.holder.append(char)
                self.dfs(pos + 1)
                self.holder.pop()
