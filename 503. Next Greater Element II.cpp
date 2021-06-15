// https://leetcode.com/problems/next-greater-element-ii/

// Given a circular integer array nums (i.e., the next element of nums[nums.length
// - 1] is nums[0]), return the next greater number for every element in nums.

// The next greater number of a number x is the first greater number to its
// traversing-order next in the array, which means you could search circularly to
// find its next greater number. If it doesn't exist, return -1 for this number.

////////////////////////////////////////////////////////////////////////////////

// next greater num -> monoqueue
// go through twice to ensure cicular
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        stack<int> toLeft; // ele = num
        for (int j : {1, 2}) { // go through twice
            for (int i = n - 1; i >= 0; --i) {
                // pop if not greater
                while (!toLeft.empty() and toLeft.top() <= nums[i]) {
                    toLeft.pop();
                }
                ans[i] = toLeft.empty() ? -1 : toLeft.top();
                toLeft.push(nums[i]);
            }
        }
        return ans;
    }
};
