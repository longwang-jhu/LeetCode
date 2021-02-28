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
        iMin, iMax = 0, m
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = (m + n + 1) // 2 - i

            if i < m and A[i] < B[j-1]: # i is too small, must increase it
                iMin = i + 1
            elif i > 0 and A[i-1] > B[j]: # i is too large, must decrease it
                iMax = i - 1
            else: # i is good
                if i == 0:
                    maxOfLeft = B[j-1]
                elif j == 0:
                    maxOfLeft = A[i-1]
                else:
                    maxOfLeft = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1: # odd
                    return maxOfLeft

                if i == m:
                    minOfRight = B[j]
                elif j == n:
                    minOfRight = A[i]
                else:
                    minOfRight = min(A[i], B[j])

                if (m + n) % 2 == 0: # even
                    return (maxOfLeft + minOfRight) / 2