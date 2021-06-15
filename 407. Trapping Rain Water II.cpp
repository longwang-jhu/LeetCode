// https://leetcode.com/problems/trapping-rain-water-ii/

// Given an m x n integer matrix heightMap representing the height of each unit
// cell in a 2D elevation map, return the volume of water it can trap after
// raining.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    typedef tuple<int, int, int> point;
    vector<pair<int, int>> dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    int trapRainWater(vector<vector<int>>& heightMap) {
        int m = heightMap.size(), n = heightMap[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        // use min pq to record height, put in edges first
        priority_queue<point, vector<point>, greater<point>> todo;
        for (int j = 0; j < n; ++j) {
            todo.push(make_tuple(heightMap[0][j], 0, j)); visited[0][j] = true;
            todo.push(make_tuple(heightMap[m - 1][j], m - 1, j)); visited[m - 1][j] = true;
        }
        for (int i = 1; i < m - 1; ++i) {
            todo.push(make_tuple(heightMap[i][0], i, 0)); visited[i][0] = true;
            todo.push(make_tuple(heightMap[i][n - 1], i, n - 1)); visited[i][n - 1] = true;
        }
        
        int ans = 0;
        int groundLevel = INT_MIN;
        
        while (!todo.empty()) {
            auto [height, i, j] = todo.top(); todo.pop();
            groundLevel = max(groundLevel, height);
            
            for (auto [iIncr, jIncr] : dirs) {
                int iNext = i + iIncr, jNext = j + jIncr;
                if (iNext >= 0 and iNext < m and jNext >= 0 and jNext < n
                   and !visited[iNext][jNext]) {
                    // trap water only when ground level is higher
                    ans += max(0, groundLevel - heightMap[iNext][jNext]);
                    todo.push(make_tuple(heightMap[iNext][jNext], iNext, jNext));
                    visited[iNext][jNext] = true;
                }
            }
        }
        return ans;
    }
};
