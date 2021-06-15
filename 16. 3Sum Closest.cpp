// https://leetcode.com/problems/3sum-closest/

// Given an array nums of n integers and an integer target, find three integers in
// nums such that the sum is closest to target. Return the sum of the three
// integers. You may assume that each input would have exactly one solution.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        if (nums.size() < 3) return -1;
        sort(nums.begin(), nums.end());
        int minDiff = INT_MAX, ans;
        for (int i = 0, n = nums.size(); i < n - 2; ++i) {
            int left = i + 1, right = n - 1;
            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];
                if (abs(total - target) < minDiff) {
                    minDiff = abs(total - target);
                    ans = total;
                }
                if (total == target) return target;
                if (total < target) ++left;
                else --right;
            }
        }
        return ans;
    }
};
