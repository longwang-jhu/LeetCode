# https://leetcode.com/problems/pacific-atlantic-water-flow/

# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and
# the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea level
# of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height is
# less than or equal to the current cell's height. Water can flow from any cell
# adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes
# that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic
# oceans.

################################################################################

# dfs from ocean to land
# use is_visited and start from boundary

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.m, self.n = len(heights), len(heights[0])
        self.dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        visited_pac = set()
        visited_atl = set()
        
        for j in range(self.n):
            self.dfs(0, j, visited_pac, 0) # first row
            self.dfs(self.m - 1, j, visited_atl, 0) # last row
        for i in range(self.m):
            self.dfs(i, 0, visited_pac, 0) # first column
            self.dfs(i, self.n - 1, visited_atl, 0) # last column
                
        return list(visited_pac & visited_atl)

    def dfs(self, x, y, visited, ground_level):
        # check if can flow backwards
        if self.heights[x][y] < ground_level:
            return
        
        visited.add((x,y))
        for dir_idx in range(4):
            x_next = x + self.dirs[dir_idx][0]
            y_next = y + self.dirs[dir_idx][1]
            if (0 <= x_next < self.m and 0 <= y_next < self.n
                and (x_next, y_next) not in visited
               ):
                self.dfs(x_next, y_next, visited, self.heights[x][y])
