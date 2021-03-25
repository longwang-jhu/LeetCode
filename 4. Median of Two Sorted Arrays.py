# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.

###############################################################################

# binary search: find kth number
# compare k//2-th of A and B and dump the smaller one

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1: # odd
            return self.find_kth(nums1, 0, nums2, 0, (m + n) // 2 + 1)
        else: # even
            return (self.find_kth(nums1, 0, nums2, 0, (m + n) // 2) 
                    + self.find_kth(nums1, 0, nums2, 0, (m + n) // 2 + 1)) / 2
    
    # find kth number of A[A_start:] and B[B_start]
    def find_kth(self, A, A_start, B, B_start, k):
        # exit case
        if A_start > len(A) - 1: # no more A
            return B[B_start + k - 1] # get kth number in B
        if B_start > len(B) - 1: # no more B
            return A[A_start + k - 1] # get kth number in A       
        if k == 1:
            return min(A[A_start], B[B_start])
        
        # find k//2th number of A and B (dump the smaller one)
        if A_start + k // 2 - 1 < len(A):
            A_val = A[A_start + k // 2 - 1]
        else:
            A_val = 2 ** 31 - 1

        if B_start + k // 2 - 1 < len(B):
            B_val = B[B_start + k // 2 - 1]
        else:
            B_val = 2 ** 31 - 1 
        
        if A_val < B_val: # dump k//2th more of A
            return self.find_kth(A, A_start + k // 2, B, B_start, k - k // 2)
        else: # dump k//2th more of B
            return self.find_kth(A, A_start, B, B_start + k // 2, k - k // 2)

# median: length of left part == length of right part
# A[0]--A[i-1] | A[i]--A[m-1]
# B[0]--B[j-1] | B[j]--B[n-1]
# need i + j = m - i + n - j (even) or i + j = m - i + n - j + 1 (odd) => set j = (m+n+1)/2 - i

# binary search over i and verify A[i-1] <= B[j] and B[j-1] <= A[i]
# return max(left) if odd and (max(left) + min(right)) / 2 if even

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         A, B, m, n = nums1, nums2, len(nums1), len(nums2)
#         if m > n: A, B, m, n = B, A, n, m # make sure len(A) <= len(B)
        
#         # binary search over i
#         i_left, i_right = 0, m
#         while i_left <= i_right:
#             i = i_left + (i_right - i_left) // 2
#             j = (m + n + 1) // 2 - i # if m + n is odd, left side has one more number
            
#             if i < m and A[i] < B[j-1]: # i is too small, must increase it
#                 i_left = i + 1
#             elif i > 0 and A[i-1] > B[j]: # i is too large, must decrease it
#                 i_right = i - 1
#             else: # i is good
#                 if i == 0:
#                     max_left = B[j-1]
#                 elif j == 0:
#                     max_left = A[i-1]
#                 else:
#                     max_left = max(A[i-1], B[j-1])

#                 if (m + n) % 2 == 1: # odd
#                     return max_left
                    
#                 if i == m:
#                     min_right = B[j]
#                 elif j == n:
#                     min_right = A[i]
#                 else:
#                     min_right = min(A[i], B[j])

#                 if (m + n) % 2 == 0: # even
#                     return (max_left + min_right) / 2