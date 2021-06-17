// https://leetcode.com/problems/partition-equal-subset-sum/

// Given a non-empty array nums containing only positive integers, find if the
// array can be partitioned into two subsets such that the sum of elements in both
// subsets is equal.

////////////////////////////////////////////////////////////////////////////////

// backpack with cap = total / 2
// dp[i][j] = if nums[0...i-1] can reach j
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total = accumulate(nums.begin(), nums.end(), 0);
        if (total % 2 != 0) return false;
        int n = nums.size(), cap = total / 2;
        vector<vector<bool>> dp(n + 1, vector<bool>(cap + 1, false));
        // base: use nothing to reach 0
        for (int i = 0; i < n + 1; ++i) dp[i][0] = true;
        for (int i = 1; i < n + 1; ++i) {
            int num = nums[i-1];
            for (int j = 1; j < cap + 1; ++j) {
                dp[i][j] = dp[i-1][j]; // not use nums[i-1]
                if (j >= num) { // use nums[i-1]
                    dp[i][j] = dp[i][j] || dp[i-1][j-num];
                }
            }
        }
        return dp.back().back();
    }
};
