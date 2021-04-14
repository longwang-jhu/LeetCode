# https://leetcode.com/problems/spiral-matrix/

# Given an m x n matrix, return all elements of the matrix in spiral order.

###############################################################################

# one pass -> change direction if necessary

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        if len(matrix) == 1: return matrix[0]
        if len(matrix[0]) == 1:
            return [col[0] for col in matrix]
        
        n_row, n_col = len(matrix), len(matrix[0])        
        visited = [[False] * n_col for _ in range(n_row)]
        # right, down, left, up
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        dir_idx = 0
        
        ans = []
        pos = (0, 0)
        for _ in range(n_row * n_col):
            ans.append(matrix[pos[0]][pos[1]])
            visited[pos[0]][pos[1]] = True
            
            # move to next pos
            dir = dirs[dir_idx]
            pos_next = (pos[0] + dir[0], pos[1] + dir[1])
            # change direction if visited
            if 0 <= pos_next[0] < n_row and 0 <= pos_next[1] < n_col \
            and not visited[pos_next[0]][pos_next[1]]:
                pos = pos_next
            else:
                dir_idx = (dir_idx + 1) % 4
                dir = dirs[dir_idx]
                pos = (pos[0] + dir[0], pos[1] + dir[1])
        
        return ans
                
                
                
            