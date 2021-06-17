// https://leetcode.com/problems/longest-increasing-subsequence/

// Given an integer array nums, return the length of the longest strictly
// increasing subsequence.

// A subsequence is a sequence that can be derived from an array by deleting some
// or no elements without changing the order of the remaining elements. For
// example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

////////////////////////////////////////////////////////////////////////////////

// dp[i] = longest increasing subseq from nums[0...i], must use nums[i]
// dp[i] = max(dp[j] + 1) over all j = 0...i-1 that nums[j] < nums[i]
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        for (int i = 1; i < nums.size(); ++i) {
            for (int j = 0; j <= i - 1; ++j) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};
