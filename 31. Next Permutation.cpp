// https://leetcode.com/problems/next-permutation/

// Implement next permutation, which rearranges numbers into the lexicographically
// next greater permutation of numbers.

// If such an arrangement is not possible, it must rearrange it as the lowest
// possible order (i.e., sorted in ascending order).

// The replacement must be in place and use only constant extra memory.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if (nums.size() == 1) return;
        
        // find first nums[i] < nums[i+1] from right: 1, *2, [4, 3, 3, 2]
        int i;
        for (i = nums.size() - 2; i >= 0; --i) {
            if (nums[i] < nums[i+1]) break;
        }
        if (i == -1) { reverse(nums.begin(), nums.end()); return; }
        // swap nums[i] with its next number from right: 1, *2, [4, 3, *3, 2] -> 1, *3, [4, 3, *2, 2]
        int j;
        for (j = nums.size() - 1; j > i; --j) {
            if (nums[j] > nums[i]) { swap(nums[i], nums[j]); break; }
        }
        // reverse nums in [...]: 1, 3, [2, 2, 3, 4]
        reverse(nums.begin() + i + 1, nums.end());
        return;
    }
};
