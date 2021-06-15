// https://leetcode.com/problems/3sum/

// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
// such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

////////////////////////////////////////////////////////////////////////////////

// sort, use two left and right for 2sum
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if (nums.size() < 3) return {};
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for (int i = 0; i < nums.size() - 2; ++i) {
            if (i > 0 and nums[i] == nums[i-1]) continue; // skip identical
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                // skip identical
                if (left > i + 1 and nums[left] == nums[left - 1]) { ++left; continue; }
                if (right < nums.size() - 1 and nums[right] == nums[right + 1]) { --right; continue; }
                int total = nums[i] + nums[left] + nums[right];
                if (total == 0) {
                    ans.push_back({nums[i], nums[left], nums[right]});
                    ++left; --right;
                } else if (total < 0) ++left;
                else --right;
            }
        }
        return ans;
    }
};
