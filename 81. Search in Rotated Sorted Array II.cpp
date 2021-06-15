// https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

// There is an integer array nums sorted in non-decreasing order (not necessarily
// with distinct values).

// Before being passed to your function, nums is rotated at an unknown pivot index
// k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1],
// ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example,
// [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
// [4,5,6,6,7,0,1,2,4,4].

// Given the array nums after the rotation and an integer target, return true if
// target is in nums, or false if it is not in nums.

// You must decrease the overall operation steps as much as possible.

////////////////////////////////////////////////////////////////////////////////

// binary search
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1, mid;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            
            if (nums[mid] == target) return true;
            if (nums[mid] > nums[right]) { // mid is in 1st part
                if (nums[left] <= target and target < nums[mid]) right = mid;
                else left = mid;
            } else if (nums[mid] < nums[right]) { // mid is in 2nd part
                if (nums[mid] < target and target <= nums[right]) left = mid;
                else right = mid;
            } else --right;
        }
        
        return nums[left] == target or nums[right] == target;
    }
};
