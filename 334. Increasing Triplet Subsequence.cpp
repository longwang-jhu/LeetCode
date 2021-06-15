// https://leetcode.com/problems/increasing-triplet-subsequence/

// Given an integer array nums, return true if there exists a triple of indices (i,
// j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices
// exists, return false.

////////////////////////////////////////////////////////////////////////////////

// track smallest and secondSmallest
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int smallest = INT_MAX, secondSmallest = INT_MAX;
        for (int& num : nums) {
            if (num <= smallest) smallest = num;
            else if (num <= secondSmallest) secondSmallest = num;
            else return true;
        }
        return false;
    }
};
