// https://leetcode.com/problems/trapping-rain-water/

// Given n non-negative integers representing an elevation map where the width of
// each bar is 1, compute how much water it can trap after raining.

////////////////////////////////////////////////////////////////////////////////

// for each i, find its leftMax and rightMax
class Solution {
public:
    int trap(vector<int>& height) {
        return trapStack(height);
        int n = height.size();
        vector<int> leftMax(n, 0);
        for (int i = 1; i < n; ++i) {
            leftMax[i] = max(leftMax[i-1], height[i-1]);
        }
        vector<int> rightMax(n, 0);
        for (int i = n - 2; i >= 0; --i) {
            rightMax[i] = max(rightMax[i+1], height[i+1]);
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += max(min(leftMax[i], rightMax[i]) - height[i], 0);
        }
        return ans;
    }
    
    int trapStack(vector<int>& height) {
        int n = height.size();
        int ans = 0;
        stack<int> toRight;
        for (int i = 0; i < n; ++i) {
            while (!toRight.empty() and height[toRight.top()] < height[i]) {
                // compute water hold at prevLess
                int prevLess = toRight.top();
                toRight.pop();
                if (toRight.empty()) break; // cannot hold water
                int width = i - toRight.top() - 1;
                int water = min(height[toRight.top()], height[i]) - height[prevLess];
                ans += width * water;
            }
            toRight.push(i);
        }
        return ans;
    }
};
