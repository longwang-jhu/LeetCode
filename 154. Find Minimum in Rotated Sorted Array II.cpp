// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

// Suppose an array of length n sorted in ascending order is rotated between 1 and
// n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
// the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

// Given the sorted rotated array nums that may contain duplicates, return the
// minimum element of this array.

// You must decrease the overall operation steps as much as possible.

////////////////////////////////////////////////////////////////////////////////

// binary search
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            // mid is in 1st part
            if (nums[mid] > nums[right]) left = mid;
            // mid is in 2nd part
            else if (nums[mid] < nums[right]) right = mid;
            // cannot decide
            else --right;
        }
        
        return min(nums[left], nums[right]);
    }
};
