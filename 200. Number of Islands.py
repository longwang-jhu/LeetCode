# https://leetcode.com/problems/number-of-islands/

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.

################################################################################

# bfs -> use is_visited and start from not is_visited and val == "1"

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.is_visited = [[False] * self.n for _ in range(self.m)]
        self.dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == "1" and not self.is_visited[i][j]:
                    self.bfs(i,j)
                    n_islands += 1
        
        return n_islands
    
    def bfs(self, x, y):
        queue = deque([(x,y)])
        self.is_visited[x][y] = True
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in self.dirs:
                x_next = x + delta_x
                y_next = y + delta_y
                
                # check if valid
                if x_next < 0 or x_next >= self.m or y_next < 0 or y_next >= self.n:
                    continue
                if self.grid[x][y] == "0" or self.is_visited[x_next][y_next]:
                    continue
                
                queue.append((x_next, y_next))
                self.is_visited[x_next][y_next] = True
