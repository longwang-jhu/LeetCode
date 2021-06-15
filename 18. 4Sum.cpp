// https://leetcode.com/problems/4sum/

// Given an array nums of n integers, return an array of all the unique quadruplets
// [nums[a], nums[b], nums[c], nums[d]] such that:

// You may return the answer in any order.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        if (nums.size() < 4) return {};
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for (int i = 0, n = nums.size(); i < n - 3; ++i) {
            if (i > 0 and nums[i] == nums[i-1]) continue; // skip identical
            for (int j = i + 1; j < n - 2 ; ++j) {
                if (j > i + 1 and nums[j] == nums[j-1]) continue;
                int left = j + 1, right = n - 1;
                while (left < right) {
                    if (left > j + 1 and nums[left] == nums[left - 1]) { ++left; continue; }
                    if (right < n - 1 and nums[right] == nums[right + 1]) { --right; continue; }
                    int total = nums[i] + nums[j] + nums[left] + nums[right];
                    if (total == target) {
                        ans.push_back({nums[i], nums[j], nums[left], nums[right]});
                        ++left; --right;
                    } else if (total < target) ++left;
                    else --right;
                }
            }
        }
        return ans;
    }
};
