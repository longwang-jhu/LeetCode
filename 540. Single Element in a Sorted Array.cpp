// https://leetcode.com/problems/single-element-in-a-sorted-array/

// You are given a sorted array consisting of only integers where every element
// appears exactly twice, except for one element which appears exactly once. Find
// this single element that appears only once.

// Follow up: Your solution should run in O(log n) time and O(1) space.

////////////////////////////////////////////////////////////////////////////////

// binary search
// if m is even check nums[m] == nums[m+1]
// if m is odd check nums[m] == nums[m-1]
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];        
        int l = 0, r = nums.size() - 1;
        while (l + 1 < r) {
            int m = l + (r - l) / 2;
            if (m % 2 == 0) { // m is even
                if (nums[m] == nums[m + 1]) l = m + 2;
                else r = m;
            } else { // m is odd
                if (nums[m] == nums[m - 1]) l = m + 1;
                else r = m;
            }
        }
        if (r == nums.size() - 1) {
            return (nums[l] == nums[l - 1]) ? nums[r] : nums[l];
        }
        return (nums[r] == nums[r + 1]) ? nums[l] : nums[r];
    }
};
