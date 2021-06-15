// https://leetcode.com/problems/single-element-in-a-sorted-array/

// You are given a sorted array consisting of only integers where every element
// appears exactly twice, except for one element which appears exactly once. Find
// this single element that appears only once.

// Follow up: Your solution should run in O(log n) time and O(1) space.

////////////////////////////////////////////////////////////////////////////////

// binary search
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        
        int left = 0, right = nums.size() - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            
            if (mid % 2 == 0) { // mid is even
                if (nums[mid] == nums[mid + 1]) left = mid + 2;
                else right = mid;
            } else { // mid is odd
                if (nums[mid] == nums[mid - 1]) left = mid + 1;
                else right = mid;
            }
        }
        
        if (right == nums.size() - 1) {
            return (nums[left] == nums[left - 1]) ? nums[right] : nums[left];
        } else {
            return (nums[right] == nums[right + 1]) ? nums[left] : nums[right];
        }
    }
};
