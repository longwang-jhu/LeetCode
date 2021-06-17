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

// two dfs fir Pacific and Altantic
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = heights.size(); n = heights[0].size();
        vector<vector<bool>> visitedP(m, vector(n, false));
        vector<vector<bool>> visitedA(m, vector(n, false));
        for (int i = 0; i < m; ++i) {
            if (!visitedP[i][0]) dfs(i, 0, heights, visitedP);
            if (!visitedA[i][n-1]) dfs(i, n - 1, heights, visitedA);
        }
        for (int j = 0; j < n; ++j) {
            if (!visitedP[0][j]) dfs(0, j, heights, visitedP);
            if (!visitedA[m-1][j]) dfs(m - 1, j, heights, visitedA);
        }
        vector<vector<int>> ans;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (visitedP[i][j] && visitedA[i][j]) ans.push_back({i,j});
            }
        }
        return ans;
    }
private:
    int m, n;
    vector<pair<int, int>> dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    void dfs(int i, int j, const vector<vector<int>>& heights,
            vector<vector<bool>>& visited) {
        visited[i][j] = true;
        for (const auto& [iIncr, jIncr] : dirs) {
            int iNext = i + iIncr, jNext = j + jIncr;
            if (iNext >= 0 && iNext < m && jNext >= 0 and jNext < n
                && !visited[iNext][jNext]
                && heights[iNext][jNext] >= heights[i][j]) {
                dfs(iNext, jNext, heights, visited);
            }
        }
        return;
    }
};
