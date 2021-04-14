# https://leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.

###############################################################################

# rotate = transpose + flip_left_right

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # tranpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        # flip_left_right
        for i in range(n):
            for j in range(n // 2):
                matrix[i][-j-1], matrix[i][j] = matrix[i][j], matrix[i][-j-1]