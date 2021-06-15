// https://leetcode.com/problems/max-chunks-to-make-sorted/

// You are given an integer array arr of length n that represents a permutation of
// the integers in the range [0, n - 1].

// We split arr into some number of chunks (i.e., partitions), and individually
// sort each chunk. After concatenating them, the result should equal the sorted
// array.

// Return the largest number of chunks we can make to sort the array.

////////////////////////////////////////////////////////////////////////////////

// find leftMax (including self)
// idx:     0, 1, 2, 3, 4, 5, 6, 7
// Example: 0, 2, 1, 4, 3, 5, 7, 6
// leftMax: 0, 2, 2, 4, 4, 5, 7, 7
// chunks:  [-----], [--], [],[--] (number of leftMax == idx)

class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n = arr.size(), ans = 0, leftMax = INT_MIN;
        for (int i = 0; i < n; ++i) {
            leftMax = max(leftMax, arr[i]);
            if (leftMax == i) ++ans;
        }
        return ans;
    }
};
