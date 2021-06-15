// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

// Return the length of the shortest, non-empty, contiguous subarray of nums with
// sum at least k.

// If there is no non-empty subarray with sum at least k, return -1.

////////////////////////////////////////////////////////////////////////////////

// cannot use sliding window due to possible negative num
// use prefixSum pre[i] = sum(nums[0...i-1]) and push_back i to deque
// for each i, find prev less num
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> pre(n + 1, 0); // pre[i] = sum(nums[0...i-1])
        for (int i = 1; i < n + 1; ++i) {
            pre[i] = pre[i-1] + nums[i-1];
        }
        deque<int> toRight; // ele = idx
        int minLen = INT_MAX;
        for (int i = 0; i < n + 1; ++i) {
            // check if nums[todo.front()...i] is a good subarray
            while (!toRight.empty() and pre[i] - pre[toRight.front()] >= k) {
                minLen = min(minLen, i - toRight.front());
                toRight.pop_front(); // toRight.front() is done, remove it
            }
            // pop if not less
            while (!toRight.empty() and pre[toRight.back()] >= pre[i]) {
                toRight.pop_back();
            }
            toRight.push_back(i);
        }
        return minLen == INT_MAX ? -1 : minLen;
    }
};
