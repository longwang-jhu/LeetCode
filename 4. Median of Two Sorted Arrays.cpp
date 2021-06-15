// https://leetcode.com/problems/median-of-two-sorted-arrays/

// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
// median of the two sorted arrays.

// The overall run time complexity should be O(log (m+n)).

////////////////////////////////////////////////////////////////////////////////

// median and sorted -> kth number -> divide and conquer
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size();
        if ((n1 + n2) % 2 == 1) { // odd
            return getKth(nums1, 0, nums2, 0, (n1 + n2) / 2 + 1);
        } else { // even
            return (getKth(nums1, 0, nums2, 0, (n1 + n2) / 2)
                    + getKth(nums1, 0, nums2, 0, (n1 + n2) / 2 + 1)) / 2.0;
        }
    }

    // get kth number from nums1[start1...] and nums2[start2...]
    int getKth(vector<int>& nums1, int start1,
               vector<int>& nums2, int start2, int k) {
        int n1 = nums1.size(), n2 = nums2.size();
        // exit case
        if (start1 > n1 - 1) return nums2[start2 + k - 1]; // no more nums1
        if (start2 > n2 - 1) return nums1[start1 + k - 1]; // no more nums2
        if (k == 1) return min(nums1[start1], nums2[start2]);
        
        // find k/2th number of nums1 and nums2
        int curr1 = start1 + k / 2 - 1;
        int curr2 = start2 + k / 2 - 1;
        int val1 = (curr1 < n1) ? nums1[curr1] : INT_MAX;
        int val2 = (curr2 < n2) ? nums2[curr2] : INT_MAX;
        
        // dump the smaller k/2 numbers
        if (val1 < val2) {
            return getKth(nums1, start1 + k / 2, nums2, start2, k - k / 2);
        } else {
            return getKth(nums1, start1, nums2, start2 + k / 2, k - k / 2);
        }
    }
};
