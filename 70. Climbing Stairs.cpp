// https://leetcode.com/problems/climbing-stairs/

// You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you
// climb to the top?

////////////////////////////////////////////////////////////////////////////////

// dp[i] = ways to reach level i
// dp[i] = dp[i-1] + dp[i-2]
class Solution {
public:
    int climbStairs(int n) {
        // return climbStairsDp1(n);
        if (n < 2) return n;
        vector<int> dp(n + 1, 1);
        for (int i = 2; i <= n; ++i) {
            dp[i] = dp[i-2] + dp[i-1];
        }
        return dp.back();
    }
    int climbStairsDp1(int n) {
        if (n < 2) return n;
        int prev2 = 1, prev1 = 1, curr;
        for (int i = 2; i <= n; ++i) {
            curr = prev2 + prev1;
            prev2 = prev1;
            prev1 = curr;
        }
        return curr;
    }
};
