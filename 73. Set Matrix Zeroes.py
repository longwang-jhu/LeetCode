# https://leetcode.com/problems/set-matrix-zeroes/

# Given an m x n matrix. If an element is 0, set its entire row and column to
# 0. Do it in-place.

# Follow up:

###############################################################################

# use set to record positions of zeros

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        return self.setZeros_const_space(matrix)
        
        m, n = len(matrix), len(matrix[0])
        
        # recode positions of zeroes
        row_set = set()
        col_set = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        
        # modify matrix
        for i in range(m):
            for j in range(n):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0
        return
    
    def setZeros_const_space(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        # use first row and col as flag to record zeroes
        set_first_row = False
        set_first_col = False
        for i in range(m):
            if matrix[i][0] == 0:
                set_first_col = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                set_first_row = True
                break
        
        # record flag
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        # modify matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # set first row or col
        if set_first_row:
            for j in range(n):
                matrix[0][j] = 0
        if set_first_col:
            for i in range(m):
                matrix[i][0] = 0
        
        return