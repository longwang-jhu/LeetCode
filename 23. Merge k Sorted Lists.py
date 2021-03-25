# https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

###############################################################################

# use priority queue
# time comp: O(n logk)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:      
        dummy = ListNode()
        curr = dummy
        pq = PriorityQueue()
        
        # put every list into the queue, use idx to avoid tie of head.val
        for idx, head in enumerate(lists):
            if head:
                pq.put((head.val, idx, head))
        
        while not pq.empty():
            val, idx, head = pq.get() # get the smallest value
            curr.next = head
            curr = curr.next
            
            # move to the next value and put it into the queue
            head = head.next
            if head:
                pq.put((head.val, idx, head))
        
        return dummy.next