// https://leetcode.com/problems/maximal-rectangle/

// Given a rows x cols binary matrix filled with 0's and 1's, find the largest
// rectangle containing only 1's and return its area.

////////////////////////////////////////////////////////////////////////////////

// scan by row, convert 2D matrix to 1D heights
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int m = matrix.size(), n = matrix[0].size();
        vector<int> heights(n, 0);
        int maxArea = 0;
        // scan by row and update heights
        for (int row = 0; row < m; ++row) {
            for (int col = 0; col < n; ++col) {
                if (matrix[row][col] == '1') ++heights[col];
                else heights[col] = 0;
            }
            maxArea = max(maxArea, largestRectangleArea(heights));
        }
        return maxArea;
    }
    
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> prevSmaller(n, -1); // index of prev smaller num
        stack<int> toRight;
        for (int i = 0; i < n; ++i) {
            // pop when prev is not smaller
            while (!toRight.empty() and heights[toRight.top()] >= heights[i]) {
                toRight.pop();
            }
            prevSmaller[i] = toRight.empty() ? -1 : toRight.top();
            toRight.push(i);
        }
        vector<int> nextSmaller(n, n); // index of next smaller num
        stack<int> toLeft;
        for (int i = n - 1; i >= 0; --i) {
            // pop when next is not smaller
            while (!toLeft.empty() and heights[toLeft.top()] >= heights[i]) {
                toLeft.pop();
            }
            nextSmaller[i] = toLeft.empty() ? n : toLeft.top();
            toLeft.push(i);
        }
        
        int maxArea = 0;
        for (int i = 0; i < n; ++i) {
            maxArea = max(maxArea, heights[i] * (nextSmaller[i] - prevSmaller[i] - 1));
        }
        return maxArea;
    }
};
