// https://leetcode.com/problems/pacific-atlantic-water-flow/

// There is an m x n rectangular island that borders both the Pacific Ocean and
// Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and
// the Atlantic Ocean touches the island's right and bottom edges.

// The island is partitioned into a grid of square cells. You are given an m x n
// integer matrix heights where heights[r][c] represents the height above sea level
// of the cell at coordinate (r, c).

// The island receives a lot of rain, and the rain water can flow to neighboring
// cells directly north, south, east, and west if the neighboring cell's height is
// less than or equal to the current cell's height. Water can flow from any cell
// adjacent to an ocean into the ocean.

// Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes
// that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic
// oceans.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<pair<int, int>> dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<vector<bool>> visitedP(m, vector(n, false));
        vector<vector<bool>> visitedA(m, vector(n, false));
        for (int i = 0; i < m; ++i) {
            if (!visitedP[i][0]) dfs(heights, visitedP, i, 0);
            if (!visitedA[i][n-1]) dfs(heights, visitedA, i, n - 1);
        }
        for (int j = 0; j < n; ++j) {
            if (!visitedP[0][j]) dfs(heights, visitedP, 0, j);
            if (!visitedA[m-1][j]) dfs(heights, visitedA, m-1, j);
        }
        
        vector<vector<int>> ans;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (visitedP[i][j] and visitedA[i][j]) ans.push_back({i,j});
            }
        }
        return ans;
    }
    
    void dfs(const vector<vector<int>> &heights, vector<vector<bool>> &visited, int i, int j) {
        visited[i][j] = true;
        for (auto [iIncr, jIncr] : dirs) {
            int iNext = i + iIncr, jNext = j + jIncr;
            if (iNext >= 0 and iNext < heights.size() and jNext >= 0 and jNext < heights[0].size()
               and !visited[iNext][jNext] and heights[iNext][jNext] >= heights[i][j]) {
                dfs(heights, visited, iNext, jNext);
            }
        }
        return;
    }
};
