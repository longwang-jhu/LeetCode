# https://leetcode.com/problems/max-area-of-island/

# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You may
# assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

################################################################################

# dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        
        max_area = 0
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.dirs = [(0,-1), (1,0), (0,1), (-1,0)]
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(i,j))
        
        return max_area
    
    def dfs(self, i, j):
        self.grid[i][j] = 0
        area = 1
        # generate child
        for idx in range(4):
            i_next = i + self.dirs[idx][0]
            j_next = j + self.dirs[idx][1]
            if 0 <= i_next < self.m and 0 <= j_next < self.n \
            and self.grid[i_next][j_next] == 1:
                area += self.dfs(i_next, j_next)
        return area
