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
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        m = grid.size(); n = grid[0].size();
        int maxArea = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    maxArea = max(maxArea, dfs(i, j, grid));
                }
            }
        }
        return maxArea;
    }
private:
    int m, n;
    vector<pair<int, int>> dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    int dfs(int i, int j, vector<vector<int>>& grid) {
        grid[i][j] = 0;
        int area = 1;
        for (const auto& [iIncr, jIncr] : dirs) {
            int iNext = i + iIncr, jNext = j + jIncr;
            if (iNext >= 0 && iNext < m && jNext >= 0 && jNext < n
               && grid[iNext][jNext] == 1) {
                area += dfs(iNext, jNext, grid);
            }
        }
        return area;
    }
};
