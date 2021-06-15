// https://leetcode.com/problems/sliding-window-maximum/

// You are given an array of integers nums, there is a sliding window of size k
// which is moving from the very left of the array to the very right. You can only
// see the k numbers in the window. Each time the sliding window moves right by one
// position.

// Return the max sliding window.

////////////////////////////////////////////////////////////////////////////////

// monoqueue toRight, only keep prev greater num
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans;
        deque<int> toRight; // ele = idx, only keep larger num
        for (int i = 0; i < n; ++i) {
            // remove out of range num
            while (!toRight.empty() and toRight.front() < i - k + 1) {
                toRight.pop_front();
            }
            // pop if not greater
            while (!toRight.empty() and nums[toRight.back()] <= nums[i]) {
                toRight.pop_back();
            }
            toRight.push_back(i);
            // update ans starting from k - 1
            if (i >= k - 1) ans.push_back(nums[toRight.front()]);
        }
        return ans;
    }
};
