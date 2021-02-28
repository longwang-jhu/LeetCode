# use dummyHead and a pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        curr = dummyHead
        
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val
            
            if v1 < v2:
                curr.next = ListNode(v1)
                l1 = l1.next
            else:
                curr.next = ListNode(v2)
                l2 = l2.next
            curr = curr.next
        
        if l1: curr.next = l1
        if l2: curr.next = l2
        
        return dummyHead.next