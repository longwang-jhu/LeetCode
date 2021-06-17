// https://leetcode.com/problems/longest-common-subsequence/

// Given two strings text1 and text2, return the length of their longest common
// subsequence. If there is no common subsequence, return 0.

// A subsequence of a string is a new string generated from the original string
// with some characters (can be none) deleted without changing the relative order
// of the remaining characters.

// A common subsequence of two strings is a subsequence that is common to both
// strings.

////////////////////////////////////////////////////////////////////////////////

// dp[i][j] = LCS from text1[0...i-1] and text2[0...j-1]
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size(), n = text2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (text1[i-1] == text2[j-1]) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j]);
                }
            }
        }
        return dp.back().back();
    }
};
