// https://leetcode.com/problems/coin-change/

// You are given an integer array coins representing coins of different
// denominations and an integer amount representing a total amount of money.

// Return the fewest number of coins that you need to make up that amount. If that
// amount of money cannot be made up by any combination of the coins, return -1.

// You may assume that you have an infinite number of each kind of coin.

////////////////////////////////////////////////////////////////////////////////

// backpack: dp[i][j] = fewest coin from coins[0...i-1] to get amount j
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        return coinChangeDp1(coins, amount);
        int m = coins.size(), n = amount;
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, n + 1));
        // base: 0 ways to get amount 0
        for (int i = 0; i <= m; ++i) dp[i][0] = 0;
        for (int i = 1; i <= m; ++i) {
            int coin = coins[i-1];
            for (int j = 1; j <= n; ++j) {
                dp[i][j] = dp[i-1][j]; // not use coins[i-1]
                if (j >= coin) { // use coins[i-1]
                    dp[i][j] = min(dp[i][j], dp[i][j-coin] + 1);
                }
            }
        }
        if (dp[m][n] == n + 1) return -1;
        return dp[m][n];
    }
    
    int coinChangeDp1(vector<int>& coins, int amount) {
        int m = coins.size(), n = amount;
        vector<int> dp(n + 1, n + 1);
        // base: 0 ways to get amount 0
        dp[0] = 0;
        for (int i = 1; i <= m; ++i) {
            int coin = coins[i-1];
            for (int j = 1; j <= n; ++j) {
                if (j >= coin) { // use coins[i-1]
                    dp[j] = min(dp[j], dp[j-coin] + 1);
                }
            }
        }
        if (dp[n] == n + 1) return -1;
        return dp[n];
    }
};
