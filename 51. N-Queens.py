# https://leetcode.com/problems/n-queens/

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.

###############################################################################

# all unique sol -> dfs -> place queen by row
# keep updating free position

# diag: (2n + 1) lines, row + col = i if (row, col) on diag[i], counting from top-left
# anti-diag: (2n + 1) lines, row - col + n - 1 = i if (row, col) on diag[i], counting from top-right

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        # init free positions
        col_free = [True] * n
        diag_free = [True] * (2 * n - 1)
        anti_diag_free = [True] * (2 * n - 1)
        
        self.dfs(ans, [], 0, n, col_free, diag_free, anti_diag_free)
        return ans
    
    def dfs(self, ans, holder, row, n, col_free, diag_free, anti_diag_free):
        if row == n:
            ans.append(holder.copy())
            return
        
        for col in range(n):
            if self.is_free(row, col, n, col_free, diag_free, anti_diag_free):
                # place queen
                holder_ele = ['.'] * n
                holder_ele[col] = 'Q'
                holder.append(''.join(holder_ele))
                
                # update free positions
                col_free[col] = False
                diag_free[row + col] = False
                anti_diag_free[row - col + n - 1] = False
                                
                # go to child
                self.dfs(ans, holder, row + 1, n, col_free, diag_free, anti_diag_free)
                
                # remove queen
                holder.pop()
                col_free[col] = True
                diag_free[row + col] = True
                anti_diag_free[row - col + n - 1] = True
    
    def is_free(self, row, col, n, col_free, diag_free, anti_diag_free):
        return col_free[col] and diag_free[row + col] and anti_diag_free[row - col + n - 1]