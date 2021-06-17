// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

// Given an array of integers nums sorted in ascending order, find the starting and
// ending position of a given target value.

// If target is not found in the array, return [-1, -1].

// You must write an algorithm with O(log n) runtime complexity.

////////////////////////////////////////////////////////////////////////////////

// binary search, find seperately
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.empty()) return {-1, -1};        
        // find firstP
        int l = 0, r = nums.size() - 1;
        while (l + 1 < r) {
            int m = l + (r - l) / 2;
            if (nums[m] < target) l = m;
            else r = m;
        }
        int firstP = (nums[l] == target) ? l : (nums[r] == target) ? r : -1;
        // find lastP
        l = 0, r = nums.size() - 1;
        while (l + 1 < r) {
            int m = l + (r - l) / 2;
            if (nums[m] > target) r = m;
            else l = m;
        }
        int lastP = (nums[r] == target) ? r : (nums[l] == target) ? l : -1;
        return {firstP, lastP};
    }
};
