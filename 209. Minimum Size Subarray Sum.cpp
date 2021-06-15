// https://leetcode.com/problems/minimum-size-subarray-sum/

// Given an array of positive integers nums and a positive integer target, return
// the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1,
// numsr] of which the sum is greater than or equal to target. If there is no such
// subarray, return 0 instead.

////////////////////////////////////////////////////////////////////////////////

// contiguous array -> sliding window
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int minLen = INT_MAX, n = nums.size();
        int left = 0, right = 0, window = 0;
        while (right < n) {
            window += nums[right]; // update window
            while (window >= target) {
                minLen = min(minLen, right - left + 1);
                window -= nums[left];
                ++left;
            }
            ++right;
        }
        return minLen == INT_MAX ? 0 : minLen;
    }
};
