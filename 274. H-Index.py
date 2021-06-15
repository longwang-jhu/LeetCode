# https://leetcode.com/problems/h-index/

# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their ith paper, return compute the
# researcher's h-index.

# According to the definition of h-index on Wikipedia: A scientist has an index h
# if h of their n papers have at least h citations each, and the other n − h
# papers have no more than h citations each.

# If there are several possible values for h, the maximum one is taken as the
# h-index.

################################################################################

# bucket sort
# bucket[count] = number of papers with count

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)
        for citation in citations:
            if citation >= n:
                bucket[n] += 1
            else:
                bucket[citation] += 1
                
        papers = 0
        for citation in range(n, -1, -1):
            papers += bucket[citation]
            if papers >= citation:
                return citation
        
        return 0
