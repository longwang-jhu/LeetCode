# https://leetcode.com/problems/n-queens/

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You
# may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.

################################################################################

# all unique sol -> dfs -> place queen by row
# keep updating free position

# diag: (2n + 1) lines, row - col + n - 1 = i if (row, col) on diag[i], counting from top-right
# anti-diag: (2n + 1) lines, row + col = i if (row, col) on diag[i], counting from top-left

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        
        # init free positions
        self.col_free = [True] * self.n
        self.diag_free = [True] * (2 * self.n - 1)
        self.anti_diag_free = [True] * (2 * self.n - 1)
        
        self.ans = []
        self.holder = []
        self.dfs(0)
        return self.ans
    
    def dfs(self, row):
        if row == self.n:
            self.ans.append(self.holder.copy())
            return
        
        for col in range(self.n):
            if self.is_free(row, col):
                # place queen
                holder_ele = ['.'] * self.n
                holder_ele[col] = 'Q'
                self.holder.append(''.join(holder_ele))
                
                # update free positions
                self.col_free[col] = False
                self.diag_free[row - col + self.n - 1] = False
                self.anti_diag_free[row + col] = False
                                
                # go to child
                self.dfs(row + 1)
                
                # remove queen
                self.holder.pop()
                self.col_free[col] = True
                self.diag_free[row - col + self.n - 1] = True
                self.anti_diag_free[row + col] = True
    
    def is_free(self, row, col):
        return self.col_free[col] and self.diag_free[row - col + self.n - 1] and self.anti_diag_free[row + col]
