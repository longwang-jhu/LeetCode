// https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

// You are given an integer array arr.

// We split arr into some number of chunks (i.e., partitions), and individually
// sort each chunk. After concatenating them, the result should equal the sorted
// array.

// Return the largest number of chunks we can make to sort the array.

////////////////////////////////////////////////////////////////////////////////

// count how many breaks you can put in
// insert a break after i when max(nums[0...i]) <= min(nums[i+1...n-1])
// use leftMax and rightMin to record
// example: [2, 1, 3, 4, 4]
// chunks:  2, 1 | 3 | 4 | 4
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n = arr.size();
        vector<int> leftMax(n), rightMin(n);
        leftMax[0] = arr[0];
        for (int i = 1; i < n; ++i) {
            leftMax[i] = max(leftMax[i-1], arr[i]);
        }
        rightMin[n-1] = arr[n-1];
        for (int i = n - 2; i >= 0; --i) {
            rightMin[i] = min(rightMin[i+1], arr[i]);
        }
        
        int breaks = 0;
        for (int i = 0; i < n - 1; ++i) {
            if (leftMax[i] <= rightMin[i + 1]) breaks++;
        }
        return breaks + 1;
    }
};
