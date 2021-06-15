// https://leetcode.com/problems/shortest-bridge/

// In a given 2D binary array grid, there are two islands.  (An island is a
// 4-directionally connected group of 1s not connected to any other 1s.)

// Now, we may change 0s to 1s so as to connect the two islands together to form 1
// island.

// Return the smallest number of 0s that must be flipped.  (It is guaranteed that
// the answer is at least 1.)

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<pair<int, int>> dirs = {{0,-1}, {0,1}, {-1,0}, {1,0}};
    queue<pair<int, int>> points;
    
    int shortestBridge(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();       
        // use dfs to find first island and mark it as -1
        bool found1st = false;
        for (int x = 0; x < m; ++x) {
            if (found1st) break;
            for (int y = 0; y < n; ++y) {
                if (grid[x][y] == 1) {
                    dfs(grid, x, y);
                    found1st = true;
                    break;
                }
            }
        }        
        // use bfs to reach for second island
        int ans = 0;
        while (!points.empty()) {
            int nThisLayer = points.size();
            while (nThisLayer--) {
                auto [x, y] = points.front(); points.pop();
                for (int i = 0; i < 4; ++i) {
                    int xNext = x + dirs[i].first;
                    int yNext = y + dirs[i].second;
                    if (xNext >= 0 and xNext < m and yNext >= 0 and yNext < n) {
                        if (grid[xNext][yNext] == 1) return ans; // reach the 2nd island
                        if (grid[xNext][yNext] == 0) {
                            grid[xNext][yNext] = -1;
                            points.push({xNext, yNext});
                        }
                    }
                }
            }
            ++ans; // move to next layer
        }
        return 0;
    }
    
    void dfs(vector<vector<int>>& grid, int x, int y) {
        grid[x][y] = -1; // mark for first island
        points.push({x, y});
        for (int i = 0; i < 4; ++i) {
            int xNext = x + dirs[i].first;
            int yNext = y + dirs[i].second;
            if (xNext >= 0 and xNext < grid.size() and yNext >= 0 and yNext < grid[0].size()
                and grid[xNext][yNext] == 1) {
                dfs(grid, xNext, yNext);
            }
        }
        return;
    }
};
