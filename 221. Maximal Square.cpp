// https://leetcode.com/problems/maximal-square/

// Given an m x n binary matrix filled with 0's and 1's, find the largest square
// containing only 1's and return its area.

////////////////////////////////////////////////////////////////////////////////

// dp[i][j] = size with bottom-right at (i,j)
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; ++i) {
            dp[i][0] = matrix[i][0] - '0';
        }
        for (int j = 1; j < n; ++j) {
            dp[0][j] = matrix[0][j] - '0';
        }
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][j] == '0') continue;
                dp[i][j] = 1;
                if (matrix[i-1][j-1] == '1') { // check for expansion
                    dp[i][j] = min({dp[i][j-1], dp[i-1][j], dp[i-1][j-1]}) + 1;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            ans = max(ans, *max_element(dp[i].begin(), dp[i].end()));
        }
        return ans * ans;
    }
};
