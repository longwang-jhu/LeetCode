// https://leetcode.com/problems/ones-and-zeroes/

// You are given an array of binary strings strs and two integers m and n.

// Return the size of the largest subset of strs such that there are at most m 0's
// and n 1's in the subset.

// A set x is a subset of a set y if all elements of x are also elements of y.

////////////////////////////////////////////////////////////////////////////////

// backpack: dp[k][i][j] = no of substrs from strs[0...k-1] with 0's < i and 1's < j
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        return findMaxFormDp2(strs, m, n);
        int l = strs.size();
        vector<vector<vector<int>>> dp(l+1, vector<vector<int>>(m+1, vector<int>(n+1, 0)));
        for (int k = 1; k <= l; ++k) {
            auto [ct0, ct1] = getCount(strs[k-1]);
            for (int i = 0; i <= m; ++i) {
                for (int j = 0; j <= n; ++j) {
                    dp[k][i][j] = dp[k-1][i][j]; // not use strs[k-1]
                    if (i >= ct0 && j >= ct1) { // use strs[k-1]
                        dp[k][i][j] = max(dp[k][i][j], dp[k-1][i-ct0][j-ct1] + 1);
                    }
                }
            }
        }
        return dp[l][m][n];
    }
    int findMaxFormDp2(vector<string>& strs, int m, int n) {
        int l = strs.size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        for (int k = 1; k <= l; ++k) {
            auto [ct0, ct1] = getCount(strs[k-1]);
            for (int i = m; i >= 0; --i) { // must go backwards
                for (int j = n; j >= 0; --j) {
                    if (i >= ct0 && j >= ct1) { // use strs[k-1]
                        dp[i][j] = max(dp[i][j], dp[i-ct0][j-ct1] + 1);
                    }
                }
            }
        }
        return dp[m][n];
    }
    
    
private:
    pair<int, int> getCount(const string& s) {
        int ct0 = 0, ct1 = 0;
        for (const char& c : s) {
            if (c == '0') ++ct0;
            else ++ct1;
        }
        return {ct0, ct1};
    }
};
