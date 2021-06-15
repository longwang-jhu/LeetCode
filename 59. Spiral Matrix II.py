# https://leetcode.com/problems/spiral-matrix-ii/

# Given a positive integer n, generate an n x n matrix filled with elements from 1
# to n2 in spiral order.

################################################################################

# one pass -> change direction if necessary

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n: return []
        if n == 1: return [[1]]
        
        matrix = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        # right, down, left, up
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        dir_idx = 0
        
        pos = (0, 0)
        for i in range(1, n * n + 1):
            matrix[pos[0]][pos[1]] = i
            visited[pos[0]][pos[1]] = True
            
            # move to next pos
            dir = dirs[dir_idx]
            pos_next = (pos[0] + dir[0], pos[1] + dir[1])
            # change direction if visited
            if 0 <= pos_next[0] < n and 0 <= pos_next[1] < n \
            and not visited[pos_next[0]][pos_next[1]]:
                pos = pos_next
            else:
                dir_idx = (dir_idx + 1) % 4
                dir = dirs[dir_idx]
                pos = (pos[0] + dir[0], pos[1] + dir[1])
        
        return matrix
