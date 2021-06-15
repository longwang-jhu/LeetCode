// https://leetcode.com/problems/sort-colors/

// Given an array nums with n objects colored red, white, or blue, sort them in-
// place so that objects of the same color are adjacent, with the colors in the
// order red, white, and blue.

// We will use the integers 0, 1, and 2 to represent the color red, white, and
// blue, respectively.

// You must solve this problem without using the library's sort function.

////////////////////////////////////////////////////////////////////////////////

// nums[...left | mid | right...]
// note: must ++mid if swap with left
class Solution {
public:
    void sortColors(vector<int>& nums) {
        if (nums.size() == 1) return;
        
        int left = 0, mid = 0, right = nums.size() - 1;
        while (mid <= right) {
            if (nums[mid] == 0) swap(nums[left++], nums[mid++]);
            else if (nums[mid] == 2) swap(nums[mid], nums[right--]);
            else ++mid;
        }
        return;
    }
};
