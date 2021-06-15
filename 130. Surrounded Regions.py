# https://leetcode.com/problems/surrounded-regions/

# Given an m x n matrix board containing 'X' and 'O', capture all regions
# surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

################################################################################

# dfs start from edges to mark connected 'O' -> 'S'
# change 'O' -> 'X' and 'S' -> 'O

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 1 or len(board[0]) == 1: return
        
        self.m, self.n = len(board), len(board[0])
        self.board = board
        self.dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # dfs start from edges
        for i in range(self.m):
            if self.board[i][0] == "O": # first col
                self.dfs(i, 0)
            if self.board[i][self.n - 1] == "O": # last col
                self.dfs(i, self.n - 1)
        for j in range(self.n):
            if self.board[0][j] == "O": # first row
                self.dfs(0, j)
            if self.board[self.m - 1][j] == "O": # last row
                self.dfs(self.m - 1, j)
        
        # change 'O' -> 'X' and 'S' -> 'O'
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                elif self.board[i][j] == 'S':
                    self.board[i][j] = 'O'
        return
    
    def dfs(self, i, j):
        self.board[i][j] = "S"
        for dir_idx in range(4):
            i_next = i + self.dirs[dir_idx][0]
            j_next = j + self.dirs[dir_idx][1]
            if (0 <= i_next < self.m and 0 <= j_next < self.n
                and self.board[i_next][j_next] == "O"):
                self.dfs(i_next, j_next)
