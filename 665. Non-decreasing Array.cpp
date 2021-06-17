// https://leetcode.com/problems/non-decreasing-array/

// Given an array nums with n integers, your task is to check if it could become
// non-decreasing by modifying at most one element.

// We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i
// (0-based) such that (0 <= i <= n - 2).

////////////////////////////////////////////////////////////////////////////////

// greedy, check to modify nums[i-1] or nums[i]
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        if (nums.empty() || nums.size() <= 2) return true;
        bool hasModified = false;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < nums[i-1]) { // found a violation
                if (hasModified) return false;
                // modify nums[i-1] or nums[i]
                if (i == 1 || nums[i-2] <= nums[i]) {
                    nums[i-1] = nums[i];
                } else nums[i] = nums[i-1];
                hasModified = true;
            }
        }
        return true;
    }
};
