# https://leetcode.com/problems/sudoku-solver/

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# The '.' character indicates empty cells.

################################################################################

# dfs with return

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.dfs(0, 0)
        return
    
    def dfs(self, i, j):
        if i == 9: return True      
        if j == 9: return self.dfs(i + 1, 0)
        if self.board[i][j] != ".": return self.dfs(i, j + 1)
        
        for val in range(1, 10):
            if not self.is_valid(i, j, val): continue
            self.board[i][j] = str(val)
            if self.dfs(i, j + 1): return True
            self.board[i][j] = "."
        return False
    
    def is_valid(self, i, j, val): # check if can put val at (i,j)
        for k in range(9):
            if self.board[i][k] == str(val): return False
            if self.board[k][j] == str(val): return False
            if self.board[i//3 * 3 + k//3][j//3 * 3 + k%3] == str(val):
                return False
        return True
