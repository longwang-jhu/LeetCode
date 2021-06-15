# https://leetcode.com/problems/search-a-2d-matrix/

# Write an efficient algorithm that searches for a value in an m x n matrix. This
# matrix has the following properties:

################################################################################

# Binary search on a long list

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])
        left = 0
        right = n_row * n_col - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            idx_row, idx_col = divmod(mid, n_col)
            num = matrix[idx_row][idx_col]
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            elif target < num:
                right = mid - 1
        
        return False
