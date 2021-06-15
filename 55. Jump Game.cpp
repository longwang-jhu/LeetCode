// https://leetcode.com/problems/jump-game/

// Given an array of non-negative integers nums, you are initially positioned at
// the first index of the array.

// Each element in the array represents your maximum jump length at that position.

// Determine if you are able to reach the last index.

////////////////////////////////////////////////////////////////////////////////

// dp[i] = if can reach index i
// greedy: update frontier from end, return frontier == 0
class Solution {
public:
    bool canJump(vector<int>& nums) {
        return canJumpGreedy(nums);
        if (nums.size() == 1) return true;
        int n = nums.size();
        // dp[i] = if can reach index i
        vector<bool> dp(n, false); dp[0] = true;
        for (int i = 0; i < n - 1; ++i) {
            int jump = nums[i];
            if (dp[i]) { // can jump forward
                if (i + jump >= n - 1) return true; // reach end
                for (int j = i + 1; j <= i + jump; ++j) dp[j] = true;
            } else return false;
        }
        return false;
    }
    
    bool canJumpGreedy(vector<int>& nums) {
        if (nums.size() == 1) return true;
        int n = nums.size();
        // start from back
        int frontier = n - 1;
        for (int i = n - 2; i >= 0; --i) {
            if (i + nums[i] >= frontier) frontier = i;
        }
        return frontier == 0;
    }
};
