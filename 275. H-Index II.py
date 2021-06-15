# https://leetcode.com/problems/h-index-ii/

# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their ith paper and citations is sorted in
# an ascending order, return compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: A scientist has an index h
# if h of their n papers have at least h citations each, and the other n − h
# papers have no more than h citations each.

# If there are several possible values for h, the maximum one is taken as the
# h-index.

# You must write an algorithm that runs in logarithmic time.

################################################################################

# binary search
# find smallest i such that citations[i] >= n - i
# return n - i

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        if len(citations) == 1:
            return 0 if citations[0] == 0 else 1
        
        n = len(citations)
        left, right = 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if citations[mid] >= n - mid:
                right = mid
            else:
                left = mid
        
        if citations[left] >= n - left:
            return n - left
        if citations[right] >= n - right:
            return n - right
        return 0
