// https://leetcode.com/problems/132-pattern/

// Given an array of n integers nums, a 132 pattern is a subsequence of three
// integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k]
// < nums[j].

// Return true if there is a 132 pattern in nums, otherwise, return false.

////////////////////////////////////////////////////////////////////////////////

// "1" is curr, "3" is next larger num, "2" is last popped num
// find next larger and compare with last popped -> monostack
// return true if curr < lastPopped
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        stack<int> toLeft; // ele = num of next larger
        int lastPopped = INT_MIN;
        for (int i = n - 1; i >= 0; --i) {
            if (nums[i] < lastPopped) return true;
            // pop is not larger and equal
            while (!toLeft.empty() and toLeft.top() < nums[i]) {
                lastPopped = toLeft.top();
                toLeft.pop();
            }
            toLeft.push(nums[i]);
        }
        return false;
    }
};
