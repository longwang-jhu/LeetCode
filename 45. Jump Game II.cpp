// https://leetcode.com/problems/jump-game-ii/

// Given an array of non-negative integers nums, you are initially positioned at
// the first index of the array.

// Each element in the array represents your maximum jump length at that position.

// Your goal is to reach the last index in the minimum number of jumps.

// You can assume that you can always reach the last index.

////////////////////////////////////////////////////////////////////////////////

// dp[i] = min jumps to reach index i
class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1) return 0;
        int n = nums.size();
        // dp[i] = min jumps to reach index i
        vector<int> dp(n, n); dp[0] = 0;
        int frontier = 0;
        for (int i = 0; i < n - 1; ++i) {
            int jump = nums[i];
            if (i + jump >= n - 1) return dp[i] + 1; // reach end
            if (i + jump > frontier) { // can go further
                for (int j = frontier + 1; j <= i + jump; ++j) {
                    dp[j] = dp[i] + 1;
                }
                frontier = i + jump;
            }
        }
        return dp[n-1];
    }
};
