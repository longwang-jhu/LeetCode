// https://leetcode.com/problems/non-decreasing-array/

// Given an array nums with n integers, your task is to check if it could become
// non-decreasing by modifying at most one element.

// We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i
// (0-based) such that (0 <= i <= n - 2).

////////////////////////////////////////////////////////////////////////////////

// greedy
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        if (nums.empty() or nums.size() <= 2) return true;
        
        bool modified = false;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i-1] > nums[i]) { // found a violation
                if (modified) return false;
                modified = true;
                
                if (i == 1 or nums[i-2] <= nums[i]) { // change nums[i-1]
                    nums[i-1] = nums[i];
                } else { // change nums[i]
                    nums[i] = nums[i-1];
                }
            }
        }
        return true;
    }
};
