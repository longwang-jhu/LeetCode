# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.

###############################################################################

# dfs: start from every position in board
# avoid revisit by tracking visited position
# return True if found answer

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        
        self.board = board
        self.word = word
        self.m, self.n = len(self.board), len(self.board[0])
        self.is_visited = set()
        
        # start from every pos
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(0, i, j):
                    return True
        return False
    
    def dfs(self, char_idx, i, j):
        if char_idx == len(self.word):
            return True
        
        # check valid
        if i < 0 or i >= self.m or j < 0 or j >= self.n \
        or (i,j) in self.is_visited or self.word[char_idx] != self.board[i][j]:
            return False
        
        self.is_visited.add((i,j))
        found = self.dfs(char_idx + 1, i - 1, j) \
        or self.dfs(char_idx + 1, i + 1, j) \
        or self.dfs(char_idx + 1, i, j - 1) \
        or self.dfs(char_idx + 1, i, j + 1)
        self.is_visited.remove((i,j))
        
        return found