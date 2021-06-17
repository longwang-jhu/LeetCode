// https://leetcode.com/problems/shortest-bridge/

// In a given 2D binary array grid, there are two islands.  (An island is a
// 4-directionally connected group of 1s not connected to any other 1s.)

// Now, we may change 0s to 1s so as to connect the two islands together to form 1
// island.

// Return the smallest number of 0s that must be flipped.  (It is guaranteed that
// the answer is at least 1.)

////////////////////////////////////////////////////////////////////////////////

// use dfs to mark 1st island, and bfs to reach 2nd island
class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        m = grid.size(); n = grid[0].size();
        bool found1 = false;
        for (int i = 0; i < m; ++i) {
            if (found1) break;
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    dfs(i, j, grid);
                    found1 = true; break;
                }
            }
        }        
        // use bfs to reach 2nd island
        int ans = 0;
        while (!island1.empty()) {
            int nCurrLayer = island1.size();
            while (nCurrLayer--) {
                auto [i, j] = island1.front(); island1.pop();
                for (const auto& [iIncr, jIncr] : dirs) {
                    int iNext = i + iIncr, jNext = j + jIncr;
                    if (iNext >= 0 && iNext < m
                        && jNext >= 0 && jNext < n) {
                        if (grid[iNext][jNext] == 1) return ans;
                        if (grid[iNext][jNext] == 0) {
                            grid[iNext][jNext] = -1;
                            island1.push({iNext, jNext});
                        }
                    }
                }
            }
            ++ans; // move to next layer
        }
        return 0;
    }
private:
    int m, n;
    vector<pair<int, int>> dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    queue<pair<int, int>> island1;
    void dfs(int i, int j, vector<vector<int>>& grid) {
        grid[i][j] = -1; // mark for 1st island
        island1.push({i, j});
        for (const auto& [iIncr, jIncr] : dirs) {
            int iNext = i + iIncr, jNext = j + jIncr;
            if (iNext >= 0 && iNext < m && jNext >= 0 && jNext < n
                && grid[iNext][jNext] == 1) {
                dfs(iNext, jNext, grid);
            }
        }
        return;
    }
};
