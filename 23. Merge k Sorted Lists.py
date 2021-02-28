# method 1: use priority queue, time complexity: O(N log_k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:      
        dummyHead = ListNode(0)
        ptr = dummyHead
        
        q = PriorityQueue()
        for idx, l in enumerate(lists):
            if l:
                q.put((l.val, idx, l)) # put every list into the queue, use idx to avoid duplicates
        
        while not q.empty():
            val, idx, l = q.get() # get the smallest value
            ptr.next = ListNode(val)
            ptr = ptr.next
            
            # move to the next value and put it into the queue
            l = l.next
            if l:
                q.put((l.val, idx, l))
        
        return dummyHead.next