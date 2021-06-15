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
        k = nums.size() - k;
        quickSelect(nums, 0, nums.size() - 1, k);
        return nums[k];
    }
    
    int partition(vector<int> &nums, int left, int right, int piv) {
        int pivVal = nums[piv];
        swap(nums[piv], nums[right]);
        int anchor = left;
        for (int i = left; i < right; ++i) {
            if (nums[i] < pivVal) swap(nums[anchor++], nums[i]);
        }
        swap(nums[anchor], nums[right]);
        return anchor;
    }
    
    void quickSelect(vector<int> &nums, int left, int right, int k) {
        // use mid as piv
        int mid = left + (right - left) / 2;
        int piv = partition(nums, left, right, mid);
        
        if (piv == k) return;
        else if (piv > k) quickSelect(nums, left, piv - 1, k);
        else quickSelect(nums, piv + 1, right, k);
        return;
    }
};
