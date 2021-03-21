# split list, reverse 2nd part, merge 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        mid = self.find_mid_node(head) # find mid node
        tail = self.reverse(mid.next) # reverse the 2nd part
        
        mid.next = None
        self.merge(head, tail)
    
    def find_mid_node(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev
        
    def merge(self, head1, head2):
        sign = 1
        dummy = ListNode()
        curr = dummy
        
        while head1 and head2:
            if sign == 1:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
            sign *= -1
        
        if head1:
            curr.next = head1
        else:
            curr.next = head2