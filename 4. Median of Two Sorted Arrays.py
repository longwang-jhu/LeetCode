# method 1
# find the kth largest number, where k is middel of length
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (m + n) % 2 == 1:
            return find_kth_large(nums1, 0, nums2, 0, (m + n) // 2 + 1)
        else:
            return (find_kth_large(nums1, 0, nums2, 0, (m + n) // 2) 
                    + find_kth_large(nums1, 0, nums2, 0, (m + n) // 2 + 1)) / 2
    
    def find_kth_large(A, left_A, B, left_B, k):
        # check if remainding list is empty
        if left_A > len(A):
            return A[left_A + k - 1]
        if left_B > len(B):
            return B[left_B + k - 1]
        
        if k == 1: # exit case
            return min(A[0], B[0])
        
        if left_A + k // 2 + 1 > len(A):
            value_A = 2 ** 31 - 1
        else:
            value_A = A[left_A + k // 2 + 1]

        if left_B + k // 2 + 1 > len(B):
            value_B = 2 ** 31 - 1
        else:
            value_B = B[left_B + k // 2 + 1]
        
        if value_A < value_B: # dump first k//2 of A
            return find_kth_large(A, left_A + k // 2, left_B, 0, k - k // 2)
        else: # dump first k // 2 of B
            return find_kth_large(A, left_A, left_B + k // 2, 0, k - k // 2)

# method 2
# median: length of left part == length of right part
# A[0]--A[i-1] | A[i]--A[m-1]
# B[0]--B[j-1] | B[j]--B[n-1]
# need i + j = m - i + n - j (even) or i + j = m - i + n - j + 1 (odd) => set j = (m+n+1)/2 - i

# binary search over i and verify A[i-1] <= B[j] and B[j-1] <= A[i]
# return max(left) if odd and (max(left) + min(right)) / 2 if even

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        if m > n: A, B, m, n = B, A, n, m # make sure len(A) <= len(B)
        
        # binary search over i
        i_left, i_right = 0, m
        while i_left <= i_right:
            i = i_left + (i_right - i_left) // 2
            j = (m + n + 1) // 2 - i # if m + n is odd, left side has one more number
            
            if i < m and A[i] < B[j-1]: # i is too small, must increase it
                i_left = i + 1
            elif i > 0 and A[i-1] > B[j]: # i is too large, must decrease it
                i_right = i - 1
            else: # i is good
                if i == 0:
                    max_left = B[j-1]
                elif j == 0:
                    max_left = A[i-1]
                else:
                    max_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1: # odd
                    return max_left
                    
                if i == m:
                    min_right = B[j]
                elif j == n:
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])

                if (m + n) % 2 == 0: # even
                    return (max_left + min_right) / 2