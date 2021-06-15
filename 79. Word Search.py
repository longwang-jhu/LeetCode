# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if word
# exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where
# adjacent cells are horizontally or vertically neighboring. The same letter cell
# may not be used more than once.

################################################################################

# dfs: start from every position in board
# avoid revisit by tracking visited position
# return True if found answer

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        
        self.board = board
        self.word = word
        self.m, self.n = len(self.board), len(self.board[0])
        self.visited = set()
        self.dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # start from every pos
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(0, i, j):
                    return True
        return False
    
    def dfs(self, char_idx, i, j):
        # check valid
        if self.word[char_idx] != self.board[i][j]:
            return False
        
        if char_idx == len(self.word) - 1: # last char
            return True
        
        self.visited.add((i,j))
        
        found = False
        for dir_idx in range(4):
            i_next = i + self.dirs[dir_idx][0]
            j_next = j + self.dirs[dir_idx][1]
            if (0 <= i_next < self.m and 0 <= j_next < self.n
               and (i_next, j_next) not in self.visited):
                found = found or self.dfs(char_idx + 1, i_next, j_next)
        
        self.visited.remove((i,j))
        
        return found
