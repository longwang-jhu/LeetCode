// https://leetcode.com/problems/01-matrix/

// Given an m x n binary matrix mat, return the distance of the nearest 0 for each
// cell.

// The distance between two adjacent cells is 1.

////////////////////////////////////////////////////////////////////////////////

// dp, scan from top-left and bottom-right
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> dp(m, vector<int>(n, m * n));
        // from top-left
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 0) dp[i][j] = 0;
                else if (i == 0 and j > 0) {
                    dp[i][j] = dp[i][j-1] + 1;
                } else if (i > 0 and j == 0) {
                    dp[i][j] = dp[i-1][j] + 1;
                } else if (i > 0 and j > 0) {
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1;
                }
            }
        }        
        // from bottom-right
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (mat[i][j] == 0) continue;
                if (i == m - 1 and j < n - 1) {
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1);
                } else if (i < m - 1 and j == n - 1) {
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1);
                } else if (i < m - 1 and j < n - 1) {
                    dp[i][j] = min(dp[i][j], min(dp[i][j+1], dp[i+1][j]) + 1);
                }
            }
        }
        return dp;
    }
};
