// https://leetcode.com/problems/house-robber/

// You are a professional robber planning to rob houses along a street. Each house
// has a certain amount of money stashed, the only constraint stopping you from
// robbing each of them is that adjacent houses have security systems connected and
// it will automatically contact the police if two adjacent houses were broken into
// on the same night.

// Given an integer array nums representing the amount of money of each house,
// return the maximum amount of money you can rob tonight without alerting the
// police.

////////////////////////////////////////////////////////////////////////////////

// dp[i] = max_money from nums[0...i-1]
// dp[i] = max(not rob nums[i-1], rob nums[i-1])
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        
        vector<int> dp(nums.size() + 1);
        dp[1] = nums[0];
        for (int i = 2; i <= nums.size(); ++i) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]);
        }
        return dp.back();
    }
};
