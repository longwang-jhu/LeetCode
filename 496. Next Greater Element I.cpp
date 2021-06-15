// https://leetcode.com/problems/next-greater-element-i/

// You are given two integer arrays nums1 and nums2 both of unique elements, where
// nums1 is a subset of nums2.

// Find all the next greater numbers for nums1's elements in the corresponding
// places of nums2.

// The Next Greater Number of a number x in nums1 is the first greater number to
// its right in nums2. If it does not exist, return -1 for this number.

////////////////////////////////////////////////////////////////////////////////

// find next greater num -> monostack
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size();
        unordered_map<int, int> hashMap; // hashMap[num] = next greater num
        stack<int> toLeft;
        for (int i = n2 - 1; i >= 0; --i) {
            // pop is not greater
            while (!toLeft.empty() and toLeft.top() <= nums2[i]) {
                toLeft.pop();
            }
            hashMap[nums2[i]] = toLeft.empty() ? -1 : toLeft.top();
            toLeft.push(nums2[i]);
        }
        vector<int> ans(n1);
        for (int i = 0; i < n1; ++i) ans[i] = hashMap[nums1[i]];
        return ans;
    }
};
