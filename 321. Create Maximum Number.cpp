// https://leetcode.com/problems/create-maximum-number/

// You are given two integer arrays nums1 and nums2 of lengths m and n
// respectively. nums1 and nums2 represent the digits of two numbers. You are also
// given an integer k.

// Create the maximum number of length k <= m + n from digits of the two numbers.
// The relative order of the digits from the same array must be preserved.

// Return an array of the k digits representing the answer.

////////////////////////////////////////////////////////////////////////////////

// step 1: get maxNumber from one array with length k
// step 2: get maxNumber of length n1 + n2 by merging two maxNumbers
// step 3: get max1 of length i from nums1, get max2 of length k - i from nums2
//         merge max1 and max2

// Note: when merging two maxNumbers, pick the greater digit (if same, pick the one has greater following digits -> get a greater function)
class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        int n1 = nums1.size(), n2 = nums2.size();
        vector<int> ans(k, 0);
        // merge max numbers from nums1 with length i and from nums2 with length k - i
        for (int i = 0; i <= k and i <= n1; ++i) {
            if (k - i > n2) continue;
            vector<int> max1 = maxNumberOne(nums1, i);
            vector<int> max2 = maxNumberOne(nums2, k - i);
            vector<int> cand = maxNumberMerge(max1, max2, k);
            if (greater(cand, 0, ans, 0)) ans = cand;
        }
        return ans;
    }
    
    // create maximum number by combining nums1 and nums2
    vector<int> maxNumberMerge(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<int> ans(k);
        for (int i1 = 0, i2 = 0, j = 0; j < k; ++j) {
            ans[j] = greater(nums1, i1, nums2, i2) ? nums1[i1++] : nums2[i2++];
        }
        return ans;
    }
    
    bool greater(vector<int>& nums1, int i1, vector<int>& nums2, int i2) {
        while (i1 < nums1.size() and i2 < nums2.size() and nums1[i1] == nums2[i2]) {
            ++i1; ++i2;
        }
        if (i1 == nums1.size() and i2 == nums2.size()) return false;
        if (i1 == nums1.size()) return false;
        if (i2 == nums2.size()) return true;
        return nums1[i1] > nums2[i2];
    }
    
    // create maximum number of length k from one array
    vector<int> maxNumberOne(vector<int>& nums, int k) {
        int n = nums.size();
        stack<int> toRight;
        for (int i = 0; i < n; ++i) {
            while (!toRight.empty() and toRight.top() < nums[i]
                  and n - i + toRight.size() > k) {
                toRight.pop();
            }
            if (toRight.size() < k) toRight.push(nums[i]);
        }
        vector<int> ans(k);
        for (int i = k - 1; i >= 0; --i) {
            ans[i] = toRight.top(); toRight.pop();
        }
        return ans;
    }
};
