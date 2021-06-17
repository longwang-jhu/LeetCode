// https://leetcode.com/problems/kth-largest-element-in-an-array/

// Given an integer array nums and an integer k, return the kth largest element in
// the array.

// Note that it is the kth largest element in the sorted order, not the kth
// distinct element.

////////////////////////////////////////////////////////////////////////////////

// quick selection, sort(nums)[n-k]
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        k = nums.size() - k; // find sort(nums)[n-k]
        quickSelect(nums, 0, nums.size() - 1, k);
        return nums[k];
    }
private:    
    int partition(vector<int>& nums, int l, int r, int p) {
        int pVal = nums[p]; swap(nums[p], nums[r]);
        int anchor = l;
        for (int i = l; i < r; ++i) {
            if (nums[i] < pVal) swap(nums[anchor++], nums[i]);
        }
        swap(nums[anchor], nums[r]);
        return anchor;
    }
    void quickSelect(vector<int>& nums, int l, int r, int k) {
        int m = l + (r - l) / 2; // use m as pivot
        int p = partition(nums, l, r, m);
        if (p == k) return;
        if (p > k) quickSelect(nums, l, p - 1, k);
        else quickSelect(nums, p + 1, r, k);
        return;
    }
};
