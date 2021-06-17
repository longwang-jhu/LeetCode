// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

// Suppose an array of length n sorted in ascending order is rotated between 1 and
// n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
// the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

// Given the sorted rotated array nums that may contain duplicates, return the
// minimum element of this array.

// You must decrease the overall operation steps as much as possible.

////////////////////////////////////////////////////////////////////////////////

// binary search, [1st part | 2nd part]
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l + 1 < r) {
            int m = l + (r - l) / 2;
            if (nums[m] > nums[r]) l = m; // m in 1st part
            else if (nums[m] < nums[r]) r = m; // m in 2nd part
            else --r; // undetermined
        }
        return min(nums[l], nums[r]);
    }
};
