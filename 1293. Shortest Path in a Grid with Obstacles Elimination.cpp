// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

// Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one
// step, you can move up, down, left or right from and to an empty cell.

// Return the minimum number of steps to walk from the upper left corner (0, 0) to
// the lower right corner (m-1, n-1) given that you can eliminate at most k
// obstacles. If it is not possible to find such walk return -1.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        if (m == 1 and n == 1) return 0;
        vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        // queue = {(x, y, obstacles)}
        queue<tuple<int, int, int>> q; q.push(make_tuple(0, 0, k));
        vector<vector<vector<bool>>> visited(m, vector<vector<bool>>(n, vector<bool>(k + 1, false)));
        visited[0][0][k] = true;
       
        int step = 0;
        while (!q.empty()) {
            int nThisLayer = q.size();
            while (nThisLayer--) {
                auto [xThis, yThis, obsThis] = q.front(); q.pop();
                // generate next step
                for (auto& [xIncr, yIncr] : dirs) {
                    int xNext = xThis + xIncr;
                    int yNext = yThis + yIncr;
                    if (xNext >= 0 and xNext < m and yNext >= 0 and yNext < n) {
                        // check if reach end
                        if (xNext == m - 1 and yNext == n - 1) return ++step;
                        
                        // add to queue depending on obsThis
                        if (grid[xNext][yNext] == 1 and obsThis > 0) {
                            if (!visited[xNext][yNext][obsThis - 1]) {
                                q.push(make_tuple(xNext, yNext, obsThis - 1));
                                visited[xNext][yNext][obsThis - 1] = true;
                            }
                        } else if (grid[xNext][yNext] == 0) {
                            if (!visited[xNext][yNext][obsThis]) {
                                q.push(make_tuple(xNext, yNext, obsThis));
                                visited[xNext][yNext][obsThis] = true;
                            }
                        }
                    }
                }
            }
            ++step;
        }
        return -1;
    }
};
