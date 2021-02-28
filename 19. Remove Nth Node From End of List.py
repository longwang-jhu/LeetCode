# two passes: find length first
# one pass: two pointers that n apart

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         # two passes
#         # find length first
#         length = 0
#         curr = head
#         while curr:
#             curr = curr.next
#             length += 1

#         # use a dummy Head
#         dummyHead = ListNode(0)
#         dummyHead.next = head
#         curr = dummyHead
#         while length > n:
#             curr = curr.next
#             length -= 1
        
#         curr.next = curr.next.next
#         return dummyHead.next
    
        # one pass
        dummyHead = ListNode(0)
        dummyHead.next = head
        fast = dummyHead
        slow = dummyHead
        
        # move fast first n time
        i = 0
        while i < n:
            fast = fast.next
            i += 1
        
        # move fast and slow the same time
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummyHead.next
        