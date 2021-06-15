# https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

###############################################################################

# foward traverse -> min_heap
# time: O(nlogk)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        if lists == [[]]: return None
        
        dummy = ListNode()
        curr = dummy
        min_heap = []
        # put every list into min_heap
        for idx, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, idx, node)) # use idx to avoid tie
        
        while min_heap:
            val, idx, node = heappop(min_heap) # get the smallest value
            curr.next = node
            curr = curr.next
            
            # move to the next value and put it into min_heap
            node = node.next
            if node:
                heappush(min_heap, (node.val, idx, node))
        
        return dummy.next