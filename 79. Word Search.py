# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.

# Note: There will be some test cases with a board or a word larger than
# constraints to test if your solution is using pruning.

###############################################################################

# bfs: start from every position in board
# avoid revisit by tracking visited position
# return True if found answer

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        ans = [False]
        
        for i in range(m):
            for j in range(n):
                if self.dfs(0, i, j, word, board, visited):
                    return True
        return False
    
    def dfs(self, char_idx, i, j, word, board, visited):
        if char_idx == len(word):
            return True
        
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited[i][j] or word[char_idx] != board[i][j]:
            return False
        
        visited[i][j] = True
        found = self.dfs(char_idx + 1, i - 1, j, word, board, visited) \
        or self.dfs(char_idx + 1, i + 1, j, word, board, visited) \
        or self.dfs(char_idx + 1, i, j - 1, word, board, visited) \
        or self.dfs(char_idx + 1, i, j + 1, word, board, visited)
        visited[i][j] = False
        
        return found