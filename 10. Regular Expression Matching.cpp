// https://leetcode.com/problems/regular-expression-matching/

// Given an input string (s) and a pattern (p), implement regular expression
// matching with support for '.' and '*' where:

// The matching should cover the entire input string (not partial).

////////////////////////////////////////////////////////////////////////////////

// dp[i][j] = isMatch(s[0...i-1], p[0...j-1])
class Solution {
public:
    bool isMatch(string s, string p) {
        int ns = s.size(), np = p.size();
        vector<vector<bool>> dp(ns + 1, vector<bool>(np + 1));
        // base
        dp[0][0] = true;
        dp[0][1] = false;
        for (int j = 2; j < np + 1; ++j) {
            if (p[j-1] == '*') dp[0][j] = dp[0][j-2]; // not use '*'
        }
        for (int i = 1; i < ns + 1; ++i) {
            for (int j = 1; j < np + 1; ++j) {
                // compare s[i-1] and p[j-1]
                if (p[j-1] == '.') {
                    dp[i][j] = dp[i-1][j-1]; // match any
                } else if (p[j-1] == '*') {
                    bool case0 = dp[i][j-2]; // not use '*'
                    bool case1 = dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.'); // use '*'
                    dp[i][j] = case0 or case1;
                } else if (p[j-1] == s[i-1]) { 
                    dp[i][j] = dp[i-1][j-1];
                } else dp[i][j] = false;
            }
        }
        return dp[ns][np];
    }
};
