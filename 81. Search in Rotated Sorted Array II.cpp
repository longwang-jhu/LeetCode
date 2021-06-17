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

// binary search, [1st part | 2nd part]
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l + 1 < r) {
            int m = l + (r - l) / 2;
            if (nums[m] == target) return true;
            if (nums[m] > nums[r]) { // m in 1st part
                if (nums[l] <= target and target < nums[m]) r = m;
                else l = m;
            } else if (nums[m] < nums[r]) { // m in 2nd part
                if (nums[m] < target and target <= nums[r]) l = m;
                else r = m;
            } else --r; // undetermined
        }
        return nums[l] == target or nums[r] == target;
    }
};
