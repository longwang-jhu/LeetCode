// https://leetcode.com/problems/number-of-islands/

// Given an m x n 2D binary grid grid which represents a map of '1's (land) and
// '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands
// horizontally or vertically. You may assume all four edges of the grid are all
// surrounded by water.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<pair<int, int>> dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j); ++ans;
                }
            }
        }
        return ans;
    }
    
    void dfs(vector<vector<char>>& grid, int _i, int _j) {
        queue<pair<int, int>> todo; todo.push(make_pair(_i, _j));
        grid[_i][_j] = '0';
        while (!todo.empty()) {
            auto [i, j] = todo.front(); todo.pop();
            for (auto [iIncr, jIncr] : dirs) {
                int iNext = i + iIncr;
                int jNext = j + jIncr;
                if (iNext >= 0 and iNext < grid.size() and jNext >= 0 and jNext < grid[0].size()
                   and grid[iNext][jNext] == '1') {
                    todo.push(make_pair(iNext, jNext));
                    grid[iNext][jNext] = '0';
                }
            }
        }
        return;
    }
};
