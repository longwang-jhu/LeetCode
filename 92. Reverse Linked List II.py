# one-pass, filp on the way: prev -> start -> ... -> end -> ...

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None

        prev, curr = None, head
        for _ in range(left - 1): # move curr to the start node
            prev, curr = curr, curr.next
        
        before_start, start = prev, curr
        start = curr
        
        prev, curr = curr, curr.next
        for _ in range(right - left): # filp the link left - right times
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        # prev is at end, curr is at end_after

        # reconnect
        if left == 1:
            head = prev
        else:
            before_start.next = prev
        
        start.next = curr

        return head