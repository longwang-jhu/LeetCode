// https://leetcode.com/problems/max-area-of-island/

// You are given an m x n binary matrix grid. An island is a group of 1's
// (representing land) connected 4-directionally (horizontal or vertical.) You may
// assume all four edges of the grid are surrounded by water.

// The area of an island is the number of cells with a value 1 in the island.

// Return the maximum area of an island in grid. If there is no island, return 0.

////////////////////////////////////////////////////////////////////////////////

// dfs
class Solution {
public:
    vector<vector<int>> dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.empty() or grid[0].empty()) return 0;
        
        int maxArea = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) {
                    maxArea = max(maxArea, dfs(grid, i, j));
                }
            }
        }
        return maxArea;
    }
    
    int dfs(vector<vector<int>> &grid, int i, int j) {
        grid[i][j] = 0;
        int area = 1;
        for (int dirIdx = 0; dirIdx < 4; ++dirIdx) {
            int iNext = i + dirs[dirIdx][0];
            int jNext = j + dirs[dirIdx][1];
            // check if child is legal
            if (iNext >=0 and iNext < grid.size() and jNext >= 0 and jNext < grid[0].size()
               and grid[iNext][jNext] == 1) {
                area += dfs(grid, iNext, jNext);
            }
        }        
        return area;
    }
};
