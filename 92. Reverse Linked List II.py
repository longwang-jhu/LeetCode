# one-pass, filp on the way
# 1) move (prev, curr) to (start_prev, start)
# 2) record (start_prev, start) for reconnecting
# 3) move (prev, curr) to (start, start_next) and start to filp
# 4) reconnect start_prev.next = end, start.next = end_next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head

        prev, curr = dummy, head
        for _ in range(left - 1): # move (prev, curr) to (start_prev, start)
            prev, curr = curr, curr.next
            
        start_prev, start = prev, curr # record (start_prev, start) for reconnecting
        
        prev, curr = curr, curr.next # move (prev, curr) to (start, start_next)
        for _ in range(right - left): # filp (right - left) times
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
            
        # prev is at end, curr is at end_next
        end, end_next = prev, curr
        
        # reconnect
        start_prev.next = end
        start.next = end_next

        return dummy.next