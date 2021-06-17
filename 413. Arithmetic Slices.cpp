// https://leetcode.com/problems/arithmetic-slices/

// An integer array is called arithmetic if it consists of at least three elements
// and if the difference between any two consecutive elements is the same.

// Given an integer array nums, return the number of arithmetic subarrays of nums.

// A subarray is a contiguous subsequence of the array.

////////////////////////////////////////////////////////////////////////////////

// dp[i] = no of subarrays in nums[0...i], must use nums[i]
// if can add nums[i], dp[i] = dp[i-1] + 1 (shift + append)
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        if (nums.size() < 3) return 0;
        vector<int> dp(nums.size(), 0);
        for (int i = 2; i < nums.size(); ++i) {
            if (nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) {
                dp[i] = dp[i-1] + 1;
            }
        }
        return accumulate(dp.begin(), dp.end(), 0);
    }
};
