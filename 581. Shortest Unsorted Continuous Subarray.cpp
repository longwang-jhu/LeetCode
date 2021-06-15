// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

// Given an integer array nums, you need to find one continuous subarray that if
// you only sort this subarray in ascending order, then the whole array will be
// sorted in ascending order.

// Return the shortest such subarray and output its length.

////////////////////////////////////////////////////////////////////////////////

// start = min idx of which exists next less num
// end = max idx of which exists prev larger num
// monoqueue
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size(), start = n, end = -1;
        stack<int> toLeft;
        for (int i = n - 1; i >= 0; --i) {
            // pop if not less
            while (!toLeft.empty() and nums[toLeft.top()] >= nums[i]) {
                toLeft.pop();
            }
            if (!toLeft.empty()) start = min(start, i);
            toLeft.push(i);
        }
        stack<int> toRight;
        for (int i = 0; i < n; ++i) {
            // pop if not larger
            while (!toRight.empty() and nums[toRight.top()] <= nums[i]) {
                toRight.pop();
            }
            if (!toRight.empty()) end = max(end, i);
            toRight.push(i);
        }
        return (start > end) ? 0 : end - start + 1;
    }
};
