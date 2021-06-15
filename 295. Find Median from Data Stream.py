# https://leetcode.com/problems/find-median-from-data-stream/

# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value and the median is the mean of the two
# middle values.

# Implement the MedianFinder class:

################################################################################

# use heapq
# small = the smaller half of the list, max heap (push in -num)
# large = # the larger half of the list, min heap

from heapq import * # python uses min_heap
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # the smaller half of the list, max heap (push in -num)
        self.large = [] # the larger half of the list, min heap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.small, -num) # push to smaller half
            heappush(self.large, -heappop(self.small)) # make sure small <= large
        else: # len(small) < len(large)
            heappush(self.large, num) # push to larger half
            heappush(self.small, -heappop(self.large)) # make sure small <= large
    
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else: # len(small) < len(large)
            return self.large[0]
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
