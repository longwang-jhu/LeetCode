# https://leetcode.com/problems/spiral-matrix/

# Given an m x n matrix, return all elements of the matrix in spiral order.

###############################################################################

# one pass -> change dir if necessary

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        if m == 1: return matrix[0] # single row
        if n == 1: return [row[0] for row in matrix] # single col
        
        is_visited = set()
        # right, down, left, up
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        dir_idx = 0
        
        ans = []
        x, y = 0, 0
        for _ in range(m * n):
            ans.append(matrix[x][y])
            is_visited.add((x,y))
            
            # move to next pos
            x_next = x + dirs[dir_idx][0]
            y_next = y + dirs[dir_idx][1]
            
            # change dir if reach boundar or is_visited
            if x_next < 0 or x_next >= m \
            or y_next < 0 or y_next >= n \
            or (x_next, y_next) in is_visited:
                dir_idx = (dir_idx + 1) % 4
                x += dirs[dir_idx][0]
                y += dirs[dir_idx][1]
            else:
                x, y = x_next, y_next

        return ans