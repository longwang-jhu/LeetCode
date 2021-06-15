// https://leetcode.com/problems/largest-rectangle-in-histogram/

// Given an array of integers heights representing the histogram's bar height where
// the width of each bar is 1, return the area of the largest rectangle in the
// histogram.

////////////////////////////////////////////////////////////////////////////////

// find largest rectangle at each index i
// need index of prev and next less num -> monostack
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> prevLessIdx(n, -1), nextLessIdx(n, n);
        stack<int> toRight, toLeft;
        for (int i = 0; i < n; ++i) {
            // pop if not less
            while (!toRight.empty() and heights[toRight.top()] >= heights[i]) {
                toRight.pop();
            }
            prevLessIdx[i] = toRight.empty() ? -1 : toRight.top();
            toRight.push(i);
        }
        for (int i = n - 1; i >= 0; --i) {
            // pop if not less
            while (!toLeft.empty() and heights[toLeft.top()] >= heights[i]) {
                toLeft.pop();
            }
            nextLessIdx[i] = toLeft.empty() ? n : toLeft.top();
            toLeft.push(i);
        }
        
        int maxArea = 0;
        for (int i = 0; i < n; ++i) {
            maxArea = max(maxArea, heights[i] * (nextLessIdx[i] - prevLessIdx[i] - 1));
        }
        return maxArea;
    }
};
