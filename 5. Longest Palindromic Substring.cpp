// https://leetcode.com/problems/longest-palindromic-substring/

// Given a string s, return the longest palindromic substring in s.

////////////////////////////////////////////////////////////////////////////////

// palindromic -> dp[i][j] = if s[i...j] is pali
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        int maxLen = 1, start = 0;
        // len = 1
        for (int i = 0; i < n; ++i) dp[i][i] = true;
        // len = 2
        for (int i = 0; i + 1 < n; ++i) {
            if (s[i] == s[i+1]) {
                dp[i][i+1] = true;
                maxLen = 2; start = i;
            }
        }
        // len = 3...n
        for (int len = 3; len <= n; ++len){
            // check s[i...i+len-1]
            for (int i = 0, j = i + len - 1; j < n; ++i, ++j) {
                if (s[i] == s[j] and dp[i+1][j-1]) {
                    dp[i][j] = true;
                    maxLen = len; start = i;
                }
            }
        }
        return s.substr(start, maxLen);
    }
};
