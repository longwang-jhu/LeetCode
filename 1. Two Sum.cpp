// https://leetcode.com/problems/two-sum/

// Given an array of integers nums and an integer target, return indices of the two
// numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not
// use the same element twice.

// You can return the answer in any order.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // hashMap[num] = idx
        unordered_map<int, int> hashMap;
        for (int i = 0; i < nums.size(); ++i) {
            int comp = target - nums[i];
            // check if comp is in hashMap
            if (hashMap.find(comp) != hashMap.end()) return {hashMap[comp], i};
            else hashMap[nums[i]] = i;
        }
        return {-1, -1};
    }
};
