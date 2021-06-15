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
        if (nums.empty()) return vector<int>{-1, -1};
        
        // find first pos
        int left = 0, right = nums.size() - 1, mid;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            if (nums[mid] >= target) right = mid;
            else left = mid;
        }
        int firstPos = (nums[left] == target) ? left : (nums[right] == target) ? right : -1;
        
        // find last pos
        left = 0, right = nums.size() - 1;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            if (nums[mid] <= target) left = mid;
            else right = mid;
        }
        int secondPos = (nums[right] == target) ? right : (nums[left] == target) ? left : -1;
        
        return vector<int>{firstPos, secondPos};
    }
};
