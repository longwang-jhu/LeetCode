// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

// Given an array of integers numbers that is already sorted in non-decreasing
// order, find two numbers such that they add up to a specific target number.

// Return the indices of the two numbers (1-indexed) as an integer array answer of
// size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

// The tests are generated such that there is exactly one solution. You may not use
// the same element twice.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;
        int total;
        while (l < r) {
            total = numbers[l] + numbers[r];
            if (total == target) return vector<int>{l+1, r+1};
            
            if (total < target) ++l;
            else --r;
        }
        return vector<int>{-1, -1};
    }
};
